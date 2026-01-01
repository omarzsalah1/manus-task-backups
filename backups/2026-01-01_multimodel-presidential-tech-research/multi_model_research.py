#!/usr/bin/env python3
"""
Multi-Model Deep Research via OpenRouter API
Sends research prompt to 8 models in parallel and saves results
"""

import os
import json
import asyncio
import aiohttp
from datetime import datetime

# OpenRouter API configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Models to query - CORRECTED model IDs based on OpenRouter availability
MODELS = {
    # RESEARCH TIER (Web-grounded + Citations)
    "perplexity/sonar-deep-research": "Research Tier - Best for multi-step research",
    "perplexity/sonar-pro": "Research Tier - In-depth queries with citations",
    
    # REASONING TIER (Complex Analysis)
    "deepseek/deepseek-v3.2": "Reasoning Tier - GPT-5 class, excellent reasoning",
    "anthropic/claude-opus-4.5": "Reasoning Tier - Frontier reasoning model",
    "openai/gpt-5.2": "Reasoning Tier - Latest OpenAI flagship",
    
    # DIVERSE PERSPECTIVES TIER
    "google/gemini-3-pro-preview": "Diverse Tier - Google's flagship",
    "x-ai/grok-4": "Diverse Tier - xAI's reasoning model",
    "qwen/qwen3-235b-a22b": "Diverse Tier - Cost-effective, strong performance",
}

# Read the research prompt
with open("/home/ubuntu/research_prompt.txt", "r") as f:
    RESEARCH_PROMPT = f.read()

# System prompt for structured output
SYSTEM_PROMPT = """You are a deep research specialist focusing on esoteric, hyper-specific technical details. 
Your task is to provide comprehensive, well-sourced research with exact specifications, model numbers, dates, and technical details.
Avoid generic or obvious information - focus on the obscure, fascinating, and little-known facts.

You MUST return your response as valid JSON with these exact fields:
{
    "model_name": "your model identifier",
    "main_response": "your detailed research findings with specific technical details",
    "evidence": ["list of sources, documents, and evidence supporting your findings"],
    "confidence_score": 7,  // integer 1-10
    "strengths": ["list of strengths of your research approach"],
    "limitations": ["list of limitations or caveats"],
    "alternatives": ["alternative perspectives or approaches to consider"]
}"""


async def query_model(session: aiohttp.ClientSession, model_id: str, tier: str) -> dict:
    """Query a single model via OpenRouter API"""
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://manus.ai",
        "X-Title": "Presidential Tech Research"
    }
    
    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": RESEARCH_PROMPT}
        ],
        "temperature": 0.7,
        "max_tokens": 8000,
    }
    
    start_time = datetime.now()
    
    try:
        async with session.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=aiohttp.ClientTimeout(total=300)) as response:
            elapsed = (datetime.now() - start_time).total_seconds()
            
            if response.status == 200:
                result = await response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                usage = result.get("usage", {})
                
                # Try to parse as JSON
                try:
                    # Find JSON in the response (might be wrapped in markdown)
                    if "```json" in content:
                        json_str = content.split("```json")[1].split("```")[0].strip()
                    elif "```" in content:
                        json_str = content.split("```")[1].split("```")[0].strip()
                    else:
                        json_str = content
                    
                    parsed = json.loads(json_str)
                    parsed["model_name"] = model_id
                except (json.JSONDecodeError, IndexError):
                    # If JSON parsing fails, wrap the raw response
                    parsed = {
                        "model_name": model_id,
                        "main_response": content,
                        "evidence": [],
                        "confidence_score": 0,
                        "strengths": [],
                        "limitations": ["Response was not in JSON format"],
                        "alternatives": []
                    }
                
                return {
                    "model_id": model_id,
                    "tier": tier,
                    "status": "success",
                    "response": parsed,
                    "raw_content": content,
                    "usage": usage,
                    "elapsed_seconds": elapsed
                }
            else:
                error_text = await response.text()
                return {
                    "model_id": model_id,
                    "tier": tier,
                    "status": "error",
                    "error": f"HTTP {response.status}: {error_text[:200]}",
                    "elapsed_seconds": elapsed
                }
                
    except asyncio.TimeoutError:
        elapsed = (datetime.now() - start_time).total_seconds()
        return {
            "model_id": model_id,
            "tier": tier,
            "status": "timeout",
            "error": "Request timed out after 300 seconds",
            "elapsed_seconds": elapsed
        }
    except Exception as e:
        elapsed = (datetime.now() - start_time).total_seconds()
        return {
            "model_id": model_id,
            "tier": tier,
            "status": "error",
            "error": str(e),
            "elapsed_seconds": elapsed
        }


async def run_parallel_queries():
    """Run all model queries in parallel"""
    
    print(f"Starting parallel queries to {len(MODELS)} models...")
    print(f"API Key present: {bool(OPENROUTER_API_KEY)}")
    print("-" * 60)
    
    async with aiohttp.ClientSession() as session:
        tasks = [
            query_model(session, model_id, tier)
            for model_id, tier in MODELS.items()
        ]
        
        results = await asyncio.gather(*tasks)
    
    # Organize results
    all_results = {
        "timestamp": datetime.now().isoformat(),
        "total_models": len(MODELS),
        "successful": 0,
        "failed": 0,
        "results": []
    }
    
    for result in results:
        all_results["results"].append(result)
        if result["status"] == "success":
            all_results["successful"] += 1
            print(f"✓ {result['model_id']}: Success ({result['elapsed_seconds']:.1f}s)")
        else:
            all_results["failed"] += 1
            print(f"✗ {result['model_id']}: {result['status']} - {result.get('error', 'Unknown error')[:100]}")
    
    print("-" * 60)
    print(f"Completed: {all_results['successful']} successful, {all_results['failed']} failed")
    
    # Save results
    with open("/home/ubuntu/model_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nResults saved to /home/ubuntu/model_results.json")
    
    return all_results


if __name__ == "__main__":
    asyncio.run(run_parallel_queries())

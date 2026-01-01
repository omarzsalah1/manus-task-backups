#!/usr/bin/env python3
"""
Synthesize multi-model research results using Claude Opus 4.5
"""

import json
import requests
from datetime import datetime

# OpenRouter API configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Load model results
with open("/home/ubuntu/model_results.json", "r") as f:
    model_results = json.load(f)

# Prepare summary of all model responses for synthesis
model_summaries = []
for result in model_results["results"]:
    if result["status"] == "success":
        response = result["response"]
        summary = {
            "model_id": result["model_id"],
            "tier": result["tier"],
            "elapsed_seconds": result["elapsed_seconds"],
            "main_response": response.get("main_response", "")[:8000],  # Truncate if too long
            "evidence": response.get("evidence", []),
            "confidence_score": response.get("confidence_score", 0),
            "strengths": response.get("strengths", []),
            "limitations": response.get("limitations", []),
            "alternatives": response.get("alternatives", []),
            "usage": result.get("usage", {})
        }
        model_summaries.append(summary)

# Create synthesis prompt
SYNTHESIS_PROMPT = f"""You are a master synthesizer analyzing research outputs from 8 different AI models on the topic of "Esoteric Presidential Technology."

## MODEL OUTPUTS TO ANALYZE:

{json.dumps(model_summaries, indent=2)}

## YOUR TASK:

Produce TWO comprehensive outputs:

### OUTPUT 1: COMBINED_BEST_OUTPUT

Analyze all model responses and create:

1. **final_result**: The best synthesized answer combining the strongest elements from all models. Include specific model numbers, dates, weights, frequencies, and technical specifications. This should be the definitive, comprehensive answer.

2. **why_this_result**: Explain your synthesis methodology with citations to specific model outputs (e.g., "DeepSeek provided the most accurate Motorola model number...")

3. **alternative_approaches**: 2-3 other notable approaches from the models that offer valid but different perspectives

4. **consensus_elements**: What did multiple models agree on? Weight by their confidence scores.

5. **unique_contributions**: What did only ONE model find that others missed? These are gems.

6. **conflicting_findings**: Where did models disagree? Analyze why and which is more likely correct.

7. **recommended_next_steps**: What should the researcher do next to verify or expand on these findings?

### OUTPUT 2: MODEL_PERFORMANCE_REPORT

Evaluate each model's performance:

1. **best_overall**: Which model provided the best overall response and why?
2. **most_creative**: Which model found the most unexpected/esoteric details?
3. **most_thorough**: Which model was most comprehensive?
4. **most_practical**: Which model gave the most usable information?
5. **best_understanding**: Which model best understood the assignment (esoteric, specific, not obvious)?

6. **quality_ranking**: Rank all 8 models from best to worst with justification for each

7. **notable_differences**: How did the approaches vary between models?

8. **synthesis_insights**: What patterns did you observe across models?

9. **cost_efficiency_notes**: Based on response quality vs. response time, which models provided best value?

## OUTPUT FORMAT:

Return your analysis as valid JSON with this exact structure:
{{
    "combined_best_output": {{
        "final_result": "...",
        "why_this_result": "...",
        "alternative_approaches": ["...", "..."],
        "consensus_elements": ["...", "..."],
        "unique_contributions": {{"model_id": "contribution", ...}},
        "conflicting_findings": [{{"topic": "...", "models_disagreed": [...], "analysis": "..."}}],
        "recommended_next_steps": ["...", "..."]
    }},
    "model_performance_report": {{
        "best_overall": {{"model": "...", "reason": "..."}},
        "most_creative": {{"model": "...", "reason": "..."}},
        "most_thorough": {{"model": "...", "reason": "..."}},
        "most_practical": {{"model": "...", "reason": "..."}},
        "best_understanding": {{"model": "...", "reason": "..."}},
        "quality_ranking": [{{"rank": 1, "model": "...", "justification": "..."}}, ...],
        "notable_differences": "...",
        "synthesis_insights": "...",
        "cost_efficiency_notes": "..."
    }}
}}
"""

def run_synthesis():
    """Run synthesis using Claude Opus 4.5"""
    
    print("Running synthesis with Claude Opus 4.5...")
    print("-" * 60)
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://manus.ai",
        "X-Title": "Presidential Tech Research Synthesis"
    }
    
    payload = {
        "model": "anthropic/claude-opus-4.5",
        "messages": [
            {"role": "user", "content": SYNTHESIS_PROMPT}
        ],
        "temperature": 0.3,
        "max_tokens": 16000,
    }
    
    start_time = datetime.now()
    
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=300)
        elapsed = (datetime.now() - start_time).total_seconds()
        
        if response.status_code == 200:
            result = response.json()
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            usage = result.get("usage", {})
            
            print(f"✓ Synthesis complete ({elapsed:.1f}s)")
            print(f"  Tokens used: {usage.get('total_tokens', 'N/A')}")
            
            # Try to parse as JSON
            try:
                if "```json" in content:
                    json_str = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    json_str = content.split("```")[1].split("```")[0].strip()
                else:
                    json_str = content
                
                synthesis = json.loads(json_str)
            except (json.JSONDecodeError, IndexError) as e:
                print(f"  Warning: Could not parse JSON, saving raw content")
                synthesis = {"raw_content": content, "parse_error": str(e)}
            
            # Save synthesis results
            synthesis_output = {
                "timestamp": datetime.now().isoformat(),
                "synthesis_model": "anthropic/claude-opus-4.5",
                "elapsed_seconds": elapsed,
                "usage": usage,
                "synthesis": synthesis,
                "raw_content": content
            }
            
            with open("/home/ubuntu/synthesis_results.json", "w") as f:
                json.dump(synthesis_output, f, indent=2)
            
            print(f"\nSynthesis saved to /home/ubuntu/synthesis_results.json")
            return synthesis_output
            
        else:
            print(f"✗ Synthesis failed: HTTP {response.status_code}")
            print(f"  Error: {response.text[:500]}")
            return None
            
    except Exception as e:
        print(f"✗ Synthesis error: {str(e)}")
        return None


if __name__ == "__main__":
    run_synthesis()

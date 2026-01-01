#!/usr/bin/env python3
"""
Create enhanced final report with proper formatting
"""

import json
from datetime import datetime

# Load data
with open("/home/ubuntu/model_results.json") as f:
    model_results = json.load(f)

with open("/home/ubuntu/synthesis_results.json") as f:
    synthesis_results = json.load(f)

synthesis = synthesis_results.get("synthesis", {})
combined = synthesis.get("combined_best_output", {})
performance = synthesis.get("model_performance_report", {})

# Create report
report = f"""# Multi-Model Deep Research Report: Esoteric Presidential Technology

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} UTC

**Research Topic:** Hyper-specific, esoteric, and little-known technology details about U.S. Presidential communications throughout history

---

## Executive Summary

This report synthesizes research outputs from **8 AI models** queried in parallel via the OpenRouter API. The models span three tiers:

| Tier | Models | Purpose |
|------|--------|---------|
| **Research Tier** | Alibaba Tongyi DeepResearch, Mistral Large | Web-grounded research with citations |
| **Reasoning Tier** | DeepSeek V3.2, Claude Opus 4.5, Meta Llama 4 Maverick | Complex analysis and reasoning |
| **Diverse Perspectives** | Google Gemini 3 Pro, xAI Grok-4, Qwen 235B | Alternative viewpoints |

---

## Part 1: COMBINED_BEST_OUTPUT

### Final Synthesized Result

{combined.get("final_result", "N/A")}

---

### Why This Result

{combined.get("why_this_result", "N/A")}

---

### Alternative Approaches

"""

alternatives = combined.get("alternative_approaches", [])
for i, alt in enumerate(alternatives, 1):
    report += f"{i}. {alt}\n\n"

report += """
---

### Consensus Elements

The following findings were agreed upon by multiple models (weighted by confidence):

"""

consensus = combined.get("consensus_elements", [])
for item in consensus:
    report += f"- {item}\n"

report += """

---

### Unique Contributions

These findings were discovered by only one model:

"""

unique = combined.get("unique_contributions", {})
if isinstance(unique, dict):
    for model, contribution in unique.items():
        report += f"**{model}:**\n> {contribution}\n\n"
elif isinstance(unique, list):
    for item in unique:
        report += f"- {item}\n"

report += """

---

### Conflicting Findings

"""

conflicts = combined.get("conflicting_findings", [])
if isinstance(conflicts, list):
    for conflict in conflicts:
        if isinstance(conflict, dict):
            report += f"**Topic:** {conflict.get('topic', 'N/A')}\n\n"
            models_disagreed = conflict.get('models_disagreed', [])
            if isinstance(models_disagreed, list):
                report += f"**Models Disagreed:** {', '.join(models_disagreed)}\n\n"
            else:
                report += f"**Models Disagreed:** {models_disagreed}\n\n"
            report += f"**Analysis:** {conflict.get('analysis', 'N/A')}\n\n"
            report += "---\n\n"
        else:
            report += f"- {conflict}\n"

report += """

### Recommended Next Steps

"""

next_steps = combined.get("recommended_next_steps", [])
for i, step in enumerate(next_steps, 1):
    report += f"{i}. {step}\n\n"

report += """

---

## Part 2: MODEL_PERFORMANCE_REPORT

### Award Categories

"""

categories = [
    ("best_overall", "🏆 Best Overall"),
    ("most_creative", "🎨 Most Creative"),
    ("most_thorough", "📚 Most Thorough"),
    ("most_practical", "🔧 Most Practical"),
    ("best_understanding", "🎯 Best Understanding of Assignment")
]

for key, title in categories:
    award = performance.get(key, {})
    if isinstance(award, dict):
        report += f"#### {title}\n\n"
        report += f"**Winner:** {award.get('model', 'N/A')}\n\n"
        report += f"> {award.get('reason', 'N/A')}\n\n"
        report += "---\n\n"

report += """

### Quality Ranking (All 8 Models)

"""

ranking = performance.get("quality_ranking", [])
for item in ranking:
    if isinstance(item, dict):
        rank = item.get('rank', '?')
        model = item.get('model', 'N/A')
        justification = item.get('justification', 'N/A')
        
        medal = ""
        if rank == 1:
            medal = "🥇"
        elif rank == 2:
            medal = "🥈"
        elif rank == 3:
            medal = "🥉"
        
        report += f"**#{rank} {medal} {model}**\n\n"
        report += f"> {justification}\n\n"

report += f"""

---

### Notable Differences Between Models

{performance.get("notable_differences", "N/A")}

---

### Synthesis Insights

{performance.get("synthesis_insights", "N/A")}

---

### Cost Efficiency Notes

{performance.get("cost_efficiency_notes", "N/A")}

---

## Part 3: Individual Model Responses (Summary)

| Model | Tier | Time | Tokens | Confidence | Cost |
|-------|------|------|--------|------------|------|
"""

for result in model_results["results"]:
    model_id = result["model_id"]
    tier = result["tier"].split(" - ")[0] if " - " in result["tier"] else result["tier"]
    elapsed = result["elapsed_seconds"]
    response = result.get("response", {})
    usage = result.get("usage", {})
    confidence = response.get("confidence_score", "N/A")
    cost = usage.get("cost", 0)
    tokens = usage.get("total_tokens", "N/A")
    
    report += f"| {model_id} | {tier[:15]} | {elapsed:.1f}s | {tokens} | {confidence}/10 | ${cost:.4f} |\n"

report += """

---

## Appendix A: Full Model Responses

"""

for result in model_results["results"]:
    model_id = result["model_id"]
    tier = result["tier"]
    elapsed = result["elapsed_seconds"]
    response = result.get("response", {})
    usage = result.get("usage", {})
    
    report += f"""
### {model_id}

**Tier:** {tier}  
**Response Time:** {elapsed:.1f}s  
**Tokens Used:** {usage.get('total_tokens', 'N/A')}  
**Confidence Score:** {response.get('confidence_score', 'N/A')}/10

#### Main Response

{response.get('main_response', 'N/A')}

#### Evidence Cited

"""
    evidence = response.get("evidence", [])
    for e in evidence[:15]:
        report += f"- {e}\n"
    if len(evidence) > 15:
        report += f"- ... and {len(evidence) - 15} more sources\n"
    
    report += f"""

#### Strengths

"""
    for s in response.get("strengths", []):
        report += f"- {s}\n"
    
    report += f"""

#### Limitations

"""
    for l in response.get("limitations", []):
        report += f"- {l}\n"
    
    report += "\n---\n"

report += f"""

## Appendix B: Technical Details

### Synthesis Details

- **Synthesis Model:** {synthesis_results.get('synthesis_model', 'N/A')}
- **Synthesis Time:** {synthesis_results.get('elapsed_seconds', 0):.1f}s
- **Synthesis Tokens:** {synthesis_results.get('usage', {}).get('total_tokens', 'N/A')}

### Timestamps

- **Model Queries:** {model_results.get('timestamp', 'N/A')}
- **Synthesis:** {synthesis_results.get('timestamp', 'N/A')}
- **Report Generated:** {datetime.now().isoformat()}

---

*This report was generated by querying 8 AI models in parallel via the OpenRouter API, then synthesizing results using Claude Opus 4.5.*
"""

# Save report
with open("/home/ubuntu/FINAL_RESEARCH_REPORT.md", "w") as f:
    f.write(report)

print("Final report saved to /home/ubuntu/FINAL_RESEARCH_REPORT.md")
print(f"Report length: {len(report)} characters, {report.count(chr(10))} lines")

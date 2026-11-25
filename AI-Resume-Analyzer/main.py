from ollama import chat
import json

print("=" * 60)
print("                AI RESUME ANALYZER")
print("=" * 60)

print("\nEnter the candidate's resume.")
resume=input(">")

print("\n Enter the job description.")
job_description=input("> ")

print("\n Resume and job description received.")


prompt = f"""
You are an AI resume analyzer.

Compare the candidate's resume with the job description.

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

Analyze:

1. Match score from 0 to 100
2. Skills mentioned in both
3. Skills required by the job but missing from the resume
4. Candidate strengths
5. Candidate gaps
6. Overall recommendation

Return ONLY valid JSON.

Use exactly this structure:

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "strengths": [],
    "gaps": [],
    "recommendation": ""
}}

Do not add explanations or markdown outside the JSON.
"""
print("\nAnalyze resume with Qwen...\n")

response= chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

ai_result = response["message"]["content"]

try:
    result = json.loads(ai_result)
    
    print("=" * 60)
    print("      AI RESUME ANALYSIS")
    print("=" * 60)
    
    print("Match Score: ", result["match_score"], "/ 100")
    
    print("\n Matched Skills:")
    for skill in result ["matched_skills"]:
        print("-", skill)
        
    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print("-", skill)
    print("\nStrengths:")
    for strength in result["strengths"]:
        print("-", strength)

    print("\nGaps:")
    for gap in result["gaps"]:
        print("-", gap)

    print("\nRecommendation:")
    print(result["recommendation"])

    print("=" * 60)

except json.JSONDecodeError:
    print("Qwen did not return valid JSON.")
    print("\nRaw AI response:")
    print(ai_result)    

# ============================================================
# APPLICATION DECISION
# ============================================================

score = result["match_score"]

print("\n" + "-" * 60)
print("             APPLICATION DECISION")
print("-" * 60)

if score >= 80:
    decision = "STRONG MATCH"
    advice = "Apply. The candidate has a strong match with the job requirements."

elif score >= 60:
    decision = "POSSIBLE MATCH"
    advice = "Apply, but consider improving the missing skills."

elif score >= 40:
    decision = "WEAK MATCH"
    advice = "The candidate has several skill gaps. Consider improving them first."

else:
    decision = "LOW MATCH"
    advice = "This position may not be suitable without significant skill development."

print("Decision:", decision)
print("Advice:", advice)

print("=" * 60)
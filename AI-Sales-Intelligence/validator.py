from ollama import chat


def validate_ai_response(ai_response, company_data):

    prompt = f"""
You are an AI Output Quality Evaluator.

COMPANY DATA
------------
Company: {company_data["company"]}
Industry: {company_data["industry"]}
Location: {company_data["location"]}
Employees: {company_data["employees"]}
Website Status: {company_data["website_status"]}


AI RESPONSE
-----------
{ai_response}


TASK
----
Identify claims in the AI response that are NOT supported by the
company data.

Examples of unsupported claims:

- The company is growing.
- The company has limited resources.
- The company has customer dissatisfaction.
- The company has supply-chain problems.
- The company is interested in buying services.

Do not treat recommendations as facts.

Do not treat the provided company information as unsupported.

The Python lead score is NOT evidence of buying intent.

Return ONLY these sections:


UNSUPPORTED CLAIMS:

List each unsupported claim.

If there are none, write:

None


BUYING INTENT VIOLATION:

YES or NO


FACT ACCURACY:

PASS or WARNING


INSTRUCTION FOLLOWING:

PASS or WARNING


EXPLANATION:

Briefly explain your findings.
"""

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
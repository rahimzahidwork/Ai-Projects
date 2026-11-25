from ollama import chat
from validator import validate_ai_response


# ============================================================
# AI SALES INTELLIGENCE ASSISTANT
# PROJECT 1
# ============================================================


print("=" * 60)
print("        AI SALES INTELLIGENCE ASSISTANT")
print("=" * 60)

print("\nEnter information about the company.\n")


# ============================================================
# 1. COMPANY INFORMATION
# ============================================================

company = input("Company name: ").strip()

industry = input("Industry: ").strip()

location = input("Location: ").strip()


# ============================================================
# 2. EMPLOYEE VALIDATION
# ============================================================

while True:

    try:
        employees = int(input("Number of employees: "))

        if employees < 0:
            print("Please enter a valid positive number.")
            continue

        break

    except ValueError:
        print("Please enter a number, for example: 35")


# ============================================================
# 3. WEBSITE STATUS
# ============================================================

website_status = input(
    "Website status (Good/Outdated/None): "
).strip()


# ============================================================
# 4. PYTHON LEAD SCORING
# ============================================================

lead_score = 0


target_industries = [
    "landscaping",
    "plumbing",
    "real estate",
    "restaurants"
]


target_locations = [
    "texas",
    "florida",
    "california"
]


# Industry score

if industry.lower() in target_industries:
    lead_score += 25


# Company size score

if employees >= 20:
    lead_score += 20


# Website score

if website_status.lower() == "outdated":
    lead_score += 30


# Location score

if location.lower() in target_locations:
    lead_score += 15


# ============================================================
# 5. DETERMINE EVIDENCE CONFIDENCE
# ============================================================

information_count = 0

if company:
    information_count += 1

if industry:
    information_count += 1

if location:
    information_count += 1

if employees >= 0:
    information_count += 1

if website_status:
    information_count += 1


if information_count == 5:
    evidence_confidence = "Moderate"

elif information_count >= 3:
    evidence_confidence = "Low"

else:
    evidence_confidence = "Very Low"


# ============================================================
# 6. CREATE AI PROMPT
# ============================================================

prompt = f"""
You are an AI Sales Intelligence Analyst.

Your job is to analyze a company using ONLY the information
provided by the user.

COMPANY INFORMATION
-------------------

Company: {company}
Industry: {industry}
Location: {location}
Employees: {employees}
Website Status: {website_status}

Python Lead Score: {lead_score}/90
Evidence Confidence: {evidence_confidence}


VERY IMPORTANT ACCURACY RULES
-----------------------------

RULE 1:
Never invent facts.

RULE 2:
Never assume the company is growing.

RULE 3:
Never assume the company has customer dissatisfaction.

RULE 4:
Never assume the company has limited resources.

RULE 5:
Never assume industry-specific problems unless they were
explicitly provided.

RULE 6:
The Python lead score is ONLY an internal qualification score.

It is NOT evidence of buying intent.

RULE 7:
Do not describe the company as interested in our services.

RULE 8:
If there is no evidence of buying intent, write:

"Buying intent: Unknown."

RULE 9:
Every inference must clearly be labeled INFERENCE.

RULE 10:
If information is unavailable, write:

"Unknown."

RULE 11:
Do not change the Python lead score.


YOUR RESPONSE MUST CONTAIN THESE SECTIONS
-----------------------------------------


1. ICP FIT

Explain whether the available information matches the
qualification criteria.

Do not claim that the company is definitely a good customer.


2. KNOWN FACTS

List ONLY facts directly provided by the user.


3. POTENTIAL PAIN POINTS

Only list potential problems that can reasonably be connected
to the provided information.

For every item use:

FACT:
or

INFERENCE:

Do not invent industry problems.


4. BUYING SIGNALS

Only list actual evidence of buying intent.

If there is no evidence, write:

"Buying intent: Unknown."


5. UNKNOWN INFORMATION

List important information that we do not have.


6. RECOMMENDED SALES APPROACH

Give a cautious sales strategy based only on the information
available.


7. PERSONALIZED OUTREACH

Write a short cold outreach message.

Do not claim the company has a problem unless the information
supports it.

Do not claim the company is interested.

Do not mention the Python score.


8. DATA QUALITY

State:

Evidence Confidence: {evidence_confidence}

Briefly explain why.
"""


# ============================================================
# 7. SEND TO QWEN
# ============================================================

print("\nAnalyzing company with Qwen...\n")


response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


# ============================================================
# 8. DISPLAY REPORT
# ============================================================

print("\n" + "=" * 60)
print("           AI SALES INTELLIGENCE REPORT")
print("=" * 60)

print(f"\nCompany: {company}")
print(f"Industry: {industry}")
print(f"Location: {location}")
print(f"Employees: {employees}")
print(f"Website Status: {website_status}")

print(f"\nPYTHON LEAD SCORE: {lead_score}/90")
print(f"EVIDENCE CONFIDENCE: {evidence_confidence}")

print("\n" + "-" * 60)
print("AI ANALYSIS")
print("-" * 60)

ai_response = response["message"]["content"]

print(ai_response)


# ============================================================
# 9. VALIDATE AI RESPONSE
# ============================================================

print("\n" + "-" * 60)
print("AI OUTPUT VALIDATION")
print("-" * 60)

company_data = {
    "company": company,
    "industry": industry,
    "location": location,
    "employees": employees,
    "website_status": website_status
}

validation_result = validate_ai_response(
    ai_response,
    company_data
)

print(validation_result)


# ============================================================
# 10. PYTHON FINAL VALIDATION DECISION
# ============================================================

print("\n" + "-" * 60)
print("PYTHON FINAL VALIDATION DECISION")
print("-" * 60)


validation_lower = validation_result.lower()


if "unsupported claims:\nnone" in validation_lower:
    final_result = "PASS"

else:
    final_result = "WARNING"


print(f"FINAL RESULT: {final_result}")

print("\n" + "=" * 60)
print("                 END OF REPORT")
print("=" * 60)
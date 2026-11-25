from ollama import chat
import json


print("=" * 60)
print("        AI CUSTOMER SUPPORT CLASSIFIER")
print("=" * 60)


# ============================================================
# 1. GET CUSTOMER MESSAGE
# ============================================================

ticket = input("\nEnter customer support message\n>")


# ============================================================
# 2. ASK QWEN TO CLASSIFY THE TICKET
# ============================================================

prompt = f"""
You are a customer support classification AI.

Analyze the following customer message:

"{ticket}"

Classify it into these categories:

Category:
- Billing
- Technical
- Account
- Delivery
- Refund
- Other

Priority:
- Low
- Medium
- High
- Urgent

Sentiment:
- Positive
- Neutral
- Negative

Intent:
Give a short description of what the customer wants.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "category": "Billing",
    "priority": "Medium",
    "sentiment": "Negative",
    "intent": "Refund"
}}

Do not add explanations, markdown, or anything outside the JSON.
"""


print("\nAnalyzing ticket...\n")


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
# 3. READ AI CLASSIFICATION
# ============================================================

print("=" * 60)
print("              CLASSIFICATION")
print("=" * 60)


ai_result = response["message"]["content"]


try:

    ticket_data = json.loads(ai_result)

    category = ticket_data["category"]
    priority = ticket_data["priority"]
    sentiment = ticket_data["sentiment"]
    intent = ticket_data["intent"]

    print("Category:", category)
    print("Priority:", priority)
    print("Sentiment:", sentiment)
    print("Intent:", intent)


except (json.JSONDecodeError, KeyError):

    print("AI did not return the expected JSON format.")
    print("\nRaw AI response:")
    print(ai_result)

    exit()


# ============================================================
# 4. ROUTING LOGIC
# ============================================================

if priority == "Urgent":

    assigned_team = "Priority Escalation Team"

elif category == "Billing":

    assigned_team = "Billing Team"

elif category == "Technical":

    assigned_team = "Technical Support Team"

elif category == "Account":

    assigned_team = "Account Support Team"

elif category == "Delivery":

    assigned_team = "Delivery Support Team"

elif category == "Refund":

    assigned_team = "Billing & Refund Team"

else:

    assigned_team = "General Support Team"


print("\n" + "-" * 60)
print("              TICKET ROUTING")
print("-" * 60)

print("Assigned Team:", assigned_team)
print("Reason:", f"{category} issue with intent: {intent}")


# ============================================================
# 5. GENERATE CUSTOMER RESPONSE
# ============================================================

response_prompt = f"""
You are a professional customer support assistant.

Customer message:

"{ticket}"

Ticket category: {category}
Priority: {priority}
Sentiment: {sentiment}
Intent: {intent}

Write a short, professional response to the customer.

Rules:

- Acknowledge the customer's problem.
- Be empathetic.
- Do not claim that a refund has already been processed.
- Do not invent information.
- Do not promise a specific refund time.
- Keep the response under 100 words.

Return ONLY the customer response.
Do not include analysis.
Do not include headings.
"""


print("\n" + "-" * 60)
print("          AI SUGGESTED RESPONSE")
print("-" * 60)

print("Qwen is generating the response...")


# Second Qwen request

response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": response_prompt
        }
    ]
)


suggested_response = response["message"]["content"].strip()


if suggested_response:

    print("\n" + suggested_response)

else:

    print("Qwen returned an empty response.")


print("\n" + "=" * 60)
print("                    END")
print("=" * 60)
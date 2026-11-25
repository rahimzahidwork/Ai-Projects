from ollama import chat
import json

print("=" * 60)
print("             AI MEETING ANALYZER")
print("=" * 60)

print("\nEnter your meeting notes.")
print("Type END when you are finished.")

lines = []

while True:
    line = input("> ")

    if line.strip().upper() == "END":
        break

    lines.append(line)

meeting_notes = "\n".join(lines)

print("\nMeeting notes received.")
print("Analyzing:", len(lines), "lines")

# ============================================================
# AI MEETING ANALYSIS
# ============================================================

prompt = f"""
You are an AI meeting analysis assistant.

Analyze the following meeting notes:

{meeting_notes}

Extract the following information:

1. A short meeting summary.
2. All action items.
3. The person responsible for each action item.
4. The deadline for each action item if one is mentioned.

Important rules:
- Only use information contained in the meeting notes.
- Do not invent names, tasks, or deadlines.
- If a responsible person or deadline is not mentioned, use "Not specified".
- Return ONLY valid JSON.

Use exactly this structure:

{{
    "summary": "",
    "action_items": [
        {{
            "task": "",
            "responsible": "",
            "deadline": ""
        }}
    ]
}}

Do not add markdown or explanations outside the JSON.
"""

print("\nSending meeting notes to Qwen...")

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
# READ AI RESULT
# ============================================================

ai_result = response["message"]["content"]

try:

    result = json.loads(ai_result)

    print("\n" + "=" * 60)
    print("              MEETING ANALYSIS")
    print("=" * 60)

    print("\nSUMMARY")
    print(result["summary"])

    print("\nACTION ITEMS")

    for number, item in enumerate(result["action_items"], start=1):

        print(f"\n{number}. {item['task']}")
        print("Responsible:", item["responsible"])
        print("Deadline:", item["deadline"])

    print("\n" + "=" * 60)

except json.JSONDecodeError:

    print("Qwen did not return valid JSON.")
    print("\nRaw AI response:")
    print(ai_result)
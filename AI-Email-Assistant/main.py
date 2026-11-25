from ollama import chat

print("=" * 60)
print("             AI EMAIL ASSISTANT")
print("=" * 60)


print("\nEnter the rough message you want to turn into an email.")

message = input("> ")

print("\nChoose the email tone:")
print("1. Professional")
print("2. Friendly")
print("3. Concise")
print("4. Apologetic")

tone_choice = input("\nEnter your choice (1-4): ")

if tone_choice == "1":
    tone = "Professional"

elif tone_choice == "2":
    tone = "Friendly"

elif tone_choice == "3":
    tone = "Concise"

elif tone_choice == "4":
    tone = "Apologetic"

else:
    tone = "Professional"

print("\n" + "=" * 60)
print("              EMAIL INFORMATION")
print("=" * 60)

print("Message:", message)
print("Tone:", tone)

print("\nInformation collected successfully.")

# ============================================================
# AI EMAIL GENERATION
# ============================================================

prompt = f"""
You are a professional email writing assistant.

Convert the following rough message into a well-written email.

Rough message:
"{message}"

Required tone:
{tone}

Rules:
- Keep the original meaning.
- Fix grammar and spelling.
- Make the email natural and professional.
- Do not invent facts.
- Do not invent names, dates, prices, or promises.
- Include a suitable subject line.
- Include a greeting and closing.
- Keep the email reasonably short.

Return only the finished email.
"""

print("\nGenerating email with Qwen...")

response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

email = response["message"]["content"]

print("\n" + "=" * 60)
print("              GENERATED EMAIL")
print("=" * 60)

print(email)

print("=" * 60)
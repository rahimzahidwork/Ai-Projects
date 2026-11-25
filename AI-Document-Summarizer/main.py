from ollama import chat



print("=" * 60)
print("          AI DOCUMENT SUMMARIZER")
print("=" * 60)

print("\nPaste your document below.")
print("Type END when you are finished.")

lines = []

while True:
    line = input("> ")

    if line.strip().upper() == "END":
        break

    lines.append(line)

document = "\n".join(lines)

print("\nChoose the summary type:")
print("1. Short Summary")
print("2. Detailed Summary")
print("3. Bullet Points")

choice = input("\nEnter your choice (1-3): ")

if choice == "1":
    summary_type = "Short Summary"

elif choice == "2":
    summary_type = "Detailed Summary"

elif choice == "3":
    summary_type = "Bullet Points"

else:
    summary_type = "Short Summary"

print("\n" + "=" * 60)
print("             DOCUMENT INFORMATION")
print("=" * 60)

print("Characters:", len(document))
print("Summary Type:", summary_type)

print("\nDocument received successfully.")

# ============================================================
# AI DOCUMENT SUMMARIZATION
# ============================================================

prompt = f"""
You are an AI document summarization assistant.

Summarize the following document.

DOCUMENT:
{document}

SUMMARY TYPE:
{summary_type}

Rules:
- Preserve the main meaning of the document.
- Do not invent facts.
- Do not add information that is not in the document.
- Remove unnecessary repetition.
- Make the result clear and easy to understand.

If the summary type is "Short Summary":
Write a concise paragraph of 2-3 sentences.

If the summary type is "Detailed Summary":
Write a more complete summary covering the important information.

If the summary type is "Bullet Points":
Use clear bullet points containing the most important information.

Return only the summary.
"""

print("\nAnalyzing document with Qwen...")

response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

summary = response["message"]["content"]

print("\n" + "=" * 60)
print("              AI SUMMARY")
print("=" * 60)

print(summary)

print("=" * 60)
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain what an LLM is in one simple sentence."
)

print(response.output_text)
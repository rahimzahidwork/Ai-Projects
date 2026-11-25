from sentence_transformers import SentenceTransformer, util
from ollama import chat

print("=" * 60)
print("          AI RAG KNOWLEDGE ASSISTANT")
print("=" * 60)

# ============================================================
# COMPANY KNOWLEDGE BASE
# ============================================================

documents = [
    "Customers can request a refund within 30 days of their purchase.",
    "Enterprise customers receive priority customer support.",
    "Standard support is available Monday to Friday from 9 AM to 6 PM.",
    "Customers can contact support through email or live chat.",
    "Refund requests must include the customer's order number.",
    "Technical issues should be reported to the technical support team.",
    "Business customers can request a dedicated account manager."
]

# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

print("\nLoading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded.")

# ============================================================
# CREATE DOCUMENT EMBEDDINGS
# ============================================================

document_embeddings = model.encode(
    documents,
    convert_to_tensor=True
)

print("Knowledge base indexed.")

# ============================================================
# USER QUESTION
# ============================================================

question = input("\nAsk a question about the company:\n> ")

print("\nSearching knowledge base...")

# Convert question into an embedding
question_embedding = model.encode(
    question,
    convert_to_tensor=True
)

# ============================================================
# SEMANTIC SEARCH
# ============================================================

similarities = util.cos_sim(
    question_embedding,
    document_embeddings
)[0]

results = []

for index, score in enumerate(similarities):
    results.append(
        (documents[index], float(score))
    )

# Highest similarity first
results.sort(
    key=lambda x: x[1],
    reverse=True
)

# Take the top 3 relevant documents
top_results = results[:3]

# ============================================================
# RETRIEVED CONTEXT
# ============================================================

context = "\n".join(
    document for document, score in top_results
)

print("\nRelevant information found.")

# ============================================================
# SEND RETRIEVED INFORMATION TO QWEN
# ============================================================

prompt = f"""
You are a company knowledge assistant.

Answer the user's question using ONLY the information provided
in the knowledge base.

KNOWLEDGE BASE:
{context}

USER QUESTION:
{question}

Rules:
- Use only the provided knowledge.
- Do not invent information.
- If the knowledge base does not contain the answer, say:
  "I don't have enough information to answer that."
- Give a clear and concise answer.
"""

print("\nGenerating answer with Qwen...")

response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

answer = response["message"]["content"]

# ============================================================
# DISPLAY ANSWER
# ============================================================

print("\n" + "=" * 60)
print("                 AI ANSWER")
print("=" * 60)

print(answer)

print("\n" + "-" * 60)
print("              RETRIEVED SOURCES")
print("-" * 60)

for document, score in top_results:
    print(f"\nSimilarity: {score:.3f}")
    print(document)

print("=" * 60)
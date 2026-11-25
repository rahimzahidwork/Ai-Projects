from sentence_transformers import SentenceTransformer, util

print("=" * 60)
print("             AI SEMANTIC SEARCH")
print("=" * 60)

# ============================================================
# KNOWLEDGE BASE
# ============================================================

documents = [
    "Our agency builds websites for restaurants.",
    "We provide SEO services for local businesses.",
    "We design e-commerce stores.",
    "We create social media marketing campaigns.",
    "We develop mobile applications for startups.",
    "We provide branding and logo design services.",
    "We build custom software solutions for businesses."
]

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

print("Knowledge base embedded successfully.")

# ============================================================
# USER QUERY
# ============================================================

query = input("\nWhat are you looking for?\n> ")

print("\nSearching by meaning...")

# Convert the user's query into an embedding
query_embedding = model.encode(
    query,
    convert_to_tensor=True
)

# ============================================================
# CALCULATE SIMILARITY
# ============================================================

similarities = util.cos_sim(
    query_embedding,
    document_embeddings
)[0]

# ============================================================
# FIND BEST MATCHES
# ============================================================

results = []

for index, score in enumerate(similarities):
    results.append((documents[index], float(score)))

results.sort(key=lambda x: x[1], reverse=True)

# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 60)
print("              SEARCH RESULTS")
print("=" * 60)

for document, score in results[:3]:
    print(f"\nSimilarity Score: {score:.3f}")
    print("Result:", document)

print("\n" + "=" * 60)
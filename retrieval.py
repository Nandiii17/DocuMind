import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("documents")

while True:

    query = input("\nAsk a question (or type exit): ")

    if query.lower() == "exit":
        break

    # Convert query to embedding
    query_embedding = model.encode(query).tolist()

    # Search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print("\nTop Results:\n")

    for i, doc in enumerate(results["documents"][0]):
        print(f"Result {i+1}:")
        print(doc)
        print("-" * 60)
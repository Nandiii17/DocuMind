import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_chunks(query, k=3):

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_collection(
        "documents"
    )

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0]
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_chunks(query, k=5):

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

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    retrieved_chunks = []

    for doc, metadata in zip(
        documents,
        metadatas
    ):

        retrieved_chunks.append(
            {
                "text": doc,
                "page": metadata["page"]
            }
        )

    return retrieved_chunks
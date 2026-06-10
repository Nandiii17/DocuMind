import chromadb


def store_chunks(chunks, embeddings):

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    # ==========================================
    # DELETE OLD COLLECTION
    # ==========================================

    try:
        client.delete_collection(
            name="documents"
        )
    except:
        pass

    # ==========================================
    # CREATE FRESH COLLECTION
    # ==========================================

    collection = client.get_or_create_collection(
        name="documents"
    )

    # ==========================================
    # CREATE IDS
    # ==========================================

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    # ==========================================
    # STORE CHUNKS
    # ==========================================

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    # ==========================================
    # RETURN COUNT
    # ==========================================

    return len(chunks)
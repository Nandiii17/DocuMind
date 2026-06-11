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
    # PREPARE DATA
    # ==========================================

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        {
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    # ==========================================
    # STORE IN CHROMADB
    # ==========================================

    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    # ==========================================
    # RETURN COUNT
    # ==========================================

    return len(chunks)
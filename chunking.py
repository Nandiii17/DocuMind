from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(pages):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks_with_metadata = []

    for page_data in pages:

        page_number = page_data["page"]
        page_text = page_data["text"]

        page_chunks = text_splitter.split_text(
            page_text
        )

        for chunk in page_chunks:

            chunks_with_metadata.append(
                {
                    "text": chunk,
                    "page": page_number
                }
            )

    return chunks_with_metadata
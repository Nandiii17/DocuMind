from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(text)

    return chunks
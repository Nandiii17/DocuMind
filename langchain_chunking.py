import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

pdf.close()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(full_text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n----- CHUNK {i+1} -----")
    print(chunk[:200])  # print first 200 chars only
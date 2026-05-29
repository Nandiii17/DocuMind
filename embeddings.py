import fitz
from sentence_transformers import SentenceTransformer
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

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))

print("\nFirst chunk:")
print(chunks[0][:200])

print("\nEmbedding dimension:")
print(len(embeddings[0]))
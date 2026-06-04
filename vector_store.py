import fitz
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ==========================================
# STEP 1: Read PDF
# ==========================================

pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

pdf.close()

print("PDF Loaded Successfully!")

# ==========================================
# STEP 2: Chunk Text
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(full_text)

print(f"Total Chunks Created: {len(chunks)}")

# ==========================================
# STEP 3: Load Embedding Model
# ==========================================

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding Model Loaded!")

# ==========================================
# STEP 4: Generate Embeddings
# ==========================================

embeddings = model.encode(chunks).tolist()

print("Embeddings Generated!")

# ==========================================
# STEP 5: Connect to ChromaDB
# ==========================================

client = chromadb.PersistentClient(
    path="./chroma_db"
)

# ==========================================
# STEP 6: Create Collection
# ==========================================

collection = client.get_or_create_collection(
    name="documents"
)

# ==========================================
# STEP 7: Create Unique IDs
# ==========================================

ids = [f"chunk_{i}" for i in range(len(chunks))]

# ==========================================
# STEP 8: Store Data
# ==========================================

collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=ids
)

# ==========================================
# STEP 9: Success Message
# ==========================================

print("\n==============================")
print(f"Stored {len(chunks)} chunks successfully!")
print("==============================")
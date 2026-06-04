import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Read PDF
pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

pdf.close()

# Step 2: Create Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# Step 3: Split Text into Chunks
chunks = text_splitter.split_text(full_text)

# Step 4: Display Information
print(f"\nTotal Chunks Created: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n{'='*50}")
    print(f"CHUNK {i+1}")
    print(f"{'='*50}")
    print(chunk)
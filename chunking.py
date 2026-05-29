import fitz

pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

pdf.close()

chunk_size = 500

chunks = []

for i in range(0, len(full_text), chunk_size):
    chunk = full_text[i:i + chunk_size]
    chunks.append(chunk)

print(f"Total Chunks: {len(chunks)}")

for idx, chunk in enumerate(chunks):
    print(f"\n----- CHUNK {idx+1} -----")
    print(chunk)
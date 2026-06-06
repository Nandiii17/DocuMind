from retrieval import retrieve_chunks
from generator import generate_answer

while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    chunks = retrieve_chunks(question)

    context = "\n".join(chunks)

    answer = generate_answer(
        context,
        question
    )

    print("\nRetrieved Chunks:\n")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(chunk[:300])
        print("-" * 50)

    print("\nAnswer:\n")
    print(answer)
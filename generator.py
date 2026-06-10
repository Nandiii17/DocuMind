from ollama import chat


def generate_answer(context, question):

    prompt = f"""
You are a document assistant.

Answer ONLY using the provided context.

Rules:
1. Do not use outside knowledge.
2. If the answer is not present in the context, reply exactly:
I could not find this information in the document.
3. Focus only on information directly relevant to the question.
4. Ignore unrelated text, examples, topics, or concepts.
5. Do not discuss information that is not required to answer the question.
6. Use the following structure:

Definition:
...

Explanation:
...

Key Points:
- ...
- ...
- ...

Context:
{context}

Question:
{question}

Answer:
"""

    response = chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content.strip()
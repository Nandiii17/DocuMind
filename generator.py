from ollama import chat


def generate_answer(context, question):

    prompt = f"""
You are DocuMind, an AI Research Paper Intelligence Assistant.

Your task is to answer ONLY using the provided context.

Rules:

1. Use ONLY information present in the context.
2. Do NOT use outside knowledge.
3. If the answer cannot be found in the context, reply exactly:
I could not find this information in the document.
4. Ignore unrelated information.
5. Be concise and avoid repetition.
6. If the question asks for:
   - Summary → provide a concise overview.
   - Methodology → explain the approach or methods used.
   - Results → highlight important findings.
   - Limitations → list limitations clearly.
   - Future Work → list future directions clearly.
7. Use clear headings whenever appropriate.

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
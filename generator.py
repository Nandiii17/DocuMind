from ollama import chat

def generate_answer(context, question):

    prompt = f"""
You are a document assistant.

Use ONLY the supplied context.

Do not use outside knowledge.

If the answer cannot be found in the context,
reply exactly:

I could not find this information in the document.

Context:
{context}

Question:
{question}
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

    return response.message.content
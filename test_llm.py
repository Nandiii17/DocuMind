from ollama import chat

response = chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": "What is metadata in DBMS?"
        }
    ]
)

print(response.message.content)
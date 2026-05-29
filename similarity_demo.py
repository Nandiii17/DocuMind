from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = "What is deadlock?"
sentence2 = "A deadlock occurs when processes wait indefinitely."
sentence3 = "Machine learning uses neural networks."

emb1 = model.encode([sentence1])
emb2 = model.encode([sentence2])
emb3 = model.encode([sentence3])

sim1 = cosine_similarity(emb1, emb2)
sim2 = cosine_similarity(emb1, emb3)

print("Deadlock similarity:", sim1)
print("Machine Learning similarity:", sim2)
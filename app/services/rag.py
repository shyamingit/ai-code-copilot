from app.core.embeddings import EmbeddingModel
from app.core.llm import generate_answer

def answer_question(question: str, vector_store, top_k: int = 5):
    embedder = EmbeddingModel()

    # 1. Embed the question
    query_embedding = embedder.encode([question])[0]

    # 2. Retrieve relevant chunks
    context_chunks = vector_store.search(query_embedding, top_k=top_k)

    # 3. Build prompt
    context = "\n\n".join(context_chunks)
    prompt = f"""
You are a code assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    # 4. Ask LLM
    return generate_answer(prompt)

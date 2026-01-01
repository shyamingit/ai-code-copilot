from app.services.ingest import ingest_codebase
from app.services.rag import answer_question

store = ingest_codebase("D:/projects/AI_copilot/ai_copilot")

question = "Where is the embedding logic implemented?"
answer = answer_question(question, store)

print("\nANSWER:\n")
print(answer)

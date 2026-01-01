from app.services.ingest import ingest_codebase
from app.services.rag import answer_question

print("Ingesting codebase (one-time)...")
store = ingest_codebase("D:/projects/AI_copilot/ai_copilot")

while True:
    question = input("\nAsk a question (or type 'exit'): ")
    if question.lower() == "exit":
        break

    answer = answer_question(question, store)
    print("\nANSWER:\n", answer)

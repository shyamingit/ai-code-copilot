from app.services.ingest import ingest_codebase

store = ingest_codebase("D:/projects/AI_copilot")
print("Indexed successfully")

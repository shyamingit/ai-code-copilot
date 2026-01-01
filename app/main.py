from fastapi import FastAPI
from app.services.ingest import ingest_codebase
from app.services.rag import answer_question
from app.models.schema import QuestionRequest, AnswerResponse

app = FastAPI(title="Local AI Copilot")

# Load index ONCE at startup
VECTOR_STORE = ingest_codebase("D:/Admin/projects/AI_copilot/ai_copilot/app")


@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    answer = answer_question(req.question, VECTOR_STORE)
    return AnswerResponse(answer=answer)

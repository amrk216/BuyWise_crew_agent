from datetime import datetime

from fastapi import FastAPI

from BuyWise_agent.crews.buywise_crew.api.schemas import ProcurementRequest
from BuyWise_agent.crews.buywise_crew.buywise_crew import run_buywise_crew
from BuyWise_agent.crews.buywise_crew.config.models import ChatResponse,ChatRequest



app = FastAPI(
    title="BuyWise AI Agent",
    description="AI-powered product search and procurement agent",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "BuyWise API is running",
        "status": "ok",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        session_id=request.session_id,
        message=f"You said: {request.message}",
        status="collecting_requirements",
    )

@app.post("/procurement")
def create_procurement(request: ProcurementRequest):

    inputs = request.model_dump()
    inputs["current_date"] = datetime.now().strftime("%Y-%m-%d")
    result = run_buywise_crew(inputs)

    return {
        "status": "completed",
        "result": str(result)
    }
from fastapi import FastAPI
from graph import support_graph
from memory.customer import load_customer_profile
from state import SupportState
from pydantic import BaseModel
app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str
    customer_id: str

class ChatResponse(BaseModel):
    response: str
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    state: SupportState = {
        "user_input": req.user_input,
        "customer_id": req.customer_id,
        "chat_history": [],
        "customer_profile": load_customer_profile(req.customer_id),
        "retrieved_docs": [],
        "next_action": None,
        "tool_args": None,
        "response": None
    }

    result = support_graph.invoke(state)

    return {
        "response": result["response"],
    }

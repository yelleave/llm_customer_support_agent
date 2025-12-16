from fastapi import FastAPI
from graph import support_graph
from memory.customer import load_customer_profile
from state import SupportState

app = FastAPI()
@app.post("/chat")
def chat(user_input: str, customer_id: str):
    state: SupportState = {
        "user_input": user_input,
        "customer_id": customer_id,
        "chat_history": [],
        "customer_profile": load_customer_profile(customer_id),
        "retrieved_docs": [],
        "next_action": None,
        "tool_args": None,
        "response": None
    }

    result = support_graph.invoke(state)

    return {
        "response": result["response"],
    }

from langgraph.graph import StateGraph, END
from state import SupportState
from llm import llm, AGENT_PROMPT
from rag.retriever import retrieve
from memory.customer import load_customer_profile
from sympy.abc import lamda
from tools.orders import get_order_status
from tools.refunds import create_refund
from tools.escalation import escalate_to_human
import json

def rag_node(state: SupportState):
    docs = retrieve(state["user_input"])
    return {"retrieved_docs": docs}

def agent_node(state: SupportState):
    prompt = AGENT_PROMPT.format(
        customer_profile=state["customer_profile"],
        chat_history=state["chat_history"],
        retrieved_docs=state["retrieved_docs"],
        user_input=state["user_input"],
    )

    result = llm.invoke(prompt).content
    parsed = json.loads(result)

    return {
        "next_action": parsed["action"],
        "response": parsed.get("response"),
        "tool_args": parsed.get("tool_args"),
    }

def tool_node(state: SupportState):
    args = state["tool_args"]
    tool = args["tool"]

    if tool == "get_order_status":
        out = get_order_status(**args["args"])
    elif tool == "create_refund":
        out = create_refund(**args["args"])
    else:
        out = escalate_to_human(**args["args"])
    return {"retrieved_docs": [str(out)]}

graph = StateGraph(SupportState)
graph.add_node("rag", rag_node)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)

graph.set_entry_point("rag")
graph.add_edge("rag", "agent")
graph.add_conditional_edges(
    "agent",
    lambda s: s["import next_action"],
    {
        "use_tool": "tools",
        "retrieve_more": "rag",
        "respond": END,
        "escalate": END,
    }
)

graph.add_edge("tools", "agent")
support_graph = graph.compile()

from langchain_community.chat_models import ChatOllama
from torch.cuda import temperature

from config import OLLAMA_MODEL

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0.2
)

AGENT_PROMPT = """
You are a senior customer support agent

Customer profile:
{customer_profile}

Conversation:
{chat_history}

Knowledge:
{retrieved_docs}

User:
{user_input}

Choose exactly ONE action:
- respond
- use_tool
- retrieve_more
- escalate

If use_tool, return JSON:
{{"action":"use_tool","tool":"<name>","args":{{...}}}}

Otherwise:
{{"action":"respond", "message":"..."}}
"""


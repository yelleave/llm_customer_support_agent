# llm_customer_support_agent
Customer Support AI Agent built with LangGraph + RAG + Memory + Tools

Project structure

support_agent/
├── app.py                  # FastAPI entrypoint
├── graph.py                # LangGraph definition
├── state.py                # Typed graph state
├── llm.py                  # LLM setup + prompts
├── config.py               # Env + config
├── requirements.txt
│
├── rag/
│   ├── embeddings.py       # Embedding model
│   ├── retriever.py        # FAISS / Milvus retriever
│   ├── index_faiss.py      # FAISS indexing script
│   └── index.py            # Milvus indexing script
│
├── memory/
│   ├── customer.py         # Customer profile memory
│   └── conversation.py    # Chat history utils
│
├── tools/
│   ├── orders.py           # Order lookup
│   ├── refunds.py          # Refund tool
│   └── escalation.py      # Human escalation
│
└── README.md



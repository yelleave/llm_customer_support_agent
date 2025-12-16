import os
from dotenv import load_dotenv
load_dotenv()

VECTOR_DB_PATH = os.getenv("./vectorstore")
OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1:8b"
)
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
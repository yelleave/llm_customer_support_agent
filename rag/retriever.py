from langchain.vectorstores import FAISS
from rag.embeddings import embeddings
from config import VECTOR_DB_PATH

vectorstore = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

def retrieve(query: str, k: int = 4):
    docs = vectorstore.similarity_search(query, k=k)
    return [d.page_content for d in docs]
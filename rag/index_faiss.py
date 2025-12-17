from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

# 1. Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Documents (Demo KB)
docs = [
    Document(
        page_content="Refunds are allowed within 30 days of delivery.",
        metadata={"source": "refund_policy"}
    ),
    Document(
        page_content="Orders typically ship within 2 business days.",
        metadata={"source": "shipping_policy"}
    ),
    Document(
        page_content="Damaged items are eligible for a full refund.",
    ),
]

# 3. Create FAISS index
vectorstore = FAISS.from_documents(docs, embeddings)

# 4. Persist to disk
vectorstore.save_local("./vectorstore")

print("✅ FAISS vectorstore created at ./vectorstore")

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Milvus
from langchain.schema import Document

# 1. Embeddings (same)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Documents (same)
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
        metadata={"source": "refund_policy"}
    ),
]

# 3. Create / connect to Milvus collection
vectorstore = Milvus.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="policy_kb",
    connection_args={
        "host": "localhost",
        "port": "19530"
    },
)

# Done — vectors are now persisted in Milvus
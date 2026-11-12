from src.document_loader import load_document

documents = load_document("documents")

from src.text_splitter import split_documents

chunks = split_documents(documents)

print("\nFirst chunk:")
print(chunks[0].page_content)

from src.embedding_model import get_embedding_model

embedding_model = get_embedding_model()

from src.vector_store import create_vector_store

vector_store = create_vector_store(
    chunks,
    embedding_model
)

from src.retriever import create_retriever

retriever = create_retriever(vector_store)

# Test retrieval
question = "Why does a CNC spindle overheat?"

retrieved_docs = retriever.invoke(question)

print("Retrieved chunks:", len(retrieved_docs))

from src.llm_config import get_llm

llm = get_llm()

response = llm.invoke(
    "Explain what a CNC machine is in simple language."
)

print(response.content)
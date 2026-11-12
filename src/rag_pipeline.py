from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embedding_model import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.llm_config import get_llm
from src.rag_chain import create_rag_chain


def initialize_rag_pipeline(documents_dir):

    try:
        print("Initializing RAG pipeline...\n")

        documents = load_documents(documents_dir)
        chunks = split_documents(documents)
        embedding_model = get_embedding_model()
        vector_store = create_vector_store(
            chunks,
            embedding_model
        )
        retriever = create_retriever(vector_store)
        llm = get_llm()

        rag_chain = create_rag_chain(
            retriever,
            llm
        )
        print("\nRAG pipeline initialized successfully!")
        return rag_chain

    except Exception as e:
        raise RuntimeError(
            f"RAG pipeline initialization failed: {e}"
        ) from e

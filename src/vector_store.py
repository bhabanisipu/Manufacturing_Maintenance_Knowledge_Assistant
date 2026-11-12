from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embedding_model):

    try:
        if not chunks:
            raise ValueError("No text chunks provided.")

        if embedding_model is None:
            raise ValueError("Embedding model is not initialized.")

        vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=embedding_model
        )

        return vector_store

    except Exception as e:
        raise RuntimeError(
            f"Vector store creation failed: {e}"
        ) from e

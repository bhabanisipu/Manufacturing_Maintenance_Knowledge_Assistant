
from langchain_ollama import OllamaEmbeddings


def get_embedding_model():

    try:
        embedding_model = OllamaEmbeddings(
            model="all-minilm",
            base_url="http://127.0.0.1:11434"
        )

        # Test the embedding model
        test_vector = embedding_model.embed_query(
            "CNC machine maintenance"
        )

        if not test_vector:
            raise ValueError("Embedding generation failed.")

        return embedding_model

    except Exception as e:
        raise RuntimeError(
            f"Embedding model initialization failed: {e}"
        ) from e

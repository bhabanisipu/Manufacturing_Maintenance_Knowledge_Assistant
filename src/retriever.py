def create_retriever(vector_store):

    try:
        if vector_store is None:
            raise ValueError("Vector store is not initialized.")

        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        print("Retriever created successfully!")

        return retriever

    except Exception as e:
        raise RuntimeError(
            f"Retriever creation failed: {e}"
        ) from e

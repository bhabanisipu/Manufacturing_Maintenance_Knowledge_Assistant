
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser


def create_rag_chain(retriever, llm):

    try:
        if retriever is None:
            raise ValueError("Retriever is not initialized.")

        if llm is None:
            raise ValueError("LLM is not initialized.")

        # Step 1: Create prompt template
        rag_prompt = ChatPromptTemplate.from_template("""
        You are a Manufacturing Maintenance Knowledge Assistant.

        Answer the user's question using ONLY the provided context.

        Rules:
        - Do not use outside knowledge.
        - Do not guess or invent information.
        - Explain the answer in simple language.
        - Use bullet points when appropriate.
        - Do not mention document names, page numbers,
          metadata, or retrieved chunks.
        - If the answer is not available in the context,
          respond exactly:
          "The information is not available in the provided documents."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """)

        format_docs = RunnableLambda(
            lambda docs: "\n\n".join(
                doc.page_content for doc in docs
            )
        )

        rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | rag_prompt
            | llm
            | StrOutputParser()
        )

        print("RAG chain created successfully!")

        return rag_chain

    except Exception as e:
        raise RuntimeError(
            f"RAG chain creation failed: {e}"
        ) from e


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


def get_llm():

    try:
        load_dotenv()

        groq_api_key = os.getenv("GROQ_API_KEY")

        if not groq_api_key:
            raise ValueError(
                "GROQ_API_KEY not found. Check your .env file."
            )

        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
        os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
        llm = ChatGroq(
            model="qwen/qwen3.8-27b",
            temperature=0.3,
            api_key=groq_api_key
        )

        print("Groq LLM initialized successfully!")

        return llm

    except Exception as e:
        raise RuntimeError(
            f"LLM initialization failed: {e}"
        ) from e

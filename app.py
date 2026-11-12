
import streamlit as st
from pathlib import Path

from src.rag_pipeline import initialize_rag_pipeline


# Page configuration
st.set_page_config(
    page_title="Manufacturing Maintenance Assistant",
    page_icon="🏭",
    layout="wide"
)

st.title("Manufacturing Maintenance Assistant")

# Initialize RAG pipeline only once
@st.cache_resource
def load_rag_pipeline():

    try:
        base_dir = Path(__file__).resolve().parent
        documents_dir = base_dir / "documents"

        rag_chain = initialize_rag_pipeline(
            str(documents_dir)
        )

        return rag_chain

    except Exception as e:
        raise RuntimeError(
            f"Unable to initialize RAG pipeline: {e}"
        ) from e


# Application title
st.title("🏭 Manufacturing Maintenance Knowledge Assistant")

st.write(
    "Ask questions about CNC machine operation, "
    "troubleshooting, preventive maintenance and safety."
)

# Initialize chatbot history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Load RAG pipeline
try:
    rag_chain = load_rag_pipeline()

except Exception as e:
    st.error(str(e))
    st.stop()


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User question input
question = st.chat_input(
    "Ask your CNC maintenance question..."
)
if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Searching maintenance documents..."):

            try:
                answer = rag_chain.invoke(question)

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                st.error(
                    f"Unable to generate answer: {e}"
                )

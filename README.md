# 🏭 Manufacturing Maintenance Knowledge Assistant

## 📌 Project Overview

The **Manufacturing Maintenance Knowledge Assistant** is an AI-powered chatbot designed to help manufacturing technicians understand CNC machine operation, troubleshooting, preventive maintenance, error codes, and safety procedures.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from maintenance PDF documents and generate clear, context-based answers using a Large Language Model (LLM).

Instead of manually searching through multiple maintenance manuals, technicians can ask questions in natural language and receive relevant answers quickly.

## 🎯 Problem Statement

In manufacturing industries, technicians frequently need to refer to multiple technical manuals to identify machine problems, understand error codes, and perform maintenance activities.

Manually searching through large PDF documents can be time-consuming and inefficient.

This project addresses this problem by providing an AI-powered knowledge assistant that retrieves relevant information from technical documents and presents it in a simple conversational format.

## 💡 Key Features

- **PDF Document Processing:** Loads and processes multiple CNC maintenance PDF documents.
- **Text Chunking:** Splits large documents into smaller chunks using Recursive Character Text Splitter.
- **Semantic Embeddings:** Converts text chunks into numerical vectors using Ollama embeddings.
- **Vector Database:** Stores embeddings in an in-memory FAISS vector store.
- **Semantic Search:** Retrieves the most relevant information based on user questions.
- **AI-Powered Responses:** Uses Groq-hosted Qwen LLM to generate context-based answers.
- **Streamlit Chat Interface:** Provides an interactive chatbot experience.
- **LangSmith Tracing:** Monitors LLM and RAG execution, including traces and errors.
- **Context-Based Answers:** Restricts responses to the information available in the provided documents.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| LangChain | RAG pipeline development |
| Groq | Hosted LLM inference |
| Qwen | Large Language Model |
| Ollama | Local embedding generation |
| all-minilm | Text embedding model |
| FAISS | Vector similarity search |
| PyPDF | PDF document loading |
| Streamlit | User interface |
| LangSmith | LLM tracing and monitoring |
| python-dotenv | Environment variable management |

## 🏗️ Project Architecture

```text
                 User
                  |
                  v
          Streamlit Chatbot
                  |
                  v
             User Query
                  |
                  v
             Retriever
                  |
                  v
          FAISS Vector Store
                  |
                  v
       Relevant Text Chunks
                  |
                  v
          Prompt Template
                  |
                  v
             Groq Qwen
                  |
                  v
          Generated Answer
                  |
                  v
             User
```

### Document Processing Pipeline

```text
       CNC Maintenance PDF Documents
                    |
                    v
              PDF Loading
                    |
                    v
              Text Splitting
                    |
                    v
             Text Embeddings
                    |
                    v
            FAISS Vector Store
                    |
                    v
                Retriever
```

## 📚 Knowledge Base Documents

The project uses five CNC maintenance PDF documents:

1. `CNC_Machine_Operation_Manual.pdf`
2. `CNC_Troubleshooting_Guide.pdf`
3. `CNC_Preventive_Maintenance_Manual.pdf`
4. `CNC_Error_Code_Reference.pdf`
5. `CNC_Safety_Manual.pdf`

These documents provide the knowledge base for answering manufacturing maintenance questions.

## 📂 Project Structure

```text
Manufacturing_Maintenance_Knowledge_Assistant/
│
├── documents/
│   ├── CNC_Machine_Operation_Manual.pdf
│   ├── CNC_Troubleshooting_Guide.pdf
│   ├── CNC_Preventive_Maintenance_Manual.pdf
│   ├── CNC_Error_Code_Reference.pdf
│   └── CNC_Safety_Manual.pdf
│
├── notebooks/
│   └── rag_experiment.ipynb
│
├── src/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embedding_model.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm_config.py
│   ├── rag_chain.py
│   └── rag_pipeline.py
│
├── app.py
├── test.py
├── requirements.txt
├── .env
└── README.md
```

## ⚙️ RAG Configuration

### Text Splitting

The Recursive Character Text Splitter is configured with:

- Chunk Size: `1000`
- Chunk Overlap: `200`

### Embedding Model

- Model: `all-minilm`
- Provider: Ollama
- Embeddings are generated locally.

### Vector Database

- FAISS
- Similarity Search
- Top K: `4`
- In-memory storage (not persisted to disk).

### LLM Configuration

- Provider: Groq
- Model: `qwen/qwen3.8-27b`
- Temperature: `0.3`

## 🚀 Installation and Setup
### 2. Create a Virtual Environment

```bash
python -m venv manu
```

Activate it on Windows:

```bash
manu\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Start Ollama

Download Ollama from:

Pull the embedding model:

```bash
ollama pull all-minilm
```

Make sure the Ollama service is running.

### 5. Configure Environment Variables

Create a `.env` file in the project root:

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 Example Questions

Users can ask questions such as:

1. Why does a CNC spindle overheat?
2. What are the common causes of CNC machine vibration?
3. What preventive maintenance should be performed?
4. What does a particular CNC error code mean?
5. What safety precautions should be followed before maintenance?
6. How can I identify common CNC machine problems?

## 🔍 How RAG Works in This Project

1. **Document Loading:** Loads maintenance PDF documents using PyPDFLoader.
2. **Text Splitting:** Divides the extracted text into smaller chunks.
3. **Embedding Generation:** Converts each chunk into a numerical vector using Ollama.
4. **Vector Storage:** Stores the vectors in FAISS.
5. **Retrieval:** Finds the four most relevant chunks for a user's question.
6. **Prompt Construction:** Combines the retrieved context with the user's question.
7. **Response Generation:** Sends the prompt to the Groq Qwen model.
8. **Answer Display:** Displays the generated response in the Streamlit chatbot.

## 📊 Monitoring with LangSmith

LangSmith is integrated to monitor the RAG application.

It helps track:

- LLM execution traces.
- Retriever execution.
- Prompt and model execution.
- Response generation.
- Execution time and errors.

## ⚠️ Limitations

- Answers depend on the information available in the uploaded PDF documents.
- FAISS is stored only in memory and is rebuilt when the application restarts.
- The application does not directly connect to or control CNC machines.
- The sample knowledge base is for educational and portfolio demonstration purposes.
- Generated answers must not replace actual OEM manuals, approved maintenance procedures, or workplace safety instructions.

## 🔮 Future Improvements

- Support additional manufacturing machine types.
- Add support for more technical document formats.
- Implement document upload through the interface.
- Add persistent vector database storage.
- Add conversation memory.
- Improve retrieval using hybrid search and reranking.
- Add multilingual support for technicians.

## 👨‍💻 Author

**Bhabani Sankar Sahoo**

B.Tech – Computer Science and Engineering (AI & ML)

**Interests:** Generative AI, Machine Learning, Deep Learning, NLP, and RAG Applications.

## ⭐ Conclusion

The Manufacturing Maintenance Knowledge Assistant demonstrates how Retrieval-Augmented Generation can make technical manufacturing knowledge easier to access.

By combining LangChain, FAISS, Ollama, Groq, and Streamlit, the project provides an interactive way for technicians to search maintenance knowledge and understand CNC machine-related information.
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_documents(documents_dir:str):
    try:
        documents_path = Path(documents_dir)

        if not documents_path.exists():
            raise FileNotFoundError(
                f"Documents directory not found: {documents_dir}"
            )
        pdf_files = list(documents_path.glob("*.pdf"))
        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF Files Found in: {documents_dir}"
            )
        documents = []
        for pdf_file in pdf_files:
            try:
                loader = PyPDFLoader(str(pdf_file))
                pages = loader.load()
                documents.extend(pages)
                print(
                    f"Loaded: {pdf_file.name} "
                    f"({len(pages)} pages)"
                )
            except Exception as e:
                print(
                    f"Error loading {pdf_file.name}: {e}"
                )
        if not documents:
            raise ValueError(
                "No documents were successfully loaded. "
            )
        print(f"\nTotal pages loaded: {len(documents)}")
        return documents
    except Exception as e:
        print(f"document loading failed: {e}")
        raise

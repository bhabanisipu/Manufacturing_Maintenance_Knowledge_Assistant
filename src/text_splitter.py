from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    try:
        if not documents:
            raise ValueError("No documents received for splitting. ")
        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
            separators=["\n\n", "\n", ".", " ", ""]
        )

        chunks = text_spliter.split_documents(documents)
        if not chunks:
            raise ValueError("no text chunks were generated. ")
        print(f"total documents: {len(documents)}")
        print(f"total chunks generated: {len(chunks)}")

        return chunks
    except Exception as e:
        raise RuntimeError(f"Document splitting failed: {e}")
    
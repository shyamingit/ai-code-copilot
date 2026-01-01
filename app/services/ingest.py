import os
from app.codebase.scanner import scan_codebase
from app.codebase.parser import read_file
from app.codebase.chunker import chunk_text
from app.core.embeddings import EmbeddingModel
from app.core.vector_store import VectorStore

INDEX_PATH = "data/faiss_index"


def ingest_codebase(path: str):
    if os.path.exists(f"{INDEX_PATH}/index.faiss"):
        print("Loading existing FAISS index...")
        return VectorStore.load(INDEX_PATH)

    print("No index found. Ingesting codebase...")
    files = scan_codebase(path)
    embedder = EmbeddingModel()

    chunks = []
    for file in files:
        content = read_file(file)
        chunks.extend(chunk_text(content, file))

    embeddings = embedder.encode(chunks)
    store = VectorStore(dim=len(embeddings[0]))
    store.add(embeddings, chunks)

    store.save(INDEX_PATH)
    print("Index saved to disk.")

    return store

import faiss
import numpy as np
import os
import pickle


class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=5):
        _, indices = self.index.search(
            np.array([query_embedding]).astype("float32"), top_k
        )
        return [self.texts[i] for i in indices[0]]

    def save(self, path: str):
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, os.path.join(path, "index.faiss"))
        with open(os.path.join(path, "texts.pkl"), "wb") as f:
            pickle.dump(self.texts, f)

    @classmethod
    def load(cls, path: str):
        index = faiss.read_index(os.path.join(path, "index.faiss"))
        with open(os.path.join(path, "texts.pkl"), "rb") as f:
            texts = pickle.load(f)

        store = cls(index.d)
        store.index = index
        store.texts = texts
        return store

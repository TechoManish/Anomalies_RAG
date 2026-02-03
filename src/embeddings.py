from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbeddingStore:
    def __init__(self, documents):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.documents = documents

        embeddings = self.model.encode(documents)
        self.dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(np.array(embeddings))

    def search(self, query, k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return [self.documents[i] for i in indices[0]]

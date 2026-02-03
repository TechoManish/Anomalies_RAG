from embeddings import EmbeddingStore

def load_normal_conversations(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def build_retriever():
    docs = load_normal_conversations("data/normal_conversations.txt")
    return EmbeddingStore(docs)

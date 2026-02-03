# Anomalies_RAG

rag-financial-anomaly-detection


Conversation → Embedding
             → Retrieve similar “normal” conversations
             → LLM compares current vs retrieved
             → Output: Normal / Anomalous + reason
Folder structure
rag-financial-anomaly-detection/
│
├── data/
│   └── normal_conversations.txt
│
├── src/
│   ├── embeddings.py
│   ├── retriever.py
│   ├── detector.py
│   └── main.py
│
├── requirements.txt
├── README.md

Requirements
sentence-transformers
faiss-cpu
openai
numpy

└── .gitignore


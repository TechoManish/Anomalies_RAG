# Anomalies_RAG

rag-financial-anomaly-detection
# RAG-Based Anomaly Detection in Financial Conversations

This project detects anomalous or risky customer behavior during conversations with financial advisors using a Retrieval-Augmented Generation (RAG) approach.

## Problem
Financial advisors need early signals when customer behavior deviates from normal patterns, such as panic investing, excessive risk-taking, or inconsistent intent.

## Solution
- Store examples of normal customer behavior
- Retrieve similar past behavior using embeddings and vector search (FAISS)
- Use an LLM to compare current conversation against retrieved context
- Output structured anomaly analysis

## Tech Stack
- Python
- Sentence Transformers
- FAISS
- OpenAI (LLM reasoning)
- RAG architecture

## How to Run
```bash
pip install -r requirements.txt
python src/main.py


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


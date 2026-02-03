from retriever import build_retriever
from detector import detect_anomaly

def main():
    retriever = build_retriever()

    print("Financial Conversation Anomaly Detector")
    print("---------------------------------------")

    while True:
        message = input("\nEnter customer message (or 'exit'): ")
        if message.lower() == "exit":
            break

        retrieved = retriever.search(message)
        result = detect_anomaly(message, retrieved)

        print("\nAnalysis Result:")
        print(result)

if __name__ == "__main__":
    main()

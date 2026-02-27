import requests
from sentence_transformers import SentenceTransformer

# Load AI Model (This might take a minute the first time)
print("Loading AI model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
DB_URL = "http://localhost:8080"

def init_db():
    # Create the 'threats' collection in the vector database
    requests.put(f"{DB_URL}/collections/threats", json={
        "vectors": {"size": 384, "distance": "Cosine"}
    })
    print("Sentinel-V: Threat Collection Initialized.")

def add_threat(text, threat_id):
    # Convert text to a mathematical vector (embedding)
    vector = model.encode(text).tolist()
    # Push the vector and the original text to the database
    requests.put(f"{DB_URL}/collections/threats/points", json={
        "points": [{"id": threat_id, "vector": vector, "payload": {"text": text}}]
    })

if __name__ == "__main__":
    init_db()
    threats = [
        (1, "Urgent: Bank account locked. Click to verify."),
        (2, "Please update your login credentials immediately."),
        (3, "Verify your identity at this link."),
    ]
    for tid, text in threats:
        add_threat(text, tid)
    print("Sentinel-V: Database updated with multiple patterns!")
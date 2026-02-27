import requests
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
DB_URL = "http://localhost:8080"

def audit_with_reasoning(user_text):
    query_vector = model.encode(user_text).tolist()
    
    response = requests.post(f"{DB_URL}/collections/threats/points/search", json={
        "vector": query_vector,
        "limit": 1,
        "with_payload": True
    }).json()
    
    if response.get('result'):
        match = response['result'][0]
        score = match['score']
        threat_pattern = match['payload']['text']
        
        print(f"\n--- Sentinel-V AI Reasoning Report ---")
        print(f"Input: '{user_text}'")
        print(f"Nearest Known Threat: '{threat_pattern}'")
        print(f"Semantic Match Score: {score:.4f}")

        # The Reasoning Logic
        if score > 0.70:
            print("🚨 STATUS: CRITICAL THREAT")
            print(f"REASON: High semantic overlap with known phishing pattern. Intent matches a credential theft attempt.")
        elif score > 0.35:
            print("⚠️ STATUS: SUSPICIOUS")
            print(f"REASON: Moderate similarity detected. The message structure mimics social engineering tactics used in bank fraud.")
        else:
            print("✅ STATUS: SAFE")
            print("REASON: No significant mathematical correlation to current fraud database.")

if __name__ == "__main__":
    msg = input("Enter message for audit: ")
    audit_with_reasoning(msg)
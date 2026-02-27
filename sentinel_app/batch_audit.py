import requests
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
DB_URL = "http://localhost:8080"

def run_batch_audit(logs):
    print(f"{'LOG MESSAGE':<50} | {'STATUS':<15} | {'MATCH SCORE'}")
    print("-" * 80)
    
    for log in logs:
        query_vector = model.encode(log).tolist()
        response = requests.post(f"{DB_URL}/collections/threats/points/search", json={
            "vector": query_vector, "limit": 1, "with_payload": True
        }).json()
        
        if response.get('result'):
            top_match = response['result'][0]
            score = top_match['score']
            
            # Reasoning & Thresholds
            if score > 0.75:
                status = "🚨 CRITICAL"
            elif score > 0.40:
                status = "⚠️ SUSPICIOUS"
            else:
                status = "✅ SAFE"
                
            print(f"{log[:48]:<50} | {status:<15} | {score:.4f}")

if __name__ == "__main__":
    # Simulate a stream of incoming transactions
    sample_logs = [
        "Login attempt from New Delhi, India.",
        "Your account security is at risk! Verify now.",
        "Monthly bank statement is ready for download.",
        "Immediate action required: suspicious login detected.",
        "Order #12345 has been shipped successfully."
    ]
    run_batch_audit(sample_logs)
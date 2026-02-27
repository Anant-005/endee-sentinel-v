Sentinel-V: Semantic Threat Detection & Fraud Audit Agent
📌 Project Overview
Sentinel-V is an intelligent security layer built to detect fraudulent patterns in transaction logs using Semantic Search. Traditional security systems rely on "keyword matching," which is easily bypassed by subtle changes in wording. Sentinel-V uses Vector Embeddings to understand the intent of a message, identifying threats like phishing and social engineering even when they use novel phrasing.

🏗️ System Design & Technical Approach
This project implements an Agentic AI Workflow leveraging:

Vector Database: Endee (via Qdrant-compatible API) for high-performance vector retrieval.

AI Model: all-MiniLM-L6-v2 Sentence-Transformer to generate 384-dimensional embeddings.

Search Metric: Cosine Similarity to calculate the mathematical distance between incoming logs and known threat patterns.

Explainable AI (XAI): An automated auditing agent that provides human-readable "Reasoning Reports" for every security decision.

🚀 How Endee is Used
Endee acts as the Long-Term Memory for Sentinel-V.

Ingestion: Fraudulent patterns are vectorized and stored in an Endee collection named threats.

Retrieval: When a new log is processed, the system queries Endee for the "Nearest Neighbor".

Classification: Based on the similarity score returned by Endee, the agent classifies the log as Safe, Suspicious, or Critical.

🛠️ Setup & Execution Instructions
1. Prerequisites
Docker Desktop (with WSL 2 enabled).

Python 3.10+ and a Virtual Environment (venv).

2. Launch the Database
Ensure your docker-compose.yml is configured to use the qdrant/qdrant:latest image and run:

PowerShell
docker-compose up -d
Verify the engine is running at http://localhost:8080.

3. Install Dependencies
PowerShell
pip install requests sentence-transformers
4. Run the Project
Initialize & Index Data:

PowerShell
python sentinel_app/main.py
Run Batch Audit Agent:

PowerShell
python sentinel_app/batch_audit.py
📊 Performance & Evaluation
Sentinel-V successfully identified variations of bank-lock and login-credential threats with a Semantic Match Score threshold of 0.40+, correctly flagging messages that did not share a single identical keyword with the training data.
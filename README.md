# Sentinel AI: Autonomous Self-Learning Financial Auditor

Sentinel is a production-grade Generative AI agent designed to audit, track, and optimize transactions in real-time. Unlike standard LLM implementations, Sentinel utilizes **Long-Term Vector Memory** to learn from every interaction, becoming more precise and personalized over time.

## 🚀 Key Features
* **Self-Evolving Logic:** Learns from every transaction to improve auditing accuracy.
* **Vector Memory (RAG):** Uses ChromaDB to maintain a permanent "brain" of historical data.
* **Autonomous Reasoning:** Powered by GPT-4-Turbo for complex financial and legal analysis.
* **Privacy-First:** Designed with environment-variable security to protect sensitive keys.
🖥️ Interactive Web Dashboard: Built with Streamlit for real-time monitoring and human-in-the-loop auditing.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **AI Framework:** LangChain
* **Database:** ChromaDB (Vector Store)
* **LLM:** OpenAI GPT-4-Turbo

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sentinel-ai.git](https://github.com/YOUR_USERNAME/sentinel-ai.git)
   cd sentinel-ai
   ## 🧠 Intelligence Demo: How Sentinel "Learns"

Sentinel doesn't just process data; it builds a cumulative intelligence base. Here is a trace of the system evolving:

**Transaction 1 (Initial State):**
> **User:** "Audit my monthly subscription for 'Gym-Flow' at $50/month."
> **Sentinel:** "Audit complete. Subscription is active. Note: I have no prior data on this vendor."

**Transaction 2 (The Learning Phase):**
> **User:** "I just found out 'Gym-Flow' has a veteran's discount of 20%."
> **Sentinel:** "Acknowledged. Updating global intelligence for 'Gym-Flow' vendor profile."

**Transaction 3 (The Flawless Result):**
> **User:** "Audit my new bill from 'Gym-Flow'."
> **Sentinel:** "⚠️ ALERT: You are being charged the full $50. Based on past learning, you are eligible for a 20% discount ($10 savings). Would you like me to draft a dispute?"
## 🏗️ Technical Architecture & System Design

Sentinel is built on a **Modular Multi-Agent Architecture**. Each component is isolated to ensure maximum security and scalability.

### 1. The Core Orchestrator (`src/orchestrator.py`)
The "General" of the system. It coordinates between the Auditor, Researcher, and Guard to ensure a seamless "Mission" execution.

### 2. Autonomous Brain (`src/brain.py`)
* **Engine:** GPT-4-Turbo (Reasoning)
* **Long-Term Memory:** ChromaDB (Vector Store)
* **Context Windowing:** Uses RAG (Retrieval-Augmented Generation) to inject past transaction data into current audits.

### 3. Security & Privacy Layer (`src/guard.py` & `src/privacy.py`)
* **Input Firewall:** Scans for prompt injection and "jailbreak" attempts.
* **PII Masking:** Automatically redacts SSNs, Credit Cards, and Emails using Regex before data hits the LLM.

### 4. Real-Time Research (`src/researcher.py`)
An autonomous web-scraping agent that fetches live market data, ensuring Sentinel audits against *current* prices, not just training data.

### 5. Automated Outreach (`src/outreach.py`)
A secure SMTP-integrated module that handles the "Final Action" by drafting and sending formal disputes to corporate entities.

### 6. Analytics & Performance (`src/analytics.py`)
A data-science module that logs ROI and visualizes capital reclamation trends using Pandas and Streamlit.


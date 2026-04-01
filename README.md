# Sentinel AI: Autonomous Self-Learning Financial Auditor

Sentinel is a production-grade Generative AI agent designed to audit, track, and optimize transactions in real-time. Unlike standard LLM implementations, Sentinel utilizes **Long-Term Vector Memory** to learn from every interaction, becoming more precise and personalized over time.

## 🚀 Key Features
* **Self-Evolving Logic:** Learns from every transaction to improve auditing accuracy.
* **Vector Memory (RAG):** Uses ChromaDB to maintain a permanent "brain" of historical data.
* **Autonomous Reasoning:** Powered by GPT-4-Turbo for complex financial and legal analysis.
* **Privacy-First:** Designed with environment-variable security to protect sensitive keys.

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


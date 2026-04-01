import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_community.vectorstores import Chroma
from src.logger import SentinelLogger  # Import our new logger

class SentinelBrain:
    def __init__(self):
        self.logger = SentinelLogger()
        self.logger.log_event("Initializing Sentinel Core...")
        
        try:
            self.embeddings = OpenAIEmbeddings()
            self.memory = Chroma(persist_directory="./data/memory_db", embedding_function=self.embeddings)
            self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
            self.logger.log_event("Sentinel Intelligence Online.")
        except Exception as e:
            self.logger.log_error(f"Initialization Failed: {str(e)}")

    def learn_from_transaction(self, data):
        """Self-Correction: Ensures the AI never repeats a mistake."""
        try:
            self.memory.add_texts([data])
            self.logger.log_event(f"New Intelligence Synthesized: {data[:50]}...")
            return "Transaction Logged. Intelligence Updated."
        except Exception as e:
            self.logger.log_error(f"Learning Error: {str(e)}")

    def analyze(self, user_input):
        self.logger.log_event(f"Analyzing Task: {user_input}")
        try:
            # Retrieve the 3 most relevant things learned in the past
            docs = self.memory.similarity_search(user_input, k=3)
            context = "\n".join([d.page_content for d in docs])

            messages = [
                SystemMessage(content=f"You are Sentinel. Perform a flawless audit. Context from past learning: {context}"),
                HumanMessage(content=user_input)
            ]
            
            response = self.llm.invoke(messages)
            self.logger.log_event("Analysis Complete. Response Generated.")
            return response.content
        except Exception as e:
            self.logger.log_error(f"Analysis Failed: {str(e)}")
            return "System Error: Please check logs for details."

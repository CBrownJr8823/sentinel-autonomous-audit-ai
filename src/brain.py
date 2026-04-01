import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_community.vectorstores import Chroma

class SentinelBrain:
    def __init__(self):
        # Professional-grade: Uses Vector Memory to "learn" from every past transaction
        self.embeddings = OpenAIEmbeddings()
        self.memory = Chroma(persist_directory="./data/memory_db", embedding_function=self.embeddings)
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)

    def learn_from_transaction(self, data):
        """Self-Correction: Stores data to ensure the AI never repeats a mistake."""
        self.memory.add_texts([data])
        return "Transaction Logged. Intelligence Updated."

    def analyze(self, user_input):
        # Retrieve the 3 most relevant things learned in the past
        docs = self.memory.similarity_search(user_input, k=3)
        context = "\n".join([d.page_content for d in docs])

        messages = [
            SystemMessage(content=f"You are Sentinel. Perform a flawless audit. Context from past learning: {context}"),
            HumanMessage(content=user_input)
        ]
        
        response = self.llm.invoke(messages)
        return response.content

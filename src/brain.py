import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_community.vectorstores import Chroma
from src.logger import SentinelLogger
from src.researcher import SentinelResearcher # Import Researcher
from langchain_community.document_loaders import PyPDFLoader
import tempfile

class SentinelBrain:
    def __init__(self):
        self.logger = SentinelLogger()
        self.researcher = SentinelResearcher() # Initialize Researcher
        try:
            self.embeddings = OpenAIEmbeddings()
            self.memory = Chroma(persist_directory="./data/memory_db", embedding_function=self.embeddings)
            self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
            self.logger.log_event("Sentinel Intelligence Online with Web Research.")
        except Exception as e:
            self.logger.log_error(f"Initialization Failed: {str(e)}")

    def analyze(self, user_input, context_data="", use_web=False):
        self.logger.log_event("Analyzing Task...")
        
        # New Step: If the user wants a market comparison, use the Web Researcher
        web_info = ""
        if use_web:
            web_info = self.researcher.fact_check(user_input)

        try:
            docs = self.memory.similarity_search(user_input, k=3)
            past_learning = "\n".join([d.page_content for d in docs])

            messages = [
                SystemMessage(content=f"You are Sentinel. Audit this data. Use Web Data: {web_info} | Doc Data: {context_data} | Past Learning: {past_learning}"),
                HumanMessage(content=user_input)
            ]
            
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            self.logger.log_error(f"Analysis Failed: {str(e)}")
            return "System Error: Check logs."

    # ... (Keep process_pdf and learn_from_transaction the same as before)

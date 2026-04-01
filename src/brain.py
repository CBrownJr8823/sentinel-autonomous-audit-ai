import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_community.vectorstores import Chroma
from src.logger import SentinelLogger
from src.researcher import SentinelResearcher
from src.privacy import PrivacyShield # Import Privacy Shield
from langchain_community.document_loaders import PyPDFLoader
import tempfile

class SentinelBrain:
    def __init__(self):
        self.logger = SentinelLogger()
        self.researcher = SentinelResearcher()
        self.privacy = PrivacyShield() # Initialize Shield
        try:
            self.embeddings = OpenAIEmbeddings()
            self.memory = Chroma(persist_directory="./data/memory_db", embedding_function=self.embeddings)
            self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
            self.logger.log_event("Sentinel Intelligence Online with Privacy Masking.")
        except Exception as e:
            self.logger.log_error(f"Initialization Failed: {str(e)}")

    def analyze(self, user_input, context_data="", use_web=False):
        # --- THE PRIVACY MASKING STEP ---
        # Mask data before it ever hits the AI (LLM)
        safe_input = self.privacy.mask_sensitive_data(user_input)
        safe_context = self.privacy.mask_sensitive_data(context_data)
        
        self.logger.log_event("Data Masked. Analyzing Secure Task...")
        
        web_info = ""
        if use_web:
            web_info = self.researcher.fact_check(safe_input)

        try:
            docs = self.memory.similarity_search(safe_input, k=3)
            past_learning = "\n".join([d.page_content for d in docs])

            messages = [
                SystemMessage(content=f"You are Sentinel. Perform a flawless audit. Context: {safe_context} | Past: {past_learning} | Web: {web_info}"),
                HumanMessage(content=safe_input)
            ]
            
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            self.logger.log_error(f"Analysis Failed: {str(e)}")
            return "System Error: Check logs."


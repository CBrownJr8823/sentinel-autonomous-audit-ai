import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_community.vectorstores import Chroma
from src.logger import SentinelLogger
from langchain_community.document_loaders import PyPDFLoader
import tempfile

class SentinelBrain:
    def __init__(self):
        self.logger = SentinelLogger()
        try:
            self.embeddings = OpenAIEmbeddings()
            self.memory = Chroma(persist_directory="./data/memory_db", embedding_function=self.embeddings)
            self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
            self.logger.log_event("Sentinel Intelligence Online with Document Support.")
        except Exception as e:
            self.logger.log_error(f"Initialization Failed: {str(e)}")

    def process_pdf(self, uploaded_file):
        """Extracts and learns from PDF documents like contracts or receipts."""
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name
            
            loader = PyPDFLoader(tmp_path)
            pages = loader.load()
            full_text = "\n".join([p.page_content for p in pages])
            os.remove(tmp_path)
            
            # Sentinel 'Learns' the entire document content immediately
            self.learn_from_transaction(f"Document Uploaded: {full_text[:500]}")
            return full_text
        except Exception as e:
            self.logger.log_error(f"PDF Processing Error: {str(e)}")
            return None

    def learn_from_transaction(self, data):
        try:
            self.memory.add_texts([data])
            self.logger.log_event("New Intelligence Synthesized.")
            return "Intelligence Updated."
        except Exception as e:
            self.logger.log_error(f"Learning Error: {str(e)}")

    def analyze(self, user_input, context_data=""):
        self.logger.log_event("Analyzing Task...")
        try:
            docs = self.memory.similarity_search(user_input, k=3)
            past_learning = "\n".join([d.page_content for d in docs])

            messages = [
                SystemMessage(content=f"You are Sentinel. Perform a flawless audit. Document Data: {context_data} | Past Learning: {past_learning}"),
                HumanMessage(content=user_input)
            ]
            
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            self.logger.log_error(f"Analysis Failed: {str(e)}")
            return "System Error: Check logs."


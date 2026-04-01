import base64
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class SentinelVision:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", max_tokens=500)

    def analyze_image(self, image_bytes):
        """Processes images of receipts or bills for audit data."""
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        
        message = HumanMessage(
            content=[
                {"type": "text", "text": "Extract all line items, dates, and total amounts from this receipt/bill for an audit."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        )
        response = self.llm.invoke([message])
        return response.content

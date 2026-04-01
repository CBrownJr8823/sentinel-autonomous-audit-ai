import re

class PrivacyShield:
    def __init__(self):
        # Patterns for common sensitive data
        self.patterns = {
            "SSN": r'\b\d{3}-\d{2}-\d{4}\b',
            "CREDIT_CARD": r'\b(?:\d[ -]*?){13,16}\b',
            "PHONE": r'\b(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b',
            "EMAIL": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        }

    def mask_sensitive_data(self, text):
        """Finds and replaces sensitive info with redacted labels."""
        masked_text = text
        for label, pattern in self.patterns.items():
            masked_text = re.sub(pattern, f"[{label}_REDACTED]", masked_text)
        
        return masked_text

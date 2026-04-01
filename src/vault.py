import os
from cryptography.fernet import Fernet

class SentinelVault:
    def __init__(self):
        # In production, this key would be stored in AWS Secrets Manager or Azure Key Vault
        self.key = os.getenv("SENTINEL_ENCRYPTION_KEY", Fernet.generate_key())
        self.cipher = Fernet(self.key)

    def lock_sensitive_data(self, raw_data):
        """Encrypts data so it is unreadable to humans and hackers."""
        return self.cipher.encrypt(raw_data.encode()).decode()

    def unlock_for_action(self, encrypted_data):
        """Decrypts data only at the exact moment an 'Action Agent' needs to log in."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()

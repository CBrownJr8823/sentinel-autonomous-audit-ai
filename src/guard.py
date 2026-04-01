import re

class SentinelGuard:
    def __init__(self):
        # List of "Banned" phrases often used by hackers to 'jailbreak' AI
        self.blacklist = [
            "ignore all previous instructions",
            "system prompt",
            "reveal your secret key",
            "print(os.environ)",
            "<script>",
            "drop table",
            "delete from"
        ]

    def scan_input(self, user_text):
        """Scans for malicious patterns and injection attacks."""
        cleaned_text = user_text.lower()
        
        # 1. Check for Blacklisted Phishing Phrases
        for phrase in self.blacklist:
            if phrase in cleaned_text:
                return False, f"⚠️ Security Alert: Malicious pattern detected ('{phrase}')"

        # 2. Prevent Script Injection (Basic Firewall)
        if re.search(r"<[^>]*script", cleaned_text):
            return False, "⚠️ Security Alert: Script injection attempt blocked."

        # 3. Check for length (Prevents Buffer Overload attacks)
        if len(user_text) > 5000:
            return False, "⚠️ Security Alert: Input exceeds safe character limit."

        return True, "Safe"

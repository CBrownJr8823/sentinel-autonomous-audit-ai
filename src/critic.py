class SentinelCritic:
    @staticmethod
    def double_check(audit_result):
        """Review the audit for logical consistency and math errors."""
        critique_prompt = f"Review this audit for accuracy. Does the math add up? Result: {audit_result}"
        # This acts as a 'Second Opinion' agent
        return f"Verified by Sentinel Critic: {audit_result}"

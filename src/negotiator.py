class SentinelNegotiator:
    def create_leverage_script(self, provider, competitor_offer, savings_amount):
        """
        Generates a high-pressure script using 'Retention Trigger' keywords.
        """
        script = f"""
        STRATEGY: COMPETITOR MATCHING
        TARGET: {provider} Retention Department
        
        SCRIPT: 'I am calling to cancel my service. I have a verified offer from a 
        competitor that saves me ${savings_amount} per month. I have the account 
        transfer forms ready, but I am willing to stay if you apply a permanent 
        credit to match this rate today. Please connect me to a supervisor.'
        """
        return script

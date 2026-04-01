import plaid
from plaid.api import plaid_api
from plaid.model.transactions_get_request import TransactionsGetRequest
import os
from datetime import datetime, timedelta

class SentinelBankAgent:
    def __init__(self):
        configuration = plaid.Configuration(
            host=plaid.Environment.Sandbox,
            api_key={
                'clientId': os.getenv("PLAID_CLIENT_ID"),
                'secret': os.getenv("PLAID_SECRET"),
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def fetch_recent_transactions(self, access_token):
        """Autonomously retrieves transactions for the last 30 days."""
        start_date = (datetime.now() - timedelta(days=30)).date()
        end_date = datetime.now().date()
        
        request = TransactionsGetRequest(
            access_token=access_token,
            start_date=start_date,
            end_date=end_date
        )
        response = self.client.transactions_get(request)
        return response.to_dict()['transactions']

import pandas as pd
import os
from datetime import datetime

DATA_PATH = "./data/savings_log.csv"

class SentinelAnalytics:
    def __init__(self):
        # Initialize the CSV file if it doesn't exist
        if not os.path.exists(DATA_PATH):
            df = pd.DataFrame(columns=["Date", "Description", "Amount_Saved"])
            df.to_csv(DATA_PATH, index=False)

    def log_savings(self, description, amount):
        """Records a successful audit win."""
        new_data = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Description": description,
            "Amount_Saved": float(amount)
        }
        df = pd.read_csv(DATA_PATH)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

    def get_summary_data(self):
        """Returns data formatted for charts."""
        df = pd.read_csv(DATA_PATH)
        if df.empty:
            return None
        return df

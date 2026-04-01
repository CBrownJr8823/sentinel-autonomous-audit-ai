import pandas as pd

class SentinelForecaster:
    @staticmethod
    def predict_trend(data_frame):
        """Uses historical data to project future spending risks."""
        if len(data_frame) < 2:
            return "Insufficient data for forecasting."
        
        # Simple linear projection of spending
        data_frame['Date'] = pd.to_datetime(data_frame['Date'])
        latest_avg = data_frame['Amount_Saved'].mean()
        
        return f"Based on your audit history, Sentinel projects an additional ${latest_avg * 1.15:.2f} in potential reclaimed capital next month."

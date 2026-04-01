import logging
import datetime

class SentinelLogger:
    def __init__(self):
        # Creates a local file to track every "thought" and "error" the AI has
        logging.basicConfig(
            filename='sentinel_system.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def log_event(self, message):
        timestamp = datetime.datetime.now()
        logging.info(f"EVENT: {message}")
        print(f"[{timestamp}] System Logged: {message}")

    def log_error(self, error_message):
        logging.error(f"CRITICAL ERROR: {error_message}")
        print(f"⚠️ SYSTEM ALERT: Error handled and logged.")

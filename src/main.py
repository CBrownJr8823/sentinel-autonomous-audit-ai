import os
from dotenv import load_dotenv
from src.brain import SentinelBrain

# Load security keys from the .env file
load_dotenv()

def start_sentinel():
    # Initialize the AI Brain
    sentinel = SentinelBrain()
    print("🚀 SENTINEL AI: SYSTEM ONLINE & LEARNING...")
    
    while True:
        task = input("\nEnter a transaction or data to audit (or type 'exit'): ")
        if task.lower() == 'exit':
            print("Shutting down Sentinel...")
            break
        
        # 1. AI analyzes the data
        output = sentinel.analyze(task)
        print(f"\n--- AUDIT RESULT ---\n{output}")
        
        # 2. AI 'Learns' from this specific transaction for next time
        sentinel.learn_from_transaction(f"Task: {task} | Result: {output}")

if __name__ == "__main__":
    start_sentinel()

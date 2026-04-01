import hashlib
import os
import pandas as pd

USER_DB = "./data/users.csv"

class SentinelAuth:
    def __init__(self):
        if not os.path.exists(USER_DB):
            df = pd.DataFrame(columns=["username", "password_hash"])
            df.to_csv(USER_DB, index=False)

    def _hash_password(self, password):
        return hashlib.sha256(str.encode(password)).hexdigest()

    def create_user(self, username, password):
        df = pd.read_csv(USER_DB)
        if username in df['username'].values:
            return False, "User already exists."
        
        new_user = {"username": username, "password_hash": self._hash_password(password)}
        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        df.to_csv(USER_DB, index=False)
        return True, "User created successfully."

    def login(self, username, password):
        df = pd.read_csv(USER_DB)
        hashed_input = self._hash_password(password)
        user_row = df[df['username'] == username]
        
        if not user_row.empty and user_row.iloc[0]['password_hash'] == hashed_input:
            return True
        return False

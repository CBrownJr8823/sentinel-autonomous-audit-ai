import streamlit as st
from src.auth import SentinelAuth
from src.brain import SentinelBrain
from src.guard import SentinelGuard
from src.analytics import SentinelAnalytics
from src.dispute import DisputeEngine

st.set_page_config(page_title="Sentinel AI - Enterprise SaaS", page_icon="🛡️", layout="wide")

auth = SentinelAuth()

# --- LOGIN LOGIC ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🛡️ Sentinel AI Login")
    choice = st.selectbox("Login or Signup", ["Login", "Sign Up"])
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if choice == "Sign Up":
        if st.button("Create Account"):
            success, msg = auth.create_user(user, pwd)
            st.success(msg) if success else st.error(msg)
    else:
        if st.button("Login"):
            if auth.login(user, pwd):
                st.session_state['logged_in'] = True
                st.session_state['username'] = user
                st.rerun()
            else:
                st.error("Invalid credentials.")
    st.stop() # Stops the app from loading until login is successful

# --- PROTECTED APP CONTENT ---
st.sidebar.title(f"Welcome, {st.session_state['username']}")
if st.sidebar.button("Logout"):
    st.session_state['logged_in'] = False
    st.rerun()

# Load the rest of the assets only after login
sentinel, guard, analytics = SentinelBrain(), SentinelGuard(), SentinelAnalytics()

tab1, tab2 = st.tabs(["🔍 Audit Center", "📊 Performance"])
# ... (The rest of your tab1 and tab2 code from the previous step goes here)

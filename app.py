import streamlit as st
from src.brain import SentinelBrain
from src.dispute import DisputeEngine
from src.guard import SentinelGuard # Import the Bouncer

st.set_page_config(page_title="Sentinel AI - Secure Portal", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_assets():
    return SentinelBrain(), SentinelGuard()

sentinel, guard = load_assets()

st.title("🛡️ Sentinel: Secure Autonomous Audit Engine")
st.sidebar.markdown("### 🔒 Security Status: **Active**")
st.sidebar.info("Firewall: Scanning all inputs")

# --- UI Sections ---
uploaded_file = st.file_uploader("Upload PDF (Encrypted Transfer)", type="pdf")
doc_text = ""
if uploaded_file:
    doc_text = sentinel.process_pdf(uploaded_file)

user_input = st.text_area("Secure Audit Command:")
use_web = st.checkbox("🔍 Enable Market Research")

if st.button("🚀 Run Secure Audit"):
    if user_input:
        # --- THE FIREWALL CHECK ---
        is_safe, message = guard.scan_input(user_input)
        
        if not is_safe:
            st.error(message)
            sentinel.logger.log_error(f"BLOCKED ATTACK: {user_input[:50]}...")
        else:
            with st.spinner("Sentinel is analyzing..."):
                result = sentinel.analyze(user_input, context_data=doc_text, use_web=use_web)
                st.session_state['last_audit'] = result
                st.success("Audit Complete")
                st.write(result)
    else:
        st.error("Please enter a command.")

# Dispute Section (Keep as is)
if 'last_audit' in st.session_state:
    if st.button("📝 Generate Dispute Letter"):
        letter = DisputeEngine.generate_letter(st.session_state['last_audit'])
        st.text_area("Copy/Paste:", value=letter, height=200)

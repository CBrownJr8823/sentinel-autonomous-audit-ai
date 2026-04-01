import streamlit as st
from src.brain import SentinelBrain
from src.dispute import DisputeEngine

# Page Config
st.set_page_config(page_title="Sentinel AI Dashboard", page_icon="🛡️", layout="wide")

# Initialize Brain
@st.cache_resource
def load_brain():
    return SentinelBrain()

sentinel = load_brain()

st.title("🛡️ Sentinel: Autonomous Audit & Research Engine")
st.markdown("### *Identify Errors. Assert Rights. Reclaim Capital.*")

# --- Sidebar: System Status ---
st.sidebar.title("System Status")
st.sidebar.success("Core: Online")
st.sidebar.info("Memory: Active (RAG)")
st.sidebar.info("Web Research: Ready")

# --- Document Upload ---
uploaded_file = st.file_uploader("Upload PDF (Contract/Receipt)", type="pdf")
doc_text = ""
if uploaded_file:
    doc_text = sentinel.process_pdf(uploaded_file)
    st.info("📄 Document Analyzed & Added to Intelligence Base.")

# --- Analysis & Research Section ---
st.divider()
user_input = st.text_area("Audit Command:", placeholder="e.g., 'Check this Verizon bill for hidden fees and compare it to current market rates'")

# The new "Power Toggle"
use_web = st.checkbox("🔍 Enable Live Web Research (Compares against live market data)")

if st.button("🚀 Run Full Audit"):
    if user_input:
        with st.spinner("Sentinel is cross-referencing memory and researching the web..."):
            # We pass the web toggle to the brain here
            result = sentinel.analyze(user_input, context_data=doc_text, use_web=use_web)
            st.session_state['last_audit'] = result 
            
            st.success("Audit Complete")
            st.subheader("Sentinel Analysis")
            st.write(result)
    else:
        st.error("Please enter a command for Sentinel.")

# --- Dispute Generation ---
if 'last_audit' in st.session_state:
    st.divider()
    st.subheader("🛠️ Take Action")
    if st.button("📝 Generate Dispute Letter"):
        letter = DisputeEngine.generate_letter(st.session_state['last_audit'])
        st.text_area("Copy/Paste this to your email:", value=letter, height=300)
        st.download_button("Download Letter (.txt)", letter, file_name="sentinel_dispute.txt")

st.divider()
st.caption("Sentinel AI v1.2 | Multi-Agent Research Enabled")

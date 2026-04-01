import streamlit as st
from src.brain import SentinelBrain
from src.dispute import DisputeEngine

st.set_page_config(page_title="Sentinel AI Dashboard", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_brain():
    return SentinelBrain()

sentinel = load_brain()

st.title("🛡️ Sentinel: Autonomous Audit & Dispute Engine")
st.markdown("### *Identify Errors. Assert Rights. Reclaim Capital.*")

# --- Document Upload ---
uploaded_file = st.file_uploader("Upload PDF (Contract/Receipt)", type="pdf")
doc_text = ""
if uploaded_file:
    doc_text = sentinel.process_pdf(uploaded_file)
    st.info("📄 Document Analyzed & Memorized.")

# --- Analysis Section ---
user_input = st.text_area("Audit Command:", placeholder="e.g., 'Check this bill for overcharges compared to my last upload'")

if st.button("🔍 Run Full Audit"):
    if user_input:
        with st.spinner("Sentinel is cross-referencing memory..."):
            result = sentinel.analyze(user_input, context_data=doc_text)
            st.session_state['last_audit'] = result # Store for the dispute generator
            st.success("Audit Complete")
            st.subheader("Sentinel Analysis")
            st.write(result)
    else:
        st.error("Please enter a command.")

# --- NEW: Dispute Generation Section ---
if 'last_audit' in st.session_state:
    st.divider()
    st.subheader("🛠️ Take Action")
    if st.button("📝 Generate Dispute Letter"):
        letter = DisputeEngine.generate_letter(st.session_state['last_audit'])
        st.text_area("Copy/Paste this to your email:", value=letter, height=300)
        st.download_button("Download Letter (.txt)", letter, file_name="sentinel_dispute.txt")



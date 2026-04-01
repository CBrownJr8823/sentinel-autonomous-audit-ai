import streamlit as st
from src.brain import SentinelBrain

st.set_page_config(page_title="Sentinel AI Dashboard", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_brain():
    return SentinelBrain()

sentinel = load_brain()

st.title("Sentinel: Autonomous Audit Engine")
st.markdown("### *Upload documents or enter text for a flawless audit.*")

# --- NEW: File Upload Section ---
uploaded_file = st.file_uploader("Upload PDF Contract or Receipt", type="pdf")
doc_text = ""

if uploaded_file is not None:
    doc_text = sentinel.process_pdf(uploaded_file)
    st.info("📄 Document loaded and added to Sentinel's memory.")

# --- Input Area ---
user_input = st.text_area("What should Sentinel look for in this data?", 
                          placeholder="e.g., 'Audit this contract for hidden cancellation fees' or 'Compare this receipt to my past gym bills'")

if st.button("Run Sentinel Audit"):
    if user_input:
        with st.spinner("Sentinel is cross-referencing memory and documents..."):
            result = sentinel.analyze(user_input, context_data=doc_text)
            st.success("Audit Complete")
            st.markdown("#### Sentinel's Analysis:")
            st.write(result)
    else:
        st.error("Please enter a question for Sentinel.")

st.divider()
st.caption("Sentinel AI v1.1 | PDF Auditing Enabled")


import streamlit as st
from src.brain import SentinelBrain
import os

# Page Config: This makes it look like a real tech startup site
st.set_page_config(page_title="Sentinel AI Dashboard", page_icon="🛡️", layout="wide")

# Initialize the Brain (using Streamlit's cache so it doesn't reload every time)
@st.cache_resource
def load_brain():
    return SentinelBrain()

sentinel = load_brain()

# --- Sidebar UI ---
st.sidebar.title("🛡️ Sentinel Control")
st.sidebar.info("Status: Online & Learning")
if st.sidebar.button("Clear System Memory"):
    st.sidebar.warning("This would reset the learning database.")

# --- Main UI ---
st.title("Sentinel: Autonomous Audit Engine")
st.markdown("### *Continuous Intelligence. Flawless Auditing.*")

# Input Area
user_input = st.text_area("Enter transaction details, contract text, or financial data:", 
                          placeholder="e.g., 'Analyze my Verizon bill for hidden fees...'")

if st.button("Run Sentinel Audit"):
    if user_input:
        with st.spinner("Sentinel is analyzing and learning..."):
            # 1. Get the AI result
            result = sentinel.analyze(user_input)
            
            # 2. Learn from it
            sentinel.learn_from_transaction(f"User Input: {user_input} | Audit Result: {result}")
            
            # 3. Show the result in a nice box
            st.success("Audit Complete")
            st.markdown("#### Sentinel's Analysis:")
            st.write(result)
    else:
        st.error("Please enter data for Sentinel to analyze.")

# Footer
st.divider()
st.caption("Sentinel AI v1.0 | Built for Enterprise-Grade Financial Intelligence")

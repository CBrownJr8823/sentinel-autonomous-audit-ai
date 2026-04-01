import streamlit as st
import pandas as pd
from src.brain import SentinelBrain
from src.dispute import DisputeEngine
from src.guard import SentinelGuard
from src.analytics import SentinelAnalytics

st.set_page_config(page_title="Sentinel AI - Enterprise", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_assets():
    return SentinelBrain(), SentinelGuard(), SentinelAnalytics()

sentinel, guard, analytics = load_assets()

# --- THE UI TABS ---
tab1, tab2 = st.tabs(["🔍 Audit Command Center", "📊 Performance & Savings"])

with tab1:
    st.title("🛡️ Sentinel Secure Audit")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    doc_text = sentinel.process_pdf(uploaded_file) if uploaded_file else ""
    
    user_input = st.text_area("Audit Command:")
    use_web = st.checkbox("🔍 Enable Market Research")

    if st.button("🚀 Run Audit"):
        is_safe, msg = guard.scan_input(user_input)
        if not is_safe:
            st.error(msg)
        else:
            with st.spinner("Analyzing..."):
                result = sentinel.analyze(user_input, doc_text, use_web)
                st.session_state['last_audit'] = result
                st.success("Complete")
                st.write(result)

    if 'last_audit' in st.session_state:
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📝 Generate Dispute"):
                st.code(DisputeEngine.generate_letter(st.session_state['last_audit']))
        with col2:
            # NEW: Log savings directly from the UI
            save_amt = st.number_input("Found savings? Enter amount ($):", min_value=0.0)
            if st.button("📈 Log Savings to Dashboard"):
                analytics.log_savings("Manual Entry", save_amt)
                st.toast(f"Logged ${save_amt} to performance!")

with tab2:
    st.title("📈 Savings Performance")
    df = analytics.get_summary_data()
    if df is not None and not df.empty:
        total = df["Amount_Saved"].sum()
        st.metric("Total Capital Reclaimed", f"${total:,.2f}")
        
        # Display a Bar Chart of savings over time
        st.subheader("Savings History")
        st.bar_chart(data=df, x="Date", y="Amount_Saved")
        
        st.subheader("Audit Log")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No savings logged yet. Run an audit to begin.")

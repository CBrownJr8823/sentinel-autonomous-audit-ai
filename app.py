import streamlit as st
import pandas as pd
from src.auth import SentinelAuth
from src.brain import SentinelBrain
from src.guard import SentinelGuard
from src.analytics import SentinelAnalytics
from src.dispute import DisputeEngine
from src.vision import SentinelVision
from src.forecaster import SentinelForecaster

# --- Page Config & Styling ---
st.set_page_config(page_title="Sentinel AI - Absolute Version", page_icon="🛡️", layout="wide")

# --- Initialize Core Services ---
auth = SentinelAuth()

# --- Login / Signup Wall ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🛡️ Sentinel AI: Enterprise Login")
    choice = st.selectbox("Action", ["Login", "Sign Up"])
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if choice == "Sign Up":
        if st.button("Create Secure Account"):
            success, msg = auth.create_user(user, pwd)
            st.success(msg) if success else st.error(msg)
    else:
        if st.button("Authenticate"):
            if auth.login(user, pwd):
                st.session_state['logged_in'] = True
                st.session_state['username'] = user
                st.rerun()
            else:
                st.error("Invalid credentials.")
    st.stop()

# --- Post-Login: Load Intelligence Assets ---
@st.cache_resource
def load_assets():
    return SentinelBrain(), SentinelGuard(), SentinelAnalytics(), SentinelVision()

sentinel, guard, analytics, vision = load_assets()

# --- Sidebar Controls ---
st.sidebar.title(f"Welcome, {st.session_state['username']}")
st.sidebar.markdown("### 🔒 System Security: **Active**")
if st.sidebar.button("Logout"):
    st.session_state['logged_in'] = False
    st.rerun()

# --- Main UI Tabs ---
tab1, tab2, tab3 = st.tabs(["🔍 Audit Command Center", "📊 Performance & Forecasting", "⚙️ System Logs"])

with tab1:
    st.title("🛡️ Secure Audit Engine")
    
    col_a, col_b = st.columns(2)
    doc_text = ""
    
    with col_a:
        st.subheader("Upload Documents")
        uploaded_file = st.file_uploader("Upload PDF (Contract/Bill)", type="pdf")
        if uploaded_file:
            doc_text = sentinel.process_pdf(uploaded_file)
            st.info("📄 PDF intelligence extracted.")

    with col_b:
        st.subheader("Vision Scan")
        uploaded_img = st.file_uploader("📸 Scan Receipt/Image", type=["jpg", "png", "jpeg"])
        if uploaded_img:
            with st.spinner("Sentinel Vision is reading the image..."):
                img_data = vision.analyze_image(uploaded_img.getvalue())
                st.success("Vision Data Extracted")
                doc_text += f"\nImage Analysis: {img_data}"

    st.divider()
    user_input = st.text_area("Audit Command:", placeholder="e.g., 'Compare this receipt to my last Verizon bill and find overcharges'")
    use_web = st.checkbox("🔍 Enable Market Research Agent")

    if st.button("🚀 EXECUTE MISSION"):
        # Firewall Check
        is_safe, msg = guard.scan_input(user_input)
        if not is_safe:
            st.error(msg)
        else:
            with st.spinner("Sentinel is processing..."):
                result = sentinel.analyze(user_input, context_data=doc_text, use_web=use_web)
                st.session_state['last_audit'] = result
                st.subheader("Audit Results")
                st.write(result)

    if 'last_audit' in st.session_state:
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            if st.button("📝 Generate Dispute Letter"):
                letter = DisputeEngine.generate_letter(st.session_state['last_audit'])
                st.code(letter, language="text")
        with c2:
            save_amt = st.number_input("Capital Reclaimed ($):", min_value=0.0)
            if st.button("📈 Log Savings"):
                analytics.log_savings("Manual Audit Win", save_amt)
                st.toast(f"Saved ${save_amt}!")

with tab2:
    st.title("📈 Performance Analytics")
    df = analytics.get_summary_data()
    
    if df is not None and not df.empty:
        total_saved = df["Amount_Saved"].sum()
        st.metric("Total Capital Reclaimed", f"${total_saved:,.2f}")
        
        # Trend Analysis
        st.subheader("Savings Forecast")
        forecast_msg = SentinelForecaster.predict_trend(df)
        st.info(forecast_msg)
        
        st.bar_chart(data=df, x="Date", y="Amount_Saved")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No data available. Run an audit to begin tracking performance.")

with tab3:
    st.title("⚙️ System Integrity")
    st.write("Sentinel AI v1.5 | Enterprise Vision Enabled")
    if st.button("Clear Cache"):
        st.cache_resource.clear()
        st.success("System memory refreshed.")

import streamlit as st
import pandas as pd
import os
from src.auth import SentinelAuth
from src.brain import SentinelBrain
from src.guard import SentinelGuard
from src.analytics import SentinelAnalytics
from src.dispute import DisputeEngine
from src.vision import SentinelVision
from src.forecaster import SentinelForecaster
from src.voice import SentinelVoice
from audio_recorder_streamlit import audio_recorder

# --- Page Config & Styling ---
st.set_page_config(page_title="Sentinel AI - Absolute Agent", page_icon="🛡️", layout="wide")

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

# --- Post-Login: Load Assets ---
@st.cache_resource
def load_assets():
    return SentinelBrain(), SentinelGuard(), SentinelAnalytics(), SentinelVision(), SentinelVoice()

sentinel, guard, analytics, vision, voice_engine = load_assets()

# --- Sidebar Controls ---
st.sidebar.title(f"Welcome, {st.session_state['username']}")
st.sidebar.markdown("### 🔒 System Security: **Active**")
if st.sidebar.button("Logout"):
    st.session_state['logged_in'] = False
    st.rerun()

# --- Main UI Tabs ---
tab1, tab2, tab3 = st.tabs(["🎙️ Audit Command Center", "📊 Performance & Forecasting", "⚙️ System Integrity"])

with tab1:
    st.title("🛡️ Sentinel Autonomous Agent")
    
    # --- Input Methods Section ---
    col1, col2, col3 = st.columns(3)
    doc_text = ""

    with col1:
        st.subheader("📄 PDF Upload")
        uploaded_file = st.file_uploader("Contract/Bill", type="pdf")
        if uploaded_file:
            doc_text = sentinel.process_pdf(uploaded_file)
            st.info("PDF Intelligence Extracted.")

    with col2:
        st.subheader("📸 Vision Scan")
        uploaded_img = st.file_uploader("Receipt Image", type=["jpg", "png", "jpeg"])
        if uploaded_img:
            with st.spinner("Reading Image..."):
                img_data = vision.analyze_image(uploaded_img.getvalue())
                st.success("Vision Data Loaded.")
                doc_text += f"\nImage Data: {img_data}"

    with col3:
        st.subheader("🎙️ Voice Command")
        audio_bytes = audio_recorder(text="Click to speak", icon_size="2x")
        if audio_bytes:
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_bytes)
            with st.spinner("Transcribing..."):
                voice_text = voice_engine.transcribe_audio("temp_audio.wav")
                st.session_state['voice_input'] = voice_text
                st.success(f"Heard: {voice_text}")
                os.remove("temp_audio.wav")

    st.divider()

    # Process either typed input or voice input
    default_input = st.session_state.get('voice_input', "")
    user_input = st.text_area("Audit Command:", value=default_input, placeholder="Ask Sentinel to audit your data...")
    
    use_web = st.checkbox("🔍 Enable Market Research Agent")

    if st.button("🚀 EXECUTE MISSION"):
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
                st.code(DisputeEngine.generate_letter(st.session_state['last_audit']), language="text")
        with c2:
            save_amt = st.number_input("Found Savings ($):", min_value=0.0)
            if st.button("📈 Log Savings"):
                analytics.log_savings("Agent Audit Win", save_amt)
                st.toast("Logged to Dashboard!")

with tab2:
    st.title("📊 Performance & Trends")
    df = analytics.get_summary_data()
    if df is not None and not df.empty:
        st.metric("Total Reclaimed", f"${df['Amount_Saved'].sum():,.2f}")
        st.info(SentinelForecaster.predict_trend(df))
        st.bar_chart(data=df, x="Date", y="Amount_Saved")
    else:
        st.info("No audit history found.")

with tab3:
    st.title("⚙️ Integrity Settings")
    st.write("System: Sentinel v1.8 (Agentic)")
    if st.button("Refresh Cache"):
        st.cache_resource.clear()
        st.rerun()

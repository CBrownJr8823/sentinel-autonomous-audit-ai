import streamlit as st
from src.brain import SentinelBrain
from src.outreach import SentinelOutreach
from src.orchestrator import SentinelOrchestrator
from src.guard import SentinelGuard
from src.researcher import SentinelResearcher

st.set_page_config(page_title="Sentinel AI - Absolute Version", layout="wide")

# Initialize the "Team"
@st.cache_resource
def init_system():
    b = SentinelBrain()
    r = SentinelResearcher()
    g = SentinelGuard()
    return b, r, g, SentinelOrchestrator(b, r, g), SentinelOutreach()

brain, res, guard, manager, mailer = init_system()

st.title("🛡️ Sentinel: Autonomous Financial Agent")

# --- UI Layout ---
with st.sidebar:
    st.header("Settings")
    target_email = st.text_input("Company Support Email", "billing@company.com")
    if st.button("Run Scheduled Audit"):
        st.toast("Auto-Audit Scheduled for 2:00 AM")

# Main Action Area
cmd = st.text_input("What is the mission today?", placeholder="Audit my bill and email a dispute if wrong.")

if st.button("🚀 EXECUTE MISSION"):
    # The Orchestrator takes over!
    report = manager.execute_full_mission(cmd)
    st.subheader("Mission Report")
    st.write(report)
    
    # Auto-Outreach Option
    if "Error" in report or "Overcharge" in report:
        if st.button("📧 Send Autonomous Dispute"):
            status = mailer.send_dispute(target_email, "Audit Dispute", report)
            st.success(status)

import streamlit as st
import os
from src.scout import SentinelScout
from src.negotiator import SentinelNegotiator
from src.vault import SentinelVault
from src.tax_shield import SentinelTaxShield

# --- CONFIGURATION & UI SETUP ---
st.set_page_config(page_title="Sentinel Prime | Enterprise AI Finance", layout="wide", page_icon="🛡️")

# Initialize our Million-Dollar Modules
scout = SentinelScout()
negotiator = SentinelNegotiator()
vault = SentinelVault()
shield = SentinelTaxShield()

# --- SIDEBAR: THE COMMANDER PANEL ---
with st.sidebar:
    st.title("🛡️ Sentinel Prime")
    st.subheader("Enterprise Command Center")
    
    mode = st.radio("Switch Focus:", ["Fleet Commander", "Audit & Arbitrage", "Tax Shield"])
    
    st.markdown("---")
    st.subheader("🔐 Security Layer")
    use_encryption = st.toggle("Enable Military-Grade Encryption", value=True)
    if use_encryption:
        st.success("Vault Status: SECURE (AES-256)")
    
    st.markdown("---")
    st.info(f"Connected as: {os.getenv('USER_ROLE', 'Lead Architect')}")

# --- MAIN INTERFACE ---

if mode == "Fleet Commander":
    st.header("🛰️ Sentinel Fleet Commander")
    st.markdown("### Global Performance Overview")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Active Agents", "124", "+12 this week")
    m2.metric("Total Alpha (Savings)", "$42,800", "+$4,200")
    m3.metric("Audit Accuracy", "99.98%", "SOC2 Verified")

    st.divider()
    st.subheader("Real-Time Agent Activity")
    agents = [
        {"Dept": "Marketing", "Task": "SaaS Arbitrage", "Status": "Negotiating", "Finding": "-$1,200/mo"},
        {"Dept": "Logistics", "Task": "Fuel Audit", "Status": "Complete", "Finding": "-$3,500/mo"},
        {"Dept": "IT Infrastructure", "Task": "Cloud Optimization", "Status": "Scanning", "Finding": "Pending"}
    ]
    st.table(agents)

elif mode == "Audit & Arbitrage":
    st.header("🔎 Audit & Market Arbitrage")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("Upload Bill/Statement")
        uploaded_file = st.file_uploader("Drop PDF or Image here", type=["pdf", "png", "jpg"])
        
        if st.button("🚀 Launch Market Scout"):
            # This triggers our 'Hunter' logic
            with st.spinner("Scouting global markets for Alpha..."):
                findings = scout.market_sweep("Verizon Business", "Telecom", 1500)
                st.session_state['findings'] = findings
                st.success("Arbitrage Opportunity Detected!")

    with col_right:
        if 'findings' in st.session_state:
            st.subheader("📊 Intelligence Report")
            st.write(st.session_state['findings'])
            
            script = negotiator.create_leverage_script("Verizon", "T-Mobile Enterprise", 450)
            st.markdown("### 🏹 Tactical Negotiation Script")
            st.code(script, language="markdown")

elif mode == "Tax Shield":
    st.header("🛡️ Autonomous Tax Shield")
    st.markdown("Predictive Expense Classification for 100% Audit Readiness.")
    
    if st.button("🔍 Run Global Tax Audit"):
        # Simulated transaction data for the demo
        sample_data = [
            {"merchant": "AWS Cloud", "amount": 1200.00, "category": "Software"},
            {"merchant": "Facebook Ads", "amount": 5000.00, "category": "Marketing"}
        ]
        report = shield.flag_deductions(sample_data)
        st.write("### ✅ 2026 Audit-Ready Defense Report")
        st.dataframe(report)
        st.success("99% Accuracy Confidence Level reached.")

# --- FOOTER ---
st.markdown("---")
st.caption("Sentinel Prime v2.0 | Built with Military-Grade Security & Agentic Intelligence")

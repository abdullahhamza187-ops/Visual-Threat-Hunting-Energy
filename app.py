import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Setup the Webpage
st.set_page_config(page_title="GridShield AI", page_icon="⚔️", layout="wide")
st.title("⚔️ GridShield AI: Real-Time Cyber-Physical Monitor")
st.markdown("### Power Grid Threat Detection Dashboard")

st.divider()

# 2. Create empty containers that we can update dynamically
col1, col2 = st.columns(2)

with col1:
    st.subheader("Live Telemetry Stream (3-Phase)")
    chart_box = st.empty() # This box will update the graph

with col2:
    st.subheader("Active Threat Log")
    alert_box = st.empty() # This box will update the alerts

st.divider()

# 3. Create the "Play" Button for your presentation
if st.button("▶️ INITIATE LIVE GRID SIMULATION", use_container_width=True):
    
    # --- PHASE 1: STABLE GRID (Runs for 4 seconds) ---
    for _ in range(4):
        # Generate stable, normal telemetry (small waves)
        stable_data = pd.DataFrame(np.random.randn(20, 3) * 0.5, columns=['Ia', 'Ib', 'Ic'])
        chart_box.line_chart(stable_data)
        
        # Show Green / Secure alerts
        with alert_box.container():
            st.success("✅ Phase A: SECURE")
            st.success("✅ Phase B: SECURE")
            st.success("✅ Phase C: SECURE")
            st.info("🟢 SYSTEM STATUS: Operating normally within 3-Sigma limits.")
            
        time.sleep(1) # Wait 1 second before the next frame
        
    # --- PHASE 2: CYBER ATTACK INJECTION (The Spike) ---
    # Generate hacked telemetry (massive spikes outside the perimeter)
    hacked_data = pd.DataFrame(np.random.randn(20, 3) * 8, columns=['Ia', 'Ib', 'Ic'])
    chart_box.line_chart(hacked_data)
    
    # Show Red / Critical alerts
    with alert_box.container():
        st.error("🚨 CRITICAL: Phase A Pulse Injection Detected!")
        st.error("🚨 3-SIGMA PERIMETER BREACHED")
        st.warning("⚠️ ACTION: AUTOMATIC ISOLATION ENGAGED")
        st.info("📝 FORENSICS: Threat saved to threat_audit_log.csv")
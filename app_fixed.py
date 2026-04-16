# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Setup the Webpage - NO EMOJIS to avoid encoding issues
st.set_page_config(page_title="GridShield AI", page_icon=None, layout="wide")
st.title("GridShield AI: Real-Time Cyber-Physical Monitor")
st.markdown("### Power Grid Threat Detection Dashboard")

st.divider()

# 2. Create empty containers that we can update dynamically
col1, col2 = st.columns(2)

with col1:
    st.subheader("Live Telemetry Stream (3-Phase)")
    chart_box = st.empty() 

with col2:
    st.subheader("Active Threat Log")
    alert_box = st.empty() 

st.divider()

# 3. Create the Play Button
if st.button("Start Live Grid Simulation", use_container_width=True):
    
    # PHASE 1: STABLE GRID (4 seconds)
    for _ in range(4):
        stable_data = pd.DataFrame(np.random.randn(20, 3) * 0.5, columns=['Ia', 'Ib', 'Ic'])
        chart_box.line_chart(stable_data)
        
        with alert_box.container():
            st.success("Phase A: SECURE")
            st.success("Phase B: SECURE") 
            st.success("Phase C: SECURE")
            st.info("SYSTEM STATUS: Normal operation")
            
        time.sleep(1)
        
    # PHASE 2: CYBER ATTACK SIMULATION
    hacked_data = pd.DataFrame(np.random.randn(20, 3) * 8, columns=['Ia', 'Ib', 'Ic'])
    chart_box.line_chart(hacked_data)
    
    with alert_box.container():
        st.error("CRITICAL: Phase A Attack Detected!")
        st.error("3-SIGMA BREACH DETECTED")
        st.warning("EMERGENCY ISOLATION ACTIVE")
        st.info("Threat logged to CSV")

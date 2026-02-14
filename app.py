import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

st.set_page_config(page_title="AQI Monitoring Lab", page_icon="🌬️", layout="wide")

st.markdown("""
    <style>
    .aqi-good { background-color: #2ecc71; color: white; padding: 20px; border-radius: 10px; text-align: center; }
    .aqi-moderate { background-color: #f1c40f; color: black; padding: 20px; border-radius: 10px; text-align: center; }
    .aqi-poor { background-color: #e67e22; color: white; padding: 20px; border-radius: 10px; text-align: center; }
    .aqi-hazardous { background-color: #e74c3c; color: white; padding: 20px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌬️ Real-Time Air Quality Monitoring")

if 'aqi_log' not in st.session_state:
    st.session_state.aqi_log = pd.DataFrame(columns=['Time', 'PPM'])

placeholder = st.empty()

for _ in range(100):
    ppm = round(np.random.uniform(300, 1200), 0)
    
    new_data = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), ppm]], columns=['Time', 'PPM'])
    st.session_state.aqi_log = pd.concat([st.session_state.aqi_log, new_data]).tail(20)

    with placeholder.container():
        c1, c2 = st.columns([1, 2])
        
        with c1:
            if ppm < 500:
                status, css, advice = "GOOD", "aqi-good", "Air quality is satisfactory."
            elif ppm < 800:
                status, css, advice = "MODERATE", "aqi-moderate", "Sensitive individuals should limit outdoor activity."
            elif ppm < 1000:
                status, css, advice = "POOR", "aqi-poor", "Everyone may begin to experience health effects."
            else:
                status, css, advice = "HAZARDOUS", "aqi-hazardous", "Health warning of emergency conditions."
            
            st.markdown(f'<div class="{css}"><h1>{status}</h1><p>AQI PPM: {ppm}</p></div>', unsafe_allow_html=True)
            st.info(f"💡 Advice: {advice}")

        with c2:
            fig = px.line(st.session_state.aqi_log, x='Time', y='PPM', title="Gas Concentration Trend (PPM)")
            st.plotly_chart(fig, use_container_width=True)
            
    time.sleep(2)

# IoT Radiation Monitor ☢️

A radiological safety node utilizing a Geiger-Müller tube to detect ionizing radiation and stream real-time dose-rate data via WiFi.

## Description
A radiological safety node utilizing a Geiger-Müller tube to detect ionizing radiation and stream real-time dose-rate data via WiFi.

## Key Features
- **Real-Time CPM Tracking:** High-precision interrupt-driven counting of ionizing events.
- **Dose Rate Calculation:** Converts raw Counts Per Minute (CPM) into Microsieverts per hour (uSv/h).
- **Radiological Alerts:** Visual and audible alarms trigger when radiation exceeds the 0.50 uSv/h threshold.

## Tech Stack
- **Language:** Python, C++
- **Libraries:** Streamlit, Plotly, Pandas, ESP8266WiFi
- **Hardware:** Geiger-Müller Counter (J305), NodeMCU

## Engineering Logic
- **Hardware:** The NodeMCU uses a hardware interrupt to count voltage pulses from the Geiger tube's high-voltage circuit.
- **Software:** Python calculates the statistical deviation of the background radiation to identify significant radiological spikes.

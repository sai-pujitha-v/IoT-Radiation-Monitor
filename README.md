# 🌬️ IoT Air Quality Index (AQI) Station

A real-time environmental monitoring system that tracks hazardous gases and calculates the local Air Quality Index (AQI) to provide health-based recommendations.

## 🚀 Features
- **Multi-Gas Detection:** Tracks CO2, Smoke, and Ammonia (NH3).
- **AQI Calculation:** Converts raw sensor data into standardized AQI levels.
- **Health Advisory:** Generates automatic warnings (e.g., "Wear a Mask") based on pollution levels.
- **Remote Telemetry:** Real-time data streaming to a Python dashboard via WiFi.

## ⚙️ Engineering Logic
- **Hardware:** ESP32 interprets analog signals from an MQ-135 sensor.
- **Software:** Python applies a logarithmic curve to the sensor's voltage output to estimate gas concentration in PPM (Parts Per Million).

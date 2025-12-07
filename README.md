# Home Assistant MQTT Gas Sensor – Nakshatra Automation Assignment

## Student Details

- **Name:** Reddi Satyanarayana  
- **Register Number:** 42614109  
- **MQTT Topic Used:** `home/reddisatyanarayana-2025/sensor`  

This repository contains my solution for the **Home Assistant + MQTT** assignment for **Nakshatra Automation**.

---

## Project Overview

The project demonstrates end-to-end integration of:

1. **Python script** publishing sensor data over MQTT  
2. **Mosquitto MQTT Broker** running inside Home Assistant  
3. **Home Assistant** subscribing to the MQTT topic and displaying the values on the dashboard  

Published sensors:

- `temperature` (°C) – random values between 24–30  
- `humidity` (%) – random values between 40–70  
- `gas` (ppm) – simulated gas level between 0–100  

All values are sent as a JSON payload to:
Example Payload:
{
  "student_name": "Reddi Satyanarayana",
  "unique_id": "42614109",
  "temperature": 27.5,
  "humidity": 64.7,
  "gas": 92
}
```text
home/reddisatyanarayana-2025/sensor


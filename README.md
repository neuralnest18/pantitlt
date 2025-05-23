# pantitlt
This project integrates an ESP32 camera module with Python scripts to perform real-time face tracking. The system moves a pan-tilt mechanism based on detected faces using computer vision techniques.



# Pan-Tilt Face Tracking Bot 🤖📷

This project is a real-time face tracking system using an ESP32-CAM module and servo motors to pan and tilt the camera. It integrates OpenCV for face detection, MicroPython for microcontroller programming, and a Flask interface for live video streaming and interaction.

---

## 🚀 Features

- 🎯 Real-time face detection using OpenCV
- 🔄 Servo-controlled camera movement (pan and tilt)
- 🌐 Flask-based web interface for live video feed and control
- 🔌 MicroPython code running on ESP32-CAM for servo control
- 💬 Optional chatbot interface with real-time communication

---

## 🛠️ Tech Stack

| Component       | Technology Used          |
|-----------------|--------------------------|
| Face Detection  | OpenCV (Python)          |
| Microcontroller | ESP32-CAM + MicroPython  |
| Servo Control   | GPIO (MicroPython PWM)   |
| Web Interface   | Flask (Python)           |
| Streaming       | MJPEG stream (OpenCV + Flask) |
| Chatbot (optional) | AIML + Flask (chat endpoint) |

---

## 🧰 Requirements

- Python 3.8+
- OpenCV
- Flask
- PySerial (for serial communication)
- ESP32-CAM board
- 2 Servo motors (for pan and tilt)
- MicroPython flashed on ESP32-CAM
- Web browser (for accessing the Flask interface)

---

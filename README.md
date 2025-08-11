# DOBI_UI

DOBI_UI is a **Streamlit-based user interface** for controlling and monitoring an autonomous inspection robot.  
It integrates with **ROS 2** and **micro-ROS** via a WebSocket bridge, supports **live video streaming**, and runs **object detection** with YOLOv8.

---

## 📂 Project Structure
```
DOBI_UI/
│── best.pt # YOLO model weights (Ultralytics YOLOv8)
│── main.py # Streamlit UI entry point
│── run_bridge.sh # Script to start ROS ↔ WebSocket bridge
│
├── assets/ # UI images, icons, etc.
├── bridge/
│ ├── ros_node.py # ROS 2 node handling robot communication
│ └── server.py # WebSocket bridge server
│
├── camera/
│ └── camera_handler.py # Handles camera feed streaming
│
├── control/
│ ├── auto_navigation.py # Autonomous navigation control
│ └── manual_control.py # Manual driving control
│
├── detection/
│ └── alert_logger.py # Logs detection alerts
│
└── utils/
└── config.py # Configuration parameters
```

---

## ⚙️ Installation (UI Only)

These steps assume **ROS 2 and micro-ROS are already installed** on your system.  
This will only install dependencies required for **Streamlit UI + YOLO object detection**.

```bash
# 1️⃣ Install Python dependencies
pip install streamlit opencv-python numpy websockets roslibpy ultralytics

# 2️⃣ Clone the repository
git clone https://github.com/YourUserName/DOBBI_UI.git
cd DOBBI_UI

# 3️⃣ Make bridge script executable
chmod +x run_bridge.sh

```

## ▶️ Running DOBI_UI
In two separate terminals:

Terminal 1 — Start the ROS ↔ WebSocket bridge:


./run_bridge.sh

Terminal 2 — Start the Streamlit UI:


streamlit run main.py --server.port 8501 --server.address 0.0.0.0

---

## 🌐 Accessing the UI
From any device on the same network:
http://<raspberry_pi_ip>:8501
Replace <raspberry_pi_ip> with the IP address of your Raspberry Pi.





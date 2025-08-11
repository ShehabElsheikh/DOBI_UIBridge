
---

## ⚙️ Installation (Raspberry Pi - Ubuntu 22.04 with ROS 2 & micro-ROS already installed)

Follow these steps **only for DOBI_UI** setup (ROS 2 installation is assumed to be complete):

```bash
# 1️⃣ Update and install Python dependencies
sudo apt update
sudo apt install python3-pip -y

# 2️⃣ Install required Python packages
pip install streamlit opencv-python numpy websockets roslibpy

# 3️⃣ Navigate to DOBI_UI project folder
cd ~/DOBI_UI

# 4️⃣ Make the bridge script executable
chmod +x run_bridge.sh
```
---
## 🚀 Running DOBI_UI
Open two separate terminals:

Terminal 1 – Start ROS ↔ WebSocket Bridge:


./run_bridge.sh
Terminal 2 – Start the Streamlit UI:


streamlit run main.py --server.port 8501 --server.address 0.0.0.0
---
🌐 Accessing the UI
Once the UI is running, open a browser on your local network and go to:
http://<raspberry_pi_ip>:8501
Replace <raspberry_pi_ip> with your Raspberry Pi's IP address.

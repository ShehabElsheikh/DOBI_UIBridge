name: DOBI_UI
description: >
  DOBI_UI is a Streamlit-based user interface for controlling and monitoring
  an autonomous inspection robot. It provides live video streaming, manual
  and autonomous control modes, and object detection capabilities.
  This guide covers installing and running the UI components only.

project_structure: |
  DOBI_UI/
  │ best.pt                  # YOLO model weights
  │ main.py                   # Streamlit UI entry point
  │ run_bridge.sh              # Script to start the ROS ↔ WebSocket bridge
  │
  ├── assets/                  # UI images, icons, etc.
  ├── bridge/
  │   ros_node.py              # ROS 2 node handling robot communication
  │   server.py                # WebSocket bridge server
  │
  ├── camera/
  │   camera_handler.py        # Handles camera feed streaming
  │
  ├── control/
  │   auto_navigation.py       # Autonomous navigation control
  │   manual_control.py        # Manual driving control
  │
  ├── detection/
  │   alert_logger.py          # Logs detection alerts
  │
  └── utils/
      config.py                 # Configuration parameters

prerequisites: |
  - Python 3.8 or later installed on Raspberry Pi
  - ROS 2 and micro-ROS already installed
  - Access to a terminal with internet connection

installation:
  - step: 1
    command: pip install streamlit opencv-python numpy websockets roslibpy
    description: Install all required Python packages for the UI.
  - step: 3
    command: cd DOBI_UI
    description: Navigate to the project folder.
  - step: 4
    command: chmod +x run_bridge.sh
    description: Make the bridge script executable.

running:
  - step: 1
    command: ./run_bridge.sh
    description: Start the ROS ↔ WebSocket bridge.
  - step: 2
    command: streamlit run main.py --server.port 8501 --server.address 0.0.0.0
    description: Start the Streamlit UI on all network interfaces.
  - step: 3
    description: >
      Access the UI from a browser on another device:
      http://<raspberry_pi_ip>:8501

notes: |
  - Replace `<raspberry_pi_ip>` with the actual IP address of your Raspberry Pi.
  - Ensure ROS 2 and micro-ROS nodes are already running before starting the UI.
  - The YOLO model file `best.pt` must be present in the project root.

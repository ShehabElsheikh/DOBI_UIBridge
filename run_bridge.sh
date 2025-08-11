#!/bin/bash
# ==========================================
# Run the dobi-UI FastAPI <-> ROS2 bridge
# ==========================================

# Fail on error
set -e

# Optional: activate your Python venv
# source venv/bin/activate

echo "[Bridge] Starting FastAPI WebSocket server with ROS2 integration..."
python3 -m bridge.server

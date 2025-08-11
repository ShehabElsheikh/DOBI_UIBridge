# main.py

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from camera.camera_handler import start_camera, stop_camera, get_latest_frame
from detection.alert_logger import log_detection, get_recent_alerts, clear_alerts
import json
import websocket

# === WebSocket connection to bridge ===
try:
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8000/ws")
except Exception as e:
    ws = None
    st.warning(f"Could not connect to bridge: {e}")

# === Page Config ===
st.set_page_config(layout="wide")
st.title("🤖 DOBI: Autonomous Inspection System")

# === STATE ===
if 'nav_mode' not in st.session_state:
    st.session_state.nav_mode = "manual"

# === TOP BAR ===
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🚗 Navigation Mode")
    nav_choice = st.radio("Choose Mode:", ["Manual", "Autonomous"], horizontal=True)

    if nav_choice.lower() != st.session_state.nav_mode:
        st.session_state.nav_mode = nav_choice.lower()

    if st.session_state.nav_mode == "manual":
        st.subheader("🎮 Manual Control")

        if ws:
            if st.button("⬆️ Forward (W)"):
                ws.send(json.dumps({"type": "command", "data": "forward"}))
            if st.button("⬅️ Left (A)"):
                ws.send(json.dumps({"type": "command", "data": "left"}))
            if st.button("➡️ Right (D)"):
                ws.send(json.dumps({"type": "command", "data": "right"}))
            if st.button("⬇️ Backward (S)"):
                ws.send(json.dumps({"type": "command", "data": "backward"}))
            if st.button("⛔ Stop (X)"):
                ws.send(json.dumps({"type": "command", "data": "stop"}))
        else:
            st.warning("Bridge not connected, commands won't be sent.")

with col2:
    st.subheader("🎮 Camera Control")
    cam_col1, cam_col2 = st.columns(2)

    with cam_col1:
        if st.button("▶️ Start Camera"):
            start_camera(log_detection)
    with cam_col2:
        if st.button("⏹ Stop Camera"):
            stop_camera()

# === LIVE CAMERA FEED ===
st.subheader("📷 Live Feed with Detection")
frame = get_latest_frame()
if frame is not None:
    st.image(frame, channels="BGR", caption="Live Annotated Feed")
else:
    st.info("Camera not active. Click 'Start Camera' to begin.")

# === ALERTS PANEL ===
with st.sidebar:
    st.header("🚨 Detection Alerts")
    if st.button("🧹 Clear Alerts"):
        clear_alerts()

    alerts = get_recent_alerts(10)
    if alerts:
        for alert in alerts:
            st.markdown(
                f"**[{alert['time']}]** `{alert['label'].upper()}` - *Severity:* {alert['severity']} | *Location:* {alert['location']}"
            )
    else:
        st.markdown("No alerts yet.")

# === AUTO REFRESH ===
if frame is not None:
    st_autorefresh(interval=1000, limit=None, key="feed-refresh")

# === FOOTER ===
st.markdown("---")
st.caption("DOBI BETA | Modular Autonomous Navigation + Real-Time Detection")

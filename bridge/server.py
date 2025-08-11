# bridge/server.py

import asyncio
import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .ros_node import RosNodeHandler

app = FastAPI()

# Allow connections from Streamlit UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ros_handler = RosNodeHandler()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            try:
                msg = await asyncio.wait_for(websocket.receive_text(), timeout=0.05)
                data = json.loads(msg)

                # Handle command from UI
                if data.get("type") == "command":
                    ros_handler.publish_command(data["data"])

            except asyncio.TimeoutError:
                pass  # No incoming message, proceed to send ROS data

            # Send latest ROS data back to UI
            ros_data = ros_handler.get_latest_data()
            await websocket.send_text(json.dumps({
                "type": "ros_data",
                "data": ros_data
            }))

    except Exception as e:
        print(f"[Bridge] WebSocket closed: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

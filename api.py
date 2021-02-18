"""
A simple api to handle and transform websocket connection between clients
"""

from typing import List, Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data: str):
        for _conn in self.active_connections:
            try:
                await _conn.send_text(data)
            except Exception:
                pass


manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def session_messages(
    *,
    websocket: WebSocket,
) -> Any:
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

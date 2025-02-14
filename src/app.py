from fastapi import FastAPI, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class MathProblem(BaseModel):
    problem: str

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    while True:
        try:
            # Wait for data from client
            data = await websocket.receive_text()
            print(f"Received math problem: {data}")
            
            # Send acknowledgment back
            await websocket.send_json({"message": "Problem received successfully"})
            
        except Exception as e:
            print(f"Connection closed: {e}")
            break

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000) 
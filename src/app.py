from fastapi import FastAPI, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import webbrowser

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("\nWaiting for input...\n")
    
    while True:
        try:
            # Wake up only when data is received
            data = await websocket.receive_text()
            
            # Print received text
            print("Received text:", data)
            print("\nWaiting for next input...\n")
            
            # Send confirmation back to frontend
            await websocket.send_json({
                "message": "Text received successfully",
                "received_text": data
            })
            
        except Exception as e:
            print(f"Connection closed: {e}")
            break

if __name__ == "__main__":
    print("\nServer starting...")
    print("Access the application at: http://localhost:8000")
    print("Press Ctrl+C to stop the server\n")
    
    # Open browser automatically
    webbrowser.open('http://localhost:8000')
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 

from fastapi  import FastAPI, WebSocket
import random


# Create application
app = FastAPI(title='websocket example')


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print('Accepting client connection...')
    await websocket.accept()
    while True:
        try:
            # wait for the message from the client
            await websocket.receive_text()
            # send message to the client
            resp = {'value': random.uniform(0,1)}
            await websocket.send_json(resp)
        except Exception as e:
            print('error:', e)
            break
    print ('Bye....')
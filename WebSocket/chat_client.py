import asyncio
import websockets

async def receive_messages():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            # Espera y muestra mensajes recibidos
            message = await websocket.recv()
            print(f"Mensaje recibido: {message}")

async def send_messages():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            # Lee el mensaje desde la entrada del usuario y lo envía
            message = input("Ingrese un mensaje: ")
            await websocket.send(message)

# Ejecuta el cliente
asyncio.gather(receive_messages(), send_messages())

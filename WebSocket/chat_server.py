import asyncio
import websockets

async def handle_client(websocket, path):
    # Espera y procesa los mensajes del cliente
    async for message in websocket:
        # Reenvía el mensaje a todos los clientes conectados
        await asyncio.gather(
            *[client.send(message) for client in clients if client != websocket]
        )

# Lista para almacenar clientes conectados
clients = set()

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print(f"Servidor de chat iniciado en {server.sockets[0].getsockname()}")

    # Bucle principal
    async with server:
        await server.serve_forever()

# Ejecuta el servidor
asyncio.run(main())

import asyncio
import websockets

# Lista para almacenar las conexiones de los clientes
clientes = set()

async def manejar_mensaje(mensaje, cliente):
    # Enviar el mensaje a todos los clientes conectados
    for cliente_conectado in clientes:
        if cliente_conectado != cliente:
            await cliente_conectado.send(mensaje)

async def servidor(websocket, path):
    # Agregar nuevo cliente a la lista
    clientes.add(websocket)
    try:
        # Bucle para manejar los mensajes del cliente
        async for mensaje in websocket:
            # Procesar el mensaje recibido del cliente
            await manejar_mensaje(mensaje, websocket)
    finally:
        # Eliminar cliente cuando se desconecte
        clientes.remove(websocket)

# Iniciar el servidor WebSocket en el puerto 8765
start_server = websockets.serve(servidor, "localhost", 8765)

# Correr el servidor
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

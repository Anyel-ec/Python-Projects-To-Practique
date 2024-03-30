from flask import Flask, request, jsonify
import requests
import queue

app = Flask(__name__)
product_queue = queue.Queue()

# Ruta para agregar productos al servidor de colas
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    producto = request.json
    product_queue.put(producto)
    return jsonify({"message": "Producto agregado a la cola"}), 200

# Ruta para enviar productos a otra API
@app.route('/enviar_productos', methods=['POST'])
def enviar_productos():
    try:
        while not product_queue.empty():
            producto = product_queue.get()
            # Envía el producto a la otra API en la ruta /ruta/productos
            response = requests.post("http://anyel.top/ruta/productos", json=producto) # Cambiar a la ruta del producto de la API 
            if response.status_code == 200:
                print("Producto enviado exitosamente a la otra API:", producto)
            else:
                print("Error al enviar el producto a la otra API:", producto)
    except Exception as e:
        print("Error al enviar productos:", e)
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Productos enviados correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)

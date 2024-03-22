from flask import Flask, jsonify, request
import ssl

app = Flask(__name__)

@app.route('/api/resource', methods=['GET'])
def get_resource():
    # Implementa la lógica para obtener un recurso
    return jsonify({'message': 'GET request to the resource'})

@app.route('/api/resource', methods=['POST'])
def create_resource():
    # Implementa la lógica para crear un recurso
    data = request.json
    # Procesa los datos recibidos en la solicitud POST
    return jsonify({'message': 'POST request to the resource', 'data': data})

# Configura el contexto SSL con los certificados generados
if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem') # se debe generar el certificado y la llave privada con este comando
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    app.run(debug=True, ssl_context=context)

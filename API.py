from flask import Flask, jsonify

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta que responde a solicitudes GET
@app.route('/saludo', methods=['GET'])
def saludar():
    mensaje = {'mensaje': '¡Hola, mundo! Esta es mi primera API en Python.'}
    return jsonify(mensaje)

# Ejecuta la aplicación en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True)

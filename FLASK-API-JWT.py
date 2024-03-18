from flask import Flask, request, jsonify
from jwt import encode, decode  # Agrega decode aquí
import datetime

app = Flask(__name__)

# Clave secreta para firmar el token
SECRET_KEY = 'anyel_ec'

# Ruta para la autenticación y generación del token
@app.route('/login', methods=['POST'])
def login():
    # Verifica las credenciales (en este ejemplo, se usa un usuario y contraseña fijos)
    if request.json and request.json['usuario'] == 'anyel' and request.json['contraseña'] == 'ec':
        # Genera un token con un payload que incluye el usuario y la fecha de expiración
        payload = {'usuario': request.json['usuario'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
        token = encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

# Decorador para requerir autenticación JWT
def requerir_autenticacion(f):
    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'mensaje': 'Token de autenticación faltante'}), 401

        try:
            # Verifica y decodifica el token
            payload = decode(token, SECRET_KEY, algorithms=['HS256'])
            # Agrega el usuario al contexto de la solicitud
            request.usuario = payload['usuario']
        except:
            return jsonify({'mensaje': 'Token de autenticación inválido'}), 401

        # Llama a la función original con el usuario autenticado
        return f(*args, **kwargs)
    
    # Cambia el nombre de la función decorada por conveniencia en depuración
    decorador.__name__ = f.__name__
    return decorador

# Ruta protegida que requiere autenticación mediante JWT
@app.route('/recurso_protegido', methods=['GET'])
@requerir_autenticacion
def recurso_protegido():
    return jsonify({'mensaje': 'Bienvenido, {}! Este es un recurso protegido.'.format(request.usuario)})

if __name__ == '__main__':
    app.run(debug=True)

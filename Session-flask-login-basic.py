from flask import Flask, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'anyel_ec'

# Datos de usuario de ejemplo (se deben almacenar de manera segura en un entorno de producción)
usuarios = {
    'usuario1': {'password': 'contraseña1'},
    'usuario2': {'password': 'contraseña2'}
}

def verificar_credenciales(usuario, contraseña):
    """Verifica las credenciales del usuario."""
    if usuario in usuarios and usuarios[usuario]['password'] == contraseña:
        return True
    return False

@app.route('/login', methods=['POST'])
def login():
    """Ruta para iniciar sesión."""
    datos = request.get_json()

    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    if verificar_credenciales(usuario, contraseña):
        # Inicia sesión y devuelve un mensaje de éxito
        session['usuario'] = usuario
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Ruta para cerrar sesión."""
    # Cierra la sesión y devuelve un mensaje de éxito
    session.pop('usuario', None)
    return jsonify({'mensaje': 'Cierre de sesión exitoso'}), 200

@app.route('/perfil', methods=['GET'])
def obtener_perfil():
    """Ruta para obtener el perfil del usuario."""
    usuario_actual = session.get('usuario')
    
    if usuario_actual:
        return jsonify({'usuario': usuario_actual}), 200
    else:
        return jsonify({'error': 'No hay sesión activa'}), 401

if __name__ == '__main__':
    app.run(debug=True)

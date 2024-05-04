import jwt
from datetime import datetime, timedelta

# Definir la clave secreta para firmar el token
SECRET_KEY = 'tu_clave_secreta'

# Función para generar un token JWT con una duración de 10 minutos
def generar_token():
    # Definir la fecha y hora de emisión del token
    ahora = datetime.utcnow()
    # Definir la fecha y hora de expiración del token (10 minutos después)
    expiracion = ahora + timedelta(minutes=10)
    
    # Crear los datos a incluir en el token (puedes agregar más datos si lo necesitas)
    datos_token = {
        'usuario_id': 1234567890,
        'exp': expiracion
    }
    
    # Generar el token JWT usando PyJWT
    token = jwt.encode(datos_token, SECRET_KEY, algorithm='HS256')
    
    return token

# Ejemplo de cómo usar la función para generar un token
token_generado = generar_token()
print("Token JWT generado:", token_generado)

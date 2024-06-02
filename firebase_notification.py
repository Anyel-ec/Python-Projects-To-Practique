import firebase_admin
from firebase_admin import credentials, messaging

# Inicializa la app de Firebase con el archivo JSON de tu cuenta de servicio
cred = credentials.Certificate("ruta/al/archivo/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def enviar_notificacion(token, titulo, cuerpo):
    # Construye el mensaje
    message = messaging.Message(
        notification=messaging.Notification(
            title=titulo,
            body=cuerpo,
        ),
        token=token,
    )

    # Envía el mensaje
    response = messaging.send(message)
    print('Mensaje enviado:', response)

# Reemplaza estos valores con los datos de tu cliente
token = 'DEVICE_REGISTRATION_TOKEN'
titulo = 'Título de la Notificación'
cuerpo = 'Este es el cuerpo de la notificación'

# Envía la notificación
enviar_notificacion(token, titulo, cuerpo)

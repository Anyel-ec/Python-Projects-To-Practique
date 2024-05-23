import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configura los detalles del servidor SMTP de Google
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # El puerto de TLS para Gmail

# Tu dirección de correo electrónico y contraseña
email_address = 'tucorreo@gmail.com'
password = 'tucontraseña'

# La dirección de correo electrónico del destinatario
recipient_email = 'destinatario@example.com'

# Crea el mensaje
message = MIMEMultipart()
message['From'] = email_address
message['To'] = recipient_email
message['Subject'] = '¡Hola desde Python!'

# El cuerpo del correo electrónico
body = 'Este es un correo electrónico enviado desde Python usando SMTP.'
message.attach(MIMEText(body, 'plain'))

# Inicia una conexión SMTP con el servidor de Google
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Inicia el modo TLS (Transport Layer Security)
    server.starttls()
    
    # Inicia sesión en tu cuenta de Google
    server.login(email_address, password)
    
    # Envía el mensaje
    server.send_message(message)

print('Correo electrónico enviado exitosamente.')

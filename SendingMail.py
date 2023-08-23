import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración
smtp_server = 'smtp.example.com'  # Cambia esto al servidor SMTP que estés utilizando
smtp_port = 587  # Puerto para conexión TLS (puede variar según el proveedor)

sender_email = 'tu_correo@example.com'
sender_password = 'tu_contraseña'
receiver_email = 'destinatario@example.com'

subject = 'Asunto del correo'
message = 'Hola, esto es un ejemplo de correo electrónico enviado desde Python.'

# Crear objeto de mensaje MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Establecer conexión SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Iniciar conexión TLS
    server.login(sender_email, sender_password)  # Iniciar sesión

    # Enviar correo electrónico
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Correo electrónico enviado correctamente.")

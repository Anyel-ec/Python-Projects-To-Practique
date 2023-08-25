import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de los datos del remitente
remitente = 'tu_correo@gmail.com'
password = 'tu_contraseña'

# Datos del destinatario
destinatario = 'appatino@espe.edu.ec'

# Crear el objeto del correo
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = 'Asunto del correo'

# Cuerpo del correo
cuerpo = 'Hola, este es un correo de prueba enviado desde Python.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Conectar al servidor de correo de Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Iniciar sesión en el servidor
server.login(remitente, password)

# Enviar el correo
texto_del_correo = mensaje.as_string()
server.sendmail(remitente, destinatario, texto_del_correo)

# Cerrar la conexión
server.quit()

print("Correo enviado exitosamente.")

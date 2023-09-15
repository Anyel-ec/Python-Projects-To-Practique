import pywhatkit as kit

# Número de teléfono (debe incluir el código de país, por ejemplo, +1 para Estados Unidos)
numero_destino = "+1234567890"

# Mensaje a enviar
mensaje = "Hola, este es un mensaje desde Python."

# Hora en formato de 24 horas (por ejemplo, 15:30 para las 3:30 PM)
hora_envio = 15
minuto_envio = 30

# Enviar el mensaje
kit.sendwhatmsg(numero_destino, mensaje, hora_envio, minuto_envio)

import pika

# Establecer conexión con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Crear una cola llamada 'hello'
channel.queue_declare(queue='hello')

# Función para enviar un mensaje a la cola
def send_message(message):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(" [x] Sent '%s'" % message)

# Función para recibir un mensaje de la cola
def receive_message():
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Enviar un mensaje a la cola
send_message("Hello, RabbitMQ!")

# Recibir un mensaje de la cola
receive_message()

# Cerrar la conexión
connection.close()

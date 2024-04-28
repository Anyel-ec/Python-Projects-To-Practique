from flask import Flask, request, jsonify
import pika
import threading

app = Flask(__name__)

# Conexión con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaramos la cola
channel.queue_declare(queue='api_queue', durable=True)


def process_request(ch, method, properties, body):
    print("Received message:", body)
    # Simulamos un proceso que toma tiempo
    import time
    time.sleep(5)
    print("Request processed")
    ch.basic_ack(delivery_tag=method.delivery_tag)


@app.route('/api', methods=['POST'])
def api():
    # Enviamos el mensaje a RabbitMQ
    channel.basic_publish(exchange='',
                          routing_key='api_queue',
                          body=request.get_data(),
                          properties=pika.BasicProperties(
                              delivery_mode=2  # make message persistent
                          ))
    return jsonify({'message': 'Request received and queued'})


def start_consuming():
    channel.basic_qos(prefetch_count=3)  # Permitir solo 3 mensajes sin confirmar
    channel.basic_consume(queue='api_queue', on_message_callback=process_request)
    channel.start_consuming()


if __name__ == '__main__':
    # Iniciamos un hilo para consumir los mensajes de RabbitMQ
    threading.Thread(target=start_consuming, daemon=True).start()
    
    # Iniciamos el servidor Flask
    app.run(debug=True)

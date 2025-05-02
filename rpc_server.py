from amqpstorm import Connection
from amqpstorm import Message

def on_request(message):
    print(f"[x] Recibido: {message.body}")

    # Procesamiento simulado (ej. invertir la cadena recibida)
    response = message.body[::-1]

    response_message = Message.create(message.channel, response)
    response_message.correlation_id = message.correlation_id
    response_message.publish(routing_key=message.reply_to)

    message.ack()

connection = Connection('127.0.0.1', 'guest', 'guest')
channel = connection.channel()
channel.queue.declare('rpc_queue')

channel.basic.consume(on_request, queue='rpc_queue')

print("🟢 Esperando solicitudes RPC...")
channel.start_consuming()

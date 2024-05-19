import json
import pika
from dotenv import load_dotenv
from ProductManagement.Infrastructure.Controllers.UpdateStockOrderSentController import UpdateStockOrderSentController
import os

def callback(ch, method, properties, body):
    products = json.loads(body.decode())
    print("Mensaje recibido:", products)
    UpdateStockOrderSentController().run(products=products)

def consume_messages():
    load_dotenv()
    
    credentials = pika.PlainCredentials(username=os.getenv('PIKA_USER'), password=os.getenv('PIKA_PASSWORD'))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue="order_sent")
    channel.basic_consume(queue='order_sent', on_message_callback=callback, auto_ack=True)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Consumo de mensajes detenido por el usuario.')
        connection.close()

consume_messages()

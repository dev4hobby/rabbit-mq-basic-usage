import pika
from time import sleep

count = 0

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        virtual_host="/",
        credentials=pika.PlainCredentials("admin", "admin"),
    )
)
channel = connection.channel()

channel.queue_declare(queue="hello")
channel.basic_qos(prefetch_count=3)

while True:
    try:
        count += 1
        channel.basic_publish(
            exchange="", routing_key="hello", body=f"Hello World: {count}"
        )
        print(f" [x] Sent 'Hello World: {count}'")
        sleep(1)
    except Exception as e:
        print(e)
        break

connection.close()

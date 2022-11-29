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

channel.exchange_declare(exchange="logs", exchange_type="fanout")

while True:
    try:
        count += 1
        channel.basic_publish(
            exchange="logs", routing_key="", body=f"Hello World: {count}"
        )
        print(f" [x] Sent 'Hello World: {count}'")
        sleep(1)
    except Exception as e:
        print(e)
        break

connection.close()

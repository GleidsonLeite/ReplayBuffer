import json
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

message = json.dumps(
    {
        "action": [1, 2, 3, 4],
        "done": True,
        "episode": 0,
        "execution_id": "12345",
        "next_state": [1, 2, 3, 4],
        "reward": 0,
        "state": [1, 2, 3, 4],
        "step": 0,
    }
)
channel.basic_publish(
    exchange="",
    routing_key="create_transition",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
)
print(" [x] Sent %r" % message)
connection.close()

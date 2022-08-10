from pika import BlockingConnection, ConnectionParameters

from src.queues import CreateTransitionQueue
from src.repositories import TransitionsRepository
from src.services.CreateTransition import CreateTransitionService


if __name__ == "__main__":
    connection_parameters = ConnectionParameters(host="localhost")
    connection = BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue="create_transition", durable=True)
    channel.basic_qos(prefetch_count=1)

    transitions_repository = TransitionsRepository()
    create_transition_service = CreateTransitionService(
        transitions_repository=transitions_repository
    )
    create_transition_queue = CreateTransitionQueue(
        create_transition_service=create_transition_service
    )
    channel.basic_consume(
        queue="create_transition",
        on_message_callback=create_transition_queue.handle,
    )
    print("[*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

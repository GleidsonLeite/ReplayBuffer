import json
from pika.adapters.blocking_connection import BlockingChannel
from pika import spec
from src.services.CreateTransition import CreateTransitionService


class CreateTransitionQueue:
    def __init__(self, create_transition_service: CreateTransitionService) -> None:
        self.__create_transition_service = create_transition_service

    def handle(
        self,
        channel: BlockingChannel,
        method: spec.Basic.Deliver,
        properties: spec.BasicProperties,
        body: bytes,
    ) -> None:
        queue_body = json.loads(body)
        self.__create_transition_service.execute(
            action=queue_body["action"],
            done=queue_body["done"],
            episode=queue_body["episode"],
            execution_id=queue_body["execution_id"],
            next_state=queue_body["next_state"],
            reward=queue_body["reward"],
            state=queue_body["state"],
            step=queue_body["step"],
        )
        channel.basic_ack(delivery_tag=method.delivery_tag)

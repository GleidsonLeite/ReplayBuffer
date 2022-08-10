from flask import Request, Response, make_response
from src.services.CreateTransition import CreateTransitionService


class CreateTransitionRoute:
    def __init__(self, create_transition_service: CreateTransitionService) -> None:
        self.__create_transition_service = create_transition_service

    def handle(self, request: Request) -> Response:
        body = request.get_json()
        self.__create_transition_service.execute(
            action=body["action"],
            done=body["done"],
            episode=body["episode"],
            execution_id=body["execution_id"],
            next_state=body["next_state"],
            reward=body["reward"],
            state=body["state"],
            step=body["step"],
        )

        return make_response({}, 201)

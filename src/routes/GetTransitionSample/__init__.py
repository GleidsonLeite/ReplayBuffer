from flask import Request, Response, make_response
from src.services.GetTransitionSample import GetTransitionSampleService


class GetTransitionSampleRoute:
    def __init__(
        self, get_transition_sample_service: GetTransitionSampleService
    ) -> None:
        self.__get_transition_sample_service = get_transition_sample_service

    def handle(self, request: Request) -> Response:
        request_body = request.get_json()
        transitions = self.__get_transition_sample_service.execute(
            execution_id=request_body["execution_id"],
            number_of_samples=request_body["number_of_samples"],
        )

        return make_response(
            [transition.as_dict for transition in transitions],
            200,
        )

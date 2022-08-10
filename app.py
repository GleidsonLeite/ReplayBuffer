from flask import Flask, request, Response
from src.error import AppException

from src.repositories import TransitionsRepository
from src.routes.CreateTransition import CreateTransitionRoute
from src.routes.GetTransitionSample import GetTransitionSampleRoute
from src.services.CreateTransition import CreateTransitionService
from src.services.GetTransitionSample import GetTransitionSampleService

app = Flask(__name__)


@app.errorhandler(AppException)
def handle_app_exception(app_exception: AppException) -> Response:
    return {"message": str(app_exception)}, app_exception.error_code


@app.route("/", methods=["POST"])
def create():
    transitions_repository = TransitionsRepository()
    create_transition_service = CreateTransitionService(
        transitions_repository=transitions_repository
    )
    create_transition_route = CreateTransitionRoute(
        create_transition_service=create_transition_service
    )

    return create_transition_route.handle(request)


@app.route("/sample", methods=["POST"])
def get_transition_sample():
    transitions_repository = TransitionsRepository()
    get_transition_sample_service = GetTransitionSampleService(
        transitions_repository=transitions_repository
    )
    get_transition_sample_route = GetTransitionSampleRoute(
        get_transition_sample_service=get_transition_sample_service
    )
    return get_transition_sample_route.handle(request)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

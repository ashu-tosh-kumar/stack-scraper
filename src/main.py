import logging

from flask import Flask, Response, make_response

from src.apis.question_no import stackoverflow_blueprint
from src.constants import api_constants
from src.domain_models import domain_enums

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """Creates, sets and returns a Flask app

    Returns:
        Flask: Returns a Flask app
    """
    app = Flask(__name__)
    app.register_blueprint(stackoverflow_blueprint)
    return app


app = create_app()


@app.get("/health")
def get_health() -> Response:
    """Base end point for health checkup

    Returns:
        Response: Returns response object
    """
    logger.debug(f"Health API hit. Returning response: {api_constants.HEALTH_RESPONSE}")

    return make_response({"status": domain_enums.ResponseStatus.SUCCESS.value, "message": api_constants.HEALTH_RESPONSE}, 200)


if __name__ == "__main__":
    app.run()

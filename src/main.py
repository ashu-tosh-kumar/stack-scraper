import logging

from flask import Flask, Response, make_response

from src.apis.question_no import stackoverflow_blueprint
from src.constants import api_constants
from src.domain_models import domain_enums

app = Flask(__name__)
app.register_blueprint(stackoverflow_blueprint)
logger = logging.getLogger(__name__)


@app.get("/health")
def get_health() -> Response:
    """Base end point for health checkup

    Returns:
        Response: Returns response object
    """
    logger.debug(f"Health API hit. Returning response: {api_constants.HEALTH_RESPONSE}")

    return make_response({"status": domain_enums.ResponseStatus.SUCCESS.value, "message": api_constants.HEALTH_RESPONSE}, 200)

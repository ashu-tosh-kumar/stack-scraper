from src import initializer
from src.constants import api_constants

app = initializer.app
logger = initializer.logger


@app.get("/health")
def get_health() -> tuple[dict, int]:
    """Base end point for health checkup

    Returns:
        tuple[dict, int]: Returns response and status code
    """
    logger.debug(f"Health API hit. Returning response: {api_constants.HEALTH_RESPONSE}")

    return api_constants.HEALTH_RESPONSE, 200

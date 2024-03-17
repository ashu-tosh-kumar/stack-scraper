import logging

from flask import Blueprint, Response, make_response
from markupsafe import escape

from src.db_wrappers.in_memory_db import db
from src.domain_models import domain_enums
from src.external_sources import scrapper_tasks

logger = logging.getLogger(__name__)
stackoverflow_blueprint = Blueprint("stackoverflow_blueprint", __name__)


@stackoverflow_blueprint.route("/stackoverflow", methods=["POST"])
def run_scrappers() -> Response:
    """This REST end point is only exposed for testing to let users trigger the scrapper
    else we won't need it in production as we would have scrappers running based on
    schedules

    Returns:
        Response: Returns response object
    """
    logger.info("End point hit: run_scrappers")

    try:
        scrapper_tasks.run_all_scrappers()
    except Exception:
        logger.exception("Error in running scrappers")
        return make_response({"status": domain_enums.ResponseStatus.ERROR.value}, 500)

    return make_response({"status": domain_enums.ResponseStatus.SUCCESS.value}, 200)


@stackoverflow_blueprint.route("/stackoverflow/<ques_no>", methods=["GET"])
def get_question_answer(ques_no: int) -> Response:
    """Function to fetch data for given question number

    Args:
        ques_no (int): Question number

    Returns:
        Response: Returns response object
    """
    logger.info("End point hit: get_question_answer")

    try:
        ques_no = int(ques_no)
    except ValueError:
        msg = f"Invalid question number: {ques_no}. ques_no should be an integer"
        logger.info(msg)
        return make_response({"status": domain_enums.ResponseStatus.ERROR.value, "message": escape(msg)}, 400)

    try:
        question_answer = db.get_question_answer_by_ques_no(ques_no=ques_no)
    except Exception:
        logger.exception("Error in fetching data from database")
        return make_response({"status": domain_enums.ResponseStatus.ERROR.value, "message": "Internal server error"}, 500)

    if question_answer:
        return make_response({"status": domain_enums.ResponseStatus.SUCCESS.value, "message": question_answer.model_dump()}, 200)
    else:
        return make_response({"status": domain_enums.ResponseStatus.SUCCESS.value, "message": "Question doesn't exist"}, 200)

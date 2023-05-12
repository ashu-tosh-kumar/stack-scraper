from src.domain_models import domain_enums
from src.external_sources import scrapper_tasks
from src.initializer import app, db, logger


@app.post("/stackoverflow")
def run_scrappers() -> tuple[dict, int]:
    """This REST end point is only exposed for testing to let users trigger the scrapper
    else we won't need it in production as we would have scrappers running based on
    schedules

    Returns:
        tuple[dict, int]: Returns response and status code
    """
    logger.info("End point hit: run_scrappers")

    scrapper_tasks.run_all_scrappers()

    return {"status": domain_enums.ResponseStatus.SUCCESS}, 200


@app.get("/stackoverflow")
def get_question_answer(ques_no: int) -> tuple[dict, int]:
    """Function to fetch data for given question number

    Args:
        ques_no (int): Question number

    Returns:
        tuple[dict, int]: Returns response and status code
    """
    logger.info("End point hit: get_question_answer")

    if not isinstance(ques_no, int):
        msg = f"Invalid question number: {ques_no}. ques_no should be an integer"
        logger.info(msg)
        return {"status": domain_enums.ResponseStatus.ERROR, "message": msg}, 400

    try:
        question_answer = db.get_question_answer_by_ques_no(ques_no=ques_no)
    except Exception:
        logger.exception("Error in fetching data from database")
        return {"status": domain_enums.ResponseStatus.ERROR, "message": "Internal server error"}, 500

    if question_answer:
        return {"status": domain_enums.ResponseStatus.SUCCESS, "message": question_answer.dict()}, 200
    else:
        return {"status": domain_enums.ResponseStatus.SUCCESS, "message": None}, 200

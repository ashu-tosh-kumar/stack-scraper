import logging
import zoneinfo
from datetime import datetime

from pydantic import validate_arguments

from src.db_wrappers import db_models

logger = logging.getLogger(__name__)


class InMemoryDatabaseWrapper:
    def __init__(self, logger) -> None:
        """Initializer for `SQLiteWrapper`

        Args:
            logger (_type_): Logger for logging
        """
        self._db: dict[str, dict] = {"stack_overflow": {}}
        self._logger = logger

        self._logger.debug("In Memory Database Initialized")

    @validate_arguments
    def upsert_question_answer(self, ques_no: int, ques_text: str, ques_comments: str | None, ans_text: str, ans_accepted: bool) -> None:
        """Creates one entry in `stack_overflow` table for given question and answer
        data

        Args:
            ques_no (int): Question number
            ques_text (str): Text of the question
            ques_comments (str | None): Comments for the given question
            ans_text (str): Text for the give answer
            ans_accepted (bool): Whether current answer is accepted or not
        """
        key = ques_no
        self._logger.info("Inserting entry into database for key: {key}")

        created = datetime.now(tz=zoneinfo.ZoneInfo("UTC"))
        self._db["stack_overflow"][key] = db_models.StackOverflowQuestionAnswer(
            ques_no=ques_no, ques_text=ques_text, ques_comments=ques_comments, ans_text=ans_text, ans_accepted=ans_accepted, created=created
        )

    @validate_arguments
    def get_question_answer_by_ques_no(self, ques_no: int) -> db_models.StackOverflowQuestionAnswer | None:
        """Fetches and returns the entry from database by question no

        Args:
            ques_no (int): Question number

        Returns:
            db_models.StackOverflow: Returns entry, if any, from database in db model
            format
        """
        self._logger.info("Reading entry from database for key: {key}")

        return self._db["stack_overflow"].get(ques_no)


db = InMemoryDatabaseWrapper(logger)

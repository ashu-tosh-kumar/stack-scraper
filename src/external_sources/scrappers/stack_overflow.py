import requests
from bs4 import BeautifulSoup

from src.constants import mock_data
from src.db_wrappers.in_memory_db import db
from src.domain_models import domain_models
from src.external_sources.external_source_base import ExternalSource
from src.initializer import logger


class StackOverflowException(Exception):
    """Raised if any exception in `StackOverflow`"""

    pass


class StackOverflow(ExternalSource):
    """Scrapper for StackOverflow"""

    def __init__(self) -> None:
        self._target_url = "https://stackoverflow.com/"

        logger.debug("Initialized the StackOverflow Scrapper")

    def _fetch_page(self, target_url: str) -> bytes:
        """Fetches the page of the given url `target_url` using GET HTTP call

        Args:
            target_url (str): Target url that needs to be fetched

        Returns:
            bytes: Returns the page content of the `target_url`
        """
        logger.info(f"fetching page {target_url}")
        page = requests.get(target_url)

        if page.status_code != 200:
            error_msg: str = f"Received non 200 status code in fetching {target_url}"
            logger.exception(error_msg)
            raise StackOverflowException(error_msg)

        return page.content

    def _make_soup(self, bytes_content: bytes) -> BeautifulSoup:
        """Creates a Beautiful soup for the given page content

        Args:
            bytes_content (bytes): Page content for which soup needs to be created

        Returns:
            BeautifulSoup: Returns Beautiful soup for given page content `bytes_content`
        """
        logger.info("Making soup out of bytes content")
        logger.debug(f"Making soup out of bytes content: {bytes_content}")
        soup = BeautifulSoup(bytes_content, "html.parser")

        return soup

    def _parse_page(self, soup: BeautifulSoup) -> list[tuple[domain_models.StackOverflowQuestion, domain_models.StackOverflowAnswer]]:
        """Parses the page using the given soup `soup` and returns parsed questions and
        answers

        Args:
            soup (BeautifulSoup): Beautiful soup that needs to be parsed

        Returns:
            list[tuple[domain_models.StackOverflowQuestion,
            domain_models.StackOverflowAnswer]]: Returns a list of tuples where each
            tuple represents one question and one answer
        """
        logger.info("Parsing data out of the soup")
        logger.debug(f"Parsing data out of the soup: {soup}")
        questions_answers: list[tuple[domain_models.StackOverflowQuestion, domain_models.StackOverflowAnswer]] = []

        # NOTE: Core logic to parse our hypothetical StackOverflow website would come
        # here.
        logger.info(f"Parsing the soup: {soup}")

        # For the sake of understanding and example, we will use mocked data here.
        logger.info(f"Using mocked data: {mock_data.MOCK_STACK_OVERFLOW_DATA}")
        for mock_ques, mock_ans in mock_data.MOCK_STACK_OVERFLOW_DATA:
            stack_question = domain_models.StackOverflowQuestion(**mock_ques)
            stack_answer = domain_models.StackOverflowAnswer(**mock_ans)
            questions_answers.append((stack_question, stack_answer))

        return questions_answers

    def _store_into_db(self, questions_answers: list[tuple[domain_models.StackOverflowQuestion, domain_models.StackOverflowAnswer]]) -> None:
        """Stores the given list of question and answers into database

        Args:
            questions_answers (list[tuple[domain_models.StackOverflowQuestion,
            domain_models.StackOverflowAnswer]]): list of tuples where each tuple
            represents one question and one answer
        """
        logger.info("Storing the list of questions and answers into database")
        logger.debug(f"Storing the list of questions and answers into database: {questions_answers}")
        for question, answer in questions_answers:
            db.upsert_question_answer(
                ques_no=question.no, ques_text=question.text, ques_comments=question.comments, ans_text=answer.text, ans_accepted=answer.accepted
            )

    def run(self) -> None:
        """Main run method responsible for running the scrapers and storing the scraped
        data into the database
        """
        page = self._fetch_page(self._target_url)
        soup = self._make_soup(page)
        questions_answers = self._parse_page(soup)
        self._store_into_db(questions_answers)

from test.src.external_sources.scrappers.stack_overflow_page_bytes_content import (
    stack_overflow_page_bytes_content,
)
from unittest.mock import Mock

import pytest
from bs4 import BeautifulSoup

from src.domain_models.domain_models import StackOverflowAnswer, StackOverflowQuestion
from src.external_sources.scrappers.stack_overflow import (
    StackOverflow,
    StackOverflowException,
)

DUMMY_TARGET_URL = "https://unittest-url"
REQUESTS = "src.external_sources.scrappers.stack_overflow.requests"


@pytest.fixture
def stack_overflow():
    yield StackOverflow()


class TestStackOverflowException:
    def test_stack_overflow_exception_should_exist(self):
        with pytest.raises(StackOverflowException):
            raise StackOverflowException()


class TestStackOverflow:
    def test__fetch_page_should_fetch_target_url(self, mocker, stack_overflow: StackOverflow):
        stub_requests = mocker.patch(REQUESTS)
        dummy_page_data = Mock()
        dummy_page_data.status_code = 200
        dummy_page_data.content = "unittest-page-content"
        stub_requests.get.return_value = dummy_page_data

        actual_value = stack_overflow._fetch_page(DUMMY_TARGET_URL)

        assert dummy_page_data.content == actual_value

    def test__fetch_page_should_raise_exception_for_error_in_fetching_page(self, mocker, stack_overflow: StackOverflow):
        stub_requests = mocker.patch(REQUESTS)
        stub_requests.get.side_effect = Exception("unittest-requests-get-exception")

        with pytest.raises(StackOverflowException):
            stack_overflow._fetch_page(DUMMY_TARGET_URL)

    def test__fetch_page_should_raise_exception_for_non_200_page_response(self, mocker, stack_overflow: StackOverflow):
        stub_requests = mocker.patch(REQUESTS)
        dummy_page_data = Mock()
        dummy_page_data.status_code = 500
        stub_requests.get.return_value = dummy_page_data

        with pytest.raises(StackOverflowException):
            stack_overflow._fetch_page(DUMMY_TARGET_URL)

    def test__make_soup_should_make_soup(self, stack_overflow: StackOverflow):
        expected_value = BeautifulSoup(stack_overflow_page_bytes_content, "html.parser")

        actual_value = stack_overflow._make_soup(stack_overflow_page_bytes_content)

        assert expected_value == actual_value

    def test__parse_page_should_parse_page_data(self, stack_overflow: StackOverflow, snapshot):
        soup = BeautifulSoup(stack_overflow_page_bytes_content, "html.parser")

        actual_value = stack_overflow._parse_page(soup)

        assert snapshot == actual_value

    def test__store_into_db_should_store_data_in_db(self, mocker, stack_overflow: StackOverflow):
        dummy_question_data = {"no": 1, "text": "unittest-text", "comments": "unittest-comments"}
        stack_overflow_question = StackOverflowQuestion(**dummy_question_data)
        dummy_answer_data = {"text": "unittest-text", "accepted": True}
        stack_overflow_answer = StackOverflowAnswer(**dummy_answer_data)
        questions_answers = [(stack_overflow_question, stack_overflow_answer)]
        spy_db = mocker.patch("src.external_sources.scrappers.stack_overflow.db")

        stack_overflow._store_into_db(questions_answers)

        spy_db.upsert_question_answer.assert_called_once_with(
            ques_no=stack_overflow_question.no,
            ques_text=stack_overflow_question.text,
            ques_comments=stack_overflow_question.comments,
            ans_text=stack_overflow_answer.text,
            ans_accepted=stack_overflow_answer.accepted,
        )

    def test_run(self, mocker, stack_overflow: StackOverflow):
        stub__fetch_page = mocker.patch("src.external_sources.scrappers.stack_overflow.StackOverflow._fetch_page")
        stub__make_soup = mocker.patch("src.external_sources.scrappers.stack_overflow.StackOverflow._make_soup")
        stub__parse_page = mocker.patch("src.external_sources.scrappers.stack_overflow.StackOverflow._parse_page")
        spy__store_into_db = mocker.patch("src.external_sources.scrappers.stack_overflow.StackOverflow._store_into_db")

        stack_overflow.run()

        page = stub__fetch_page(stack_overflow._target_url)
        soup = stub__make_soup(page)
        questions_answers = stub__parse_page(soup)
        spy__store_into_db.assert_called_once_with(questions_answers)

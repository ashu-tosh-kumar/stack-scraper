import json
from datetime import datetime

import pytest

from src.db_wrappers import db_models

SAMPLE_STACK_OVERFLOW_QUESTION_ANSWER_DICT = {
    1: db_models.StackOverflowQuestionAnswer(
        ques_no=1, ques_text="Sample question text", ans_text="Sample answer text", ans_accepted=True, created=datetime.now()
    )
}


class TestRunScrappers:
    def test_run_scrappers_should_run_all_scrappers(self, mocker, test_client):
        spy_scrapper_tasks = mocker.patch("src.apis.question_no.scrapper_tasks")

        response = test_client.post("/stackoverflow")

        assert spy_scrapper_tasks.run_all_scrappers.called
        assert 200 == response.status_code

    def test_run_scrappers_should_return_appropriate_message_if_scrappers_fail(self, mocker, test_client):
        stub_scrapper_tasks = mocker.patch("src.apis.question_no.scrapper_tasks")
        stub_scrapper_tasks.run_all_scrappers.side_effect = Exception("unittest-scrappers-exception")

        response = test_client.post("/stackoverflow")

        assert 500 == response.status_code


class TestGetQuestionAnswer:
    @pytest.mark.parametrize(
        "question_no, expected_value",
        [
            (
                1,
                {
                    **SAMPLE_STACK_OVERFLOW_QUESTION_ANSWER_DICT.get(1).dict(),
                    "created": SAMPLE_STACK_OVERFLOW_QUESTION_ANSWER_DICT.get(1).dict()["created"].strftime("%a, %d %b %Y %H:%M:%S GMT"),
                },
            ),
            (999, "Question doesn't exist"),
            ("invalid-question-no", "Invalid question number: invalid-question-no. ques_no should be an integer"),
        ],
        ids=["valid-question", "non-existent-question-no", "invalid-question-no"],
    )
    def test_get_question_answer_should_return_expected_data(self, mocker, test_client, question_no, expected_value):
        stub_db = mocker.patch("src.apis.question_no.db")
        stub_db.get_question_answer_by_ques_no.side_effect = lambda ques_no: SAMPLE_STACK_OVERFLOW_QUESTION_ANSWER_DICT.get(ques_no)

        response = test_client.get(f"/stackoverflow/{question_no}")
        response_dict = json.loads(response.data)

        assert expected_value == response_dict["message"]

    def test_get_question_answer_should_return_appropriate_message_if_error_in_fetching(self, mocker, test_client):
        stub_db = mocker.patch("src.apis.question_no.db")
        stub_db.get_question_answer_by_ques_no.side_effect = Exception("unittest-exception-get_question_answer_by_ques_no")
        expected_value = "Internal server error"

        response = test_client.get(f"/stackoverflow/{1}")
        response_dict = json.loads(response.data)

        assert expected_value == response_dict["message"]

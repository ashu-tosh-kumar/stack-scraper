import zoneinfo
from datetime import datetime
from unittest.mock import Mock

import pytest

from src.db_wrappers import db_models
from src.db_wrappers.in_memory_db import InMemoryDatabaseWrapper


@pytest.fixture
def in_memory_db():
    yield InMemoryDatabaseWrapper(Mock())


class TestInMemoryDatabaseWrapper:
    def test_upsert_question_answer_should_upsert_correct_data(self, in_memory_db: InMemoryDatabaseWrapper):
        dummy_data = {
            "ques_no": 1,
            "ques_text": "unittest-ques_text",
            "ques_comments": "unittest-ques_comments",
            "ans_text": "unittest-ans_text",
            "ans_accepted": True,
        }

        in_memory_db.upsert_question_answer(**dummy_data)

        data_in_memory = in_memory_db._db["stack_overflow"][dummy_data["ques_no"]]
        assert data_in_memory.ques_no == dummy_data["ques_no"]
        assert data_in_memory.ques_text == dummy_data["ques_text"]
        assert data_in_memory.ques_comments == dummy_data["ques_comments"]
        assert data_in_memory.ans_text == dummy_data["ans_text"]
        assert data_in_memory.ans_accepted == dummy_data["ans_accepted"]

    def test_get_question_answer_by_ques_no_should_return_expected_data(self, in_memory_db: InMemoryDatabaseWrapper):
        dummy_data = {
            "ques_no": 1,
            "ques_text": "unittest-ques_text",
            "ques_comments": "unittest-ques_comments",
            "ans_text": "unittest-ans_text",
            "ans_accepted": True,
            "created": datetime.now(tz=zoneinfo.ZoneInfo("UTC")),
        }
        in_memory_db._db["stack_overflow"][1] = db_models.StackOverflowQuestionAnswer(**dummy_data)

        actual_value = in_memory_db.get_question_answer_by_ques_no(dummy_data["ques_no"])

        assert dummy_data["ques_no"] == actual_value.ques_no
        assert dummy_data["ques_text"] == actual_value.ques_text
        assert dummy_data["ques_comments"] == actual_value.ques_comments
        assert dummy_data["ans_text"] == actual_value.ans_text
        assert dummy_data["ans_accepted"] == actual_value.ans_accepted
        assert dummy_data["created"] == actual_value.created

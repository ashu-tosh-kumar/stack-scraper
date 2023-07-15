from datetime import datetime

from src.db_wrappers.db_models import StackOverflowQuestionAnswer


class TestStackOverflowQuestionAnswer:
    def test_stack_overflow_question_answer_model(self):
        dummy_data = {
            "ques_no": 1,
            "ques_text": "unittest-ques_text",
            "ques_comments": "unittest-ques_comments",
            "ans_text": "unittest-ans_text",
            "ans_accepted": True,
            "created": datetime.now(),
        }

        stack_overflow_model = StackOverflowQuestionAnswer(**dummy_data)

        assert stack_overflow_model.ques_no == dummy_data["ques_no"]
        assert stack_overflow_model.ques_text == dummy_data["ques_text"]
        assert stack_overflow_model.ques_comments == dummy_data["ques_comments"]
        assert stack_overflow_model.ans_text == dummy_data["ans_text"]
        assert stack_overflow_model.ans_accepted == dummy_data["ans_accepted"]
        assert stack_overflow_model.created == dummy_data["created"]

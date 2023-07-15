from src.domain_models.domain_models import StackOverflowAnswer, StackOverflowQuestion


class TestStackOverflowQuestion:
    def test_stack_overflow_question_model(self):
        dummy_data = {"no": 1, "text": "unittest-text", "comments": "unittest-comments"}
        stack_overflow_question = StackOverflowQuestion(**dummy_data)

        assert stack_overflow_question.no == dummy_data["no"]
        assert stack_overflow_question.text == dummy_data["text"]
        assert stack_overflow_question.comments == dummy_data["comments"]


class TestStackOverflowAnswer:
    def test_stack_overflow_answer_model(self):
        dummy_data = {"text": "unittest-text", "accepted": True}
        stack_overflow_answer = StackOverflowAnswer(**dummy_data)

        assert stack_overflow_answer.text == dummy_data["text"]
        assert stack_overflow_answer.accepted == dummy_data["accepted"]

from src.constants.mock_data import MOCK_STACK_OVERFLOW_DATA


class TestMockStackOverflowData:
    def test_mock_stack_overflow_data_should_have_required_questions(self):
        expected_value = set([1, 2, 3, 4])

        question_nos = set()
        for stack_overflow_data in MOCK_STACK_OVERFLOW_DATA:
            question_nos.add(stack_overflow_data[0]["no"])

        assert expected_value == question_nos

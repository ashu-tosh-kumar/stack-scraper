from src.domain_models.domain_enums import ResponseStatus


class TestResponseStatus:
    def test_response_status_should_contain_expected_enums(self):
        assert ResponseStatus.SUCCESS
        assert ResponseStatus.ERROR

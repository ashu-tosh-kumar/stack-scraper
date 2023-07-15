import json

from flask import Flask

from src.constants import api_constants
from src.main import create_app


class TestCreateApp:
    def test_create_app_should_return_flask_app(self):
        app = create_app()

        assert isinstance(app, Flask)


class TestHealth:
    def test_health_should_return_expected_response(self, test_client):
        expected_value = api_constants.HEALTH_RESPONSE

        response = test_client.get("/health")
        response_dict = json.loads(response.data)

        assert expected_value == response_dict["message"]

"""This module aims to contain all common fixtures that can be reused across different
test modules"""

import pytest

from src.main import create_app


@pytest.fixture()
def test_app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def test_client(test_app):
    return test_app.test_client()

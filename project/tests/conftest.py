# Imports
import os
import pytest
from starlette.testclient import TestClient
# Custom Imports
from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # Set up
    main.api.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.api) as test_client:

        # Testing
        yield test_client

    # Tear down

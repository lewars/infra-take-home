import pytest
from reverse.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

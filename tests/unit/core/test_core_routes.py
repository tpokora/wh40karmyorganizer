import pytest

from wh40k import app


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home route."""
    # given
    expected_header = b'<h1>Welcome to Warhammer 40K Army Organizer!</h1>'

    # when
    response = client.get('/')

    # then
    assert response.status_code == 200
    assert expected_header in response.data

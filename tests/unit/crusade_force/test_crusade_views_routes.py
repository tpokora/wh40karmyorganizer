import pytest

from wh40k import app


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


def test_get_crusade_home(client):
    # given
    expected_crusade_home_header = b'<h1>Crusade forces</h1>'

    # when
    response = client.get('/crusades')

    # then
    assert response.status_code == 200
    assert expected_crusade_home_header in response.data

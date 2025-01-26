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


# Dice rolls
def test_dice_rolls(client):
    """Test the home route."""

    # when
    response = client.get('/dice_roll/2d6')

    # then
    assert response.status_code == 200
    assert len(response.json) == 2


def test_dice_rolls_incorrect_format(client):
    """Test the home route."""

    # when
    response = client.get('/dice_roll/xd6')

    # then
    assert response.status_code == 400

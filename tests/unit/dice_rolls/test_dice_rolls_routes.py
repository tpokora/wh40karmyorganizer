import pytest
from flask_wtf.csrf import generate_csrf

from wh40k import app


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


# Dice rolls
def test_dice_rolls(client):
    # given
    expected_form_dice_number_label = b'<label for="dice_number">Dice number</label>'
    expected_form_dice_size_label = b'<label for="dice_size">Dice size</label>'

    # when
    response = client.get('/dice_roll')

    # then
    assert response.status_code == 200
    assert expected_form_dice_number_label in response.data
    assert expected_form_dice_size_label in response.data


def test_dice_rolls_form(client):
    # given
    expected_dice_rolls_result_header = b'<h2>Dice rolls result</h2>'

    # Get CSRF token
    csrf_token = _get_csrf_token(client)

    # when
    response = client.post('/dice_roll', data={
        'dice_number': '2',
        'dice_size': '32',
        'csrf_token': csrf_token
    })

    # then
    assert response.status_code == 200
    assert expected_dice_rolls_result_header in response.data


def test_dice_rolls_form_validation_errors(client):
    # given
    expected_dice_number_validation_error = b'Dice number must be a numeric value'
    expected_dice_size_validation_error = b'Dice size must be a numeric value'

    # when
    response = client.post("dice_roll", data={
        "dice_number": "string value",
        "dice_size": "string value"
    })
    assert response.status_code == 200
    assert expected_dice_number_validation_error in response.data
    assert expected_dice_size_validation_error in response.data


def _get_csrf_token(client):
    client.get('/dice_roll')
    csrf_token = generate_csrf()
    return csrf_token

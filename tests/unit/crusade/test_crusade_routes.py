import os

import pytest

from wh40k import app


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


def test_create_crusade(client):
    """Test the crusade creation route."""
    # given
    crusade_force = "Shadow Strike 5th Company"
    faction = "Raven Guard"
    request_body = {
        "crusade_force": crusade_force,
        "faction": faction
    }
    expected_response = {
        "crusade_force": crusade_force,
        "faction": faction,
        "supply_limit": 1000,
        "supply_used": 0
    }

    # when
    response = client.post('/crusade', json=request_body)

    # then
    assert response.status_code == 201
    assert response.json == expected_response
    __remove_file(crusade_force)


def test_get_all_crusades_returns_list(client):
    """Test the get all crusades route. Should return crusade list"""
    # given
    crusade_force = "Shadow Strike 5th Company"
    faction = "Raven Guard"
    request_body = {
        "crusade_force": crusade_force,
        "faction": faction
    }
    expected_response = {
        "crusade_force": crusade_force,
        "faction": faction,
        "supply_limit": 1000,
        "supply_used": 0
    }
    client.post('/crusade', json=request_body)

    # when
    response = client.get('/crusade')

    # then
    assert response.status_code == 200
    assert len(response.json) != 0
    assert expected_response in response.json
    __remove_file(crusade_force)


def test_create_crusade_returns_error_for_missing_crusade_force(client):
    """Test the get all crusades route. Should return error if crusade_force is missing"""
    # given
    request_body = {
        "faction": "faction"
    }
    expected_response = {
        "error": "Missing 'crusade_force' in request body"
    }

    # when
    response = client.post('/crusade', json=request_body)
    assert response.status_code == 400
    assert expected_response == response.json


def test_create_crusade_returns_error_for_missing_faction(client):
    """Test the get all crusades route. Should return error if faction is missing"""
    # given
    request_body = {
        "crusade_force": "crusade_force",
    }
    expected_response = {
        "error": "Missing 'faction' in request body"
    }

    # when
    response = client.post('/crusade', json=request_body)

    # then
    assert response.status_code == 400
    assert expected_response == response.json


# Import crusade forces tests
def test_import_all_crusade_forces(client):
    """JSON array should save crusade forces"""
    # given
    request_body = [{
        "crusade_force": "crusade_force1",
        "faction": "faction1",
        "supply_limit": 1000,
        "supply_used": 0
    }, {
        "crusade_force": "crusade_force2",
        "faction": "faction1",
        "supply_limit": 1000,
        "supply_used": 0
    }]

    expected_response = [{
        "crusade_force": "crusade_force1",
        "faction": "faction1",
        "supply_limit": 1000,
        "supply_used": 0
    }, {
        "crusade_force": "crusade_force2",
        "faction": "faction1",
        "supply_limit": 1000,
        "supply_used": 0
    }]

    # when
    response = client.post('/crusade/import', json=request_body)

    # then
    assert response.status_code == 201
    assert expected_response == response.json
    __remove_file("crusade_force1")
    __remove_file("crusade_force2")


def test_import_all_crusade_forces_with_invalid_crusade_force_return_status_code_400(client):
    """JSON array with invalid crusade force should 400 status code"""
    # given
    request_body = [{
        "faction": "faction1",
        "supply_limit": 1000,
        "supply_used": 0
    }]

    expected_response = {
        "error": "Missing 'crusade_force' in request body"
    }

    # when
    response = client.post('/crusade/import', json=request_body)

    # then
    assert response.status_code == 400
    assert expected_response == response.json


def __remove_file(file_name: str):
    os.remove(f'storage/{file_name.replace(" ", "_")}.json')

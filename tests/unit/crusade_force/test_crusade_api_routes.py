from tests.unit.crusade_force.db_test import DatabaseTest


class CrusadeAPI(DatabaseTest):
    def setUp(self):
        super().setUp()
        self.client = self.app.test_client()

    def tearDown(self):
        super().tearDown()

    def test_create_crusade(self):
        # given
        crusade_force = "test_create_crusade"
        faction = "Raven Guard"
        request_body = {
            "crusade_force": crusade_force,
            "faction": faction
        }
        expected_response = {
            "crusade_force": crusade_force,
            "crusade_id": 1,
            "faction": faction,
            "supply_limit": 1000,
            "supply_used": 0
        }

        # when
        response = self.client.post('/api/crusade', json=request_body)

        # then
        assert response.status_code == 201
        assert response.json == expected_response

    def test_get_crusade_by_id_should_return(self):
        # given
        crusade_force = "test_create_crusade_by_id"
        faction = "Raven Guard"
        request_body = {
            "crusade_force": crusade_force,
            "faction": faction
        }
        crusade_id = 1
        expected_response = {
            "crusade_force": crusade_force,
            "crusade_id": crusade_id,
            "faction": faction,
            "supply_limit": 1000,
            "supply_used": 0
        }
        self.client.post('/api/crusade', json=request_body)

        # when
        response = self.client.get(f'/api/crusade/{crusade_id}')

        # then
        assert response.status_code == 200
        assert response.json == expected_response

    def test_get_crusade_by_id_should_exception_when_crusade_not_exist(self):
        # given
        crusade_id = 1
        expected_response = {
            "error": f"Crusade force with id '{crusade_id}' does not exist"
        }

        # when
        response = self.client.get(f'/api/crusade/{crusade_id}')

        # then
        assert response.status_code == 400
        assert response.json == expected_response

    def test_get_all_crusades_returns_list(self):
        # given
        crusade_force = "test_get_all_crusades_returns_list"
        crusade_id = 1
        faction = "Raven Guard"
        request_body = {
            "crusade_force": crusade_force,
            "faction": faction
        }
        expected_response = {
            "crusade_force": crusade_force,
            "crusade_id": crusade_id,
            "faction": faction,
            "supply_limit": 1000,
            "supply_used": 0
        }
        self.client.post('/api/crusade', json=request_body)

        # when
        response = self.client.get('/api/crusade')

        # then
        assert response.status_code == 200
        assert len(response.json) != 0
        assert expected_response in response.json

    def test_create_crusade_returns_error_for_missing_crusade_force(self):
        # given
        request_body = {
            "faction": "faction"
        }
        expected_response = {
            "error": "Missing 'crusade_force' in request body"
        }

        # when
        response = self.client.post('/api/crusade', json=request_body)
        assert response.status_code == 400
        assert expected_response == response.json

    def test_create_crusade_returns_error_for_missing_faction(self):
        # given
        request_body = {
            "crusade_force": "crusade_force",
        }
        expected_response = {
            "error": "Missing 'faction' in request body"
        }

        # when
        response = self.client.post('/api/crusade', json=request_body)

        # then
        assert response.status_code == 400
        assert expected_response == response.json

    def test_create_crusade_returns_error_when_crusade_force_already_exist_with_the_same_name(self):
        # given
        crusade_force = "Test Crusade Force"
        faction = "Raven Guard"
        request_body = {
            "crusade_force": crusade_force,
            "faction": faction
        }
        self.client.post('/api/crusade', json=request_body)

        expected_response = {
            "error": f"Crusade force '{crusade_force}' exists"
        }

        # when
        response = self.client.post('/api/crusade', json=request_body)

        # then
        assert response.status_code == 400
        assert expected_response == response.json

    def test_get_all_crusades_by_name_returns_list(self):
        # given
        crusade_force1 = "crusade_to_find"
        faction = "Raven Guard"
        request_body_first = {
            "crusade_force": crusade_force1,
            "faction": faction
        }
        crusade_force2 = "should_not_be_found"
        request_body_second = {
            "crusade_force": crusade_force2,
            "faction": faction
        }
        self.client.post('/api/crusade', json=request_body_first)
        self.client.post('/api/crusade', json=request_body_second)

        expected_response = [{
            "crusade_force": crusade_force1,
            "crusade_id": 1,
            "faction": faction,
            "supply_limit": 1000,
            "supply_used": 0
        }]

        # when
        response = self.client.get('/api/crusade/find/find')

        # then
        assert response.status_code == 200
        assert len(response.json) != 0
        assert expected_response == response.json


# Import crusade forces tests
class CrusadeImportAPI(DatabaseTest):
    def setUp(self):
        super().setUp()
        self.client = self.app.test_client()

    def tearDown(self):
        super().tearDown()

    def test_import_all_crusade_forces(self):
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

        crusade1_id = 1
        crusade2_id = 2
        expected_response = [{
            "crusade_force": "crusade_force1",
            "crusade_id": crusade1_id,
            "faction": "faction1",
            "supply_limit": 1000,
            "supply_used": 0
        }, {
            "crusade_force": "crusade_force2",
            "crusade_id": crusade2_id,
            "faction": "faction1",
            "supply_limit": 1000,
            "supply_used": 0
        }]

        # when
        response = self.client.post('/api/crusade/import', json=request_body)

        # then
        assert response.status_code == 201
        assert [element for element in expected_response if element in response.json]

    def test_import_all_crusade_forces_with_invalid_crusade_force_return_status_code_400(self):
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
        response = self.client.post('/api/crusade/import', json=request_body)

        # then
        assert response.status_code == 400
        assert expected_response == response.json

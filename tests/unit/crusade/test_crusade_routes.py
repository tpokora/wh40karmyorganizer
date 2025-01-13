from unittest.mock import patch

from app import FileHandler
from tests.unit.core.test_file_handler import FileStorageTest
from wh40k import app


class CrusadeAPI(FileStorageTest):
    def setUp(self):
        super().setUp()
        self.client = app.test_client()

    def tearDown(self):
        self.client = None

    def test_create_crusade(self):
        """Test the crusade creation route."""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            crusade_force = "Test Crusade Force"
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
            response = self.client.post('/crusade', json=request_body)

            # then
            assert response.status_code == 201
            assert response.json == expected_response
            self.remove_file(crusade_force)

    def test_get_all_crusades_returns_list(self):
        """Test the get all crusades route. Should return crusade list"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            crusade_force = "Test Crusade Force"
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
            self.client.post('/crusade', json=request_body)

            # when
            response = self.client.get('/crusade')

            # then
            assert response.status_code == 200
            assert len(response.json) != 0
            assert expected_response in response.json
            self.remove_file(crusade_force)

    def test_create_crusade_returns_error_for_missing_crusade_force(self):
        """Test the get all crusades route. Should return error if crusade_force is missing"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            request_body = {
                "faction": "faction"
            }
            expected_response = {
                "error": "Missing 'crusade_force' in request body"
            }

            # when
            response = self.client.post('/crusade', json=request_body)
            assert response.status_code == 400
            assert expected_response == response.json

    def test_create_crusade_returns_error_for_missing_faction(self):
        """Test the get all crusades route. Should return error if faction is missing"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            request_body = {
                "crusade_force": "crusade_force",
            }
            expected_response = {
                "error": "Missing 'faction' in request body"
            }

            # when
            response = self.client.post('/crusade', json=request_body)

            # then
            assert response.status_code == 400
            assert expected_response == response.json

    def test_create_crusade_returns_error_when_crusade_force_already_exist_with_the_same_name(self):
        """Test the save crusade route. Should return 400 status code when crusade with the same name already exists"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            crusade_force = "Test Crusade Force"
            faction = "Raven Guard"
            request_body = {
                "crusade_force": crusade_force,
                "faction": faction
            }
            self.client.post('/crusade', json=request_body)

            expected_response = {
                "error": f"Crusade force '{crusade_force}' exists"
            }

            # when
            response = self.client.post('/crusade', json=request_body)

            # then
            assert response.status_code == 400
            assert expected_response == response.json
            self.remove_file(crusade_force)


# Import crusade forces tests
class CrusadeImportAPI(FileStorageTest):
    def setUp(self):
        super().setUp()
        self.client = app.test_client()

    def tearDown(self):
        self.client = None

    def test_import_all_crusade_forces(self):
        """JSON array should save crusade forces"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
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
            response = self.client.post('/crusade/import', json=request_body)

            # then
            assert response.status_code == 201
            assert expected_response == response.json
            self.remove_file("crusade_force1")
            self.remove_file("crusade_force2")

    def test_import_all_crusade_forces_with_invalid_crusade_force_return_status_code_400(self):
        """JSON array with invalid crusade force should 400 status code"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
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
            response = self.client.post('/crusade/import', json=request_body)

            # then
            assert response.status_code == 400
            assert expected_response == response.json

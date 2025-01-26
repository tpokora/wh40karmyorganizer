import hashlib

from unittest.mock import patch

from app import FileHandler
from tests.unit.core.test_file_handler import FileStorageTest
from wh40k import app


class CrusadeTestHelper:
    @staticmethod
    def get_crusade_id(crusade_force):
        return hashlib.md5(crusade_force.encode('utf-8')).hexdigest()


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
            crusade_force = "test_create_crusade"
            faction = "Raven Guard"
            request_body = {
                "crusade_force": crusade_force,
                "faction": faction
            }
            crusade_id = CrusadeTestHelper.get_crusade_id(crusade_force)
            expected_response = {
                "crusade_force": crusade_force,
                "crusade_id": crusade_id,
                "faction": faction,
                "supply_limit": 1000,
                "supply_used": 0
            }

            # when
            response = self.client.post('/crusade', json=request_body)

            # then
            assert response.status_code == 201
            assert response.json == expected_response
            self.remove_file(crusade_id)

    def test_get_crusade_by_id_should_return(self):
        """Test the get crusade force by id route."""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            crusade_force = "test_create_crusade_by_id"
            faction = "Raven Guard"
            request_body = {
                "crusade_force": crusade_force,
                "faction": faction
            }
            crusade_id = CrusadeTestHelper.get_crusade_id(crusade_force)
            expected_response = {
                "crusade_force": crusade_force,
                "crusade_id": crusade_id,
                "faction": faction,
                "supply_limit": 1000,
                "supply_used": 0
            }
            self.client.post('/crusade', json=request_body)

            # when
            response = self.client.get(f'/crusade/{crusade_id}')

            # then
            assert response.status_code == 200
            assert response.json == expected_response
            self.remove_file(crusade_id)

    def test_get_crusade_by_id_should_exception_when_crusade_not_exist(self):
        """Test the get crusade force by idroute."""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path

            # given
            expected_response = {
                "error": "Crusade force with id not_existing_crusade does not exist"
            }

            # when
            response = self.client.get('/crusade/not_existing_crusade')

            # then
            assert response.status_code == 400
            assert response.json == expected_response

    def test_get_all_crusades_returns_list(self):
        """Test the get all crusades route. Should return crusade list"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            crusade_force = "test_get_all_crusades_returns_list"
            faction = "Raven Guard"
            request_body = {
                "crusade_force": crusade_force,
                "faction": faction
            }
            crusade_id = CrusadeTestHelper.get_crusade_id(crusade_force)
            expected_response = {
                "crusade_force": crusade_force,
                "crusade_id": crusade_id,
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
            self.remove_file(crusade_id)

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
            crusade_id = CrusadeTestHelper.get_crusade_id(crusade_force)
            self.client.post('/crusade', json=request_body)

            expected_response = {
                "error": f"Crusade force '{crusade_force}' exists"
            }

            # when
            response = self.client.post('/crusade', json=request_body)

            # then
            assert response.status_code == 400
            assert expected_response == response.json
            self.remove_file(crusade_id)

    def test_get_all_crusades_by_name_returns_list(self):
        """Test the get all crusades by name route. Should return crusade list"""
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
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
            self.client.post('/crusade', json=request_body_first)
            self.client.post('/crusade', json=request_body_second)

            expected_response = [{
                "crusade_force": crusade_force1,
                "crusade_id": CrusadeTestHelper.get_crusade_id(crusade_force1),
                "faction": faction,
                "supply_limit": 1000,
                "supply_used": 0
            }]

            # when
            response = self.client.get('/crusade/find/find')

            # then
            assert response.status_code == 200
            assert len(response.json) != 0
            assert expected_response == response.json
            self.remove_file(CrusadeTestHelper.get_crusade_id(crusade_force1))
            self.remove_file(CrusadeTestHelper.get_crusade_id(crusade_force2))


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

            crusade1_id = CrusadeTestHelper.get_crusade_id("crusade_force1")
            crusade2_id = CrusadeTestHelper.get_crusade_id("crusade_force2")
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
            response = self.client.post('/crusade/import', json=request_body)

            # then
            assert response.status_code == 201
            assert [element for element in expected_response if element in response.json]
            self.remove_file(crusade1_id)
            self.remove_file(crusade2_id)

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

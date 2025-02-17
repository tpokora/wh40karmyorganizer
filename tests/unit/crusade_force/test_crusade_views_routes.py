from unittest.mock import patch

from app import Crusade
from app.crusade_force.crusade import CrusadeService
from tests.unit.crusade_force.db_test import DatabaseTest


class CrusadeViews(DatabaseTest):
    def setUp(self):
        super().setUp()
        self.client = self.app.test_client()

    def tearDown(self):
        super().tearDown()

    @patch.object(CrusadeService, 'get_by_id')
    def test_crusade_force_detail_with_valid_crusade(self, mock_get_by_id):
        # given
        crusade_id = '1'
        crusade = Crusade(crusade_id=1, crusade_force='Test Force', faction='Test Faction', supply_limit=1000, supply_used=200)
        mock_get_by_id.return_value = crusade
        expected_template = 'crusade_force/crusade_detail.html'

        # when
        response = self.client.get(f'/crusades/{crusade_id}')

        # then
        assert response.status_code == 200
        self.assert_template_used(expected_template)
        assert b'Test Force' in response.data
        assert b'Faction: Test Faction' in response.data
        assert b'Supply Limit: 1000' in response.data
        assert b'Supply Used: 200' in response.data

    @patch.object(CrusadeService, 'get_all')
    def test_crusade_forces_home_with_empty_list(self, mock_get_all):
        # given
        mock_get_all.return_value = []
        expected_crusade_home_header = b'<h1>Crusade forces</h1>'

        # when
        response = self.client.get('/crusades')

        # then
        assert response.status_code == 200
        assert expected_crusade_home_header in response.data
        assert b'No crusade forces found' in response.data

    @patch.object(CrusadeService, 'get_all')
    def test_crusade_forces_home_with_list(self, mock_get_all):
        # given
        crusade = Crusade(crusade_id=1, crusade_force='Test Force', faction='Test Faction', supply_limit=1000, supply_used=200)
        mock_get_all.return_value = [crusade]
        expected_crusade_home_header = b'<h1>Crusade forces</h1>'

        # when
        response = self.client.get('/crusades')

        # then
        assert response.status_code == 200
        assert expected_crusade_home_header in response.data
        assert b'Test Force' in response.data
        assert b'<p>Faction: Test Faction | 200/1000</p>' in response.data

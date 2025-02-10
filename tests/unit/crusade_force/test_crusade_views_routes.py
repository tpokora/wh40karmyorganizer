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
        assert b'<h3>Test Force</h3>' in response.data
        assert b'<p>Faction: Test Faction</p>' in response.data
        assert b'<p>Supply Limit: 1000</p>' in response.data
        assert b'<p>Supply Used: 200</p>' in response.data

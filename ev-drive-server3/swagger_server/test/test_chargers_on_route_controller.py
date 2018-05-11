# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.on_route import OnRoute  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChargersOnRouteController(BaseTestCase):
    """ChargersOnRouteController integration test stubs"""

    def test_chargers_on_route(self):
        """Test case for chargers_on_route

        Get a list of the chargers on route
        """
        response = self.client.open(
            '/revolution/api/chargers_on_route/{from}/{to}'.format(_from='_from_example', to='to_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

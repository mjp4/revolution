# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dist_to_charger import DistToCharger  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDistController(BaseTestCase):
    """DistController integration test stubs"""

    def test_get_dist_to_charger(self):
        """Test case for get_dist_to_charger

        Get the distance to charger
        """
        response = self.client.open(
            '/revolution/api/dist_to_charger/{lat_here}/{long_here}/{lat_there}/{long_there}'.format(lat_here='lat_here_example', long_here='long_here_example', lat_there='lat_there_example', long_there='long_there_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

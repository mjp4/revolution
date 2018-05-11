# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.charge_perc import ChargePerc  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStatusController(BaseTestCase):
    """StatusController integration test stubs"""

    def test_get_charge_perc(self):
        """Test case for get_charge_perc

        Get the charge percentage
        """
        response = self.client.open(
            '/revolution/api/charge_perc/nissan/{username}/{password}'.format(username='username_example', password='password_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

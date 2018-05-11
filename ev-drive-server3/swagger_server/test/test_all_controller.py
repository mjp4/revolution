# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.all_info import AllInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllController(BaseTestCase):
    """AllController integration test stubs"""

    def test_all_info(self):
        """Test case for all_info

        Get all the info
        """
        response = self.client.open(
            '/revolution/api/all_info/{username}/{password}/{to}'.format(username='username_example', password='password_example', to='to_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

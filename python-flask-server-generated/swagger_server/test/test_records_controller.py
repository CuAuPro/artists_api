# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.artist import Artist  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecordsController(BaseTestCase):
    """RecordsController integration test stubs"""

    def test_artists_get(self):
        """Test case for artists_get

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/artists',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artists_post(self):
        """Test case for artists_post

        
        """
        body = Artist()
        response = self.client.open(
            '/artists',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artists_username_delete(self):
        """Test case for artists_username_delete

        Delete an artist by username
        """
        response = self.client.open(
            '/artists/{username}'.format(username='username_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artists_username_get(self):
        """Test case for artists_username_get

        
        """
        response = self.client.open(
            '/artists/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artists_username_put(self):
        """Test case for artists_username_put

        Update an artist by username
        """
        body = Artist()
        response = self.client.open(
            '/artists/{username}'.format(username='username_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

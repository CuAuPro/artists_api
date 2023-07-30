# coding: utf-8

"""
    Simple API

    A simple API to illustrate OpenAPI concepts  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.records_api import RecordsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRecordsApi(unittest.TestCase):
    """RecordsApi unit test stubs"""

    def setUp(self):
        self.api = RecordsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_artists_get(self):
        """Test case for artists_get

        """
        pass

    def test_artists_post(self):
        """Test case for artists_post

        """
        pass

    def test_artists_username_delete(self):
        """Test case for artists_username_delete

        Delete an artist by username  # noqa: E501
        """
        pass

    def test_artists_username_get(self):
        """Test case for artists_username_get

        """
        pass

    def test_artists_username_put(self):
        """Test case for artists_username_put

        Update an artist by username  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    jiaozifs API

    jiaozifs HTTP API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import jiaozifs_client
from jiaozifs_client.api.list_members_api import ListMembersApi  # noqa: E501
from jiaozifs_client.rest import ApiException


class TestListMembersApi(unittest.TestCase):
    """ListMembersApi unit test stubs"""

    def setUp(self):
        self.api = ListMembersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_members(self):
        """Test case for list_members

        get list of members in repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

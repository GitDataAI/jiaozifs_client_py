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
from jiaozifs_client.api.group_api import GroupApi  # noqa: E501
from jiaozifs_client.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_repo_group(self):
        """Test case for list_repo_group

        list groups for repo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

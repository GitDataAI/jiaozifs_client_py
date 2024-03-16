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
from jiaozifs_client.api.member_api import MemberApi  # noqa: E501
from jiaozifs_client.rest import ApiException


class TestMemberApi(unittest.TestCase):
    """MemberApi unit test stubs"""

    def setUp(self):
        self.api = MemberApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invite_member(self):
        """Test case for invite_member

        invite member  # noqa: E501
        """
        pass

    def test_revoke_member(self):
        """Test case for revoke_member

        Revoke member in repository  # noqa: E501
        """
        pass

    def test_update_member_group(self):
        """Test case for update_member_group

        update member by user id and change group role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

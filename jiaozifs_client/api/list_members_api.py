# coding: utf-8

"""
    jiaozifs API

    jiaozifs HTTP API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jiaozifs_client.api_client import ApiClient


class ListMembersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_members(self, owner, repository, **kwargs):  # noqa: E501
        """get list of members in repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_members(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :return: list[Member]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_members_with_http_info(owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.list_members_with_http_info(owner, repository, **kwargs)  # noqa: E501
            return data

    def list_members_with_http_info(self, owner, repository, **kwargs):  # noqa: E501
        """get list of members in repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_members_with_http_info(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :return: list[Member]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `list_members`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `list_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Member]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
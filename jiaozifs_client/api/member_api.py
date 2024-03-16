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


class MemberApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def invite_member(self, owner, repository, user_id, group_id, **kwargs):  # noqa: E501
        """invite member  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invite_member(owner, repository, user_id, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str user_id: (required)
        :param str group_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.invite_member_with_http_info(owner, repository, user_id, group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.invite_member_with_http_info(owner, repository, user_id, group_id, **kwargs)  # noqa: E501
            return data

    def invite_member_with_http_info(self, owner, repository, user_id, group_id, **kwargs):  # noqa: E501
        """invite member  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invite_member_with_http_info(owner, repository, user_id, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str user_id: (required)
        :param str group_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'user_id', 'group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invite_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `invite_member`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `invite_member`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `invite_member`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `invite_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}/member/invite', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revoke_member(self, owner, repository, user_id, **kwargs):  # noqa: E501
        """Revoke member in repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_member(owner, repository, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revoke_member_with_http_info(owner, repository, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_member_with_http_info(owner, repository, user_id, **kwargs)  # noqa: E501
            return data

    def revoke_member_with_http_info(self, owner, repository, user_id, **kwargs):  # noqa: E501
        """Revoke member in repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_member_with_http_info(owner, repository, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `revoke_member`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `revoke_member`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `revoke_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}/member', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_member_group(self, owner, repository, user_id, group_id, **kwargs):  # noqa: E501
        """update member by user id and change group role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_member_group(owner, repository, user_id, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str user_id: (required)
        :param str group_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_member_group_with_http_info(owner, repository, user_id, group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_member_group_with_http_info(owner, repository, user_id, group_id, **kwargs)  # noqa: E501
            return data

    def update_member_group_with_http_info(self, owner, repository, user_id, group_id, **kwargs):  # noqa: E501
        """update member by user id and change group role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_member_group_with_http_info(owner, repository, user_id, group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str user_id: (required)
        :param str group_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'user_id', 'group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_member_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `update_member_group`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `update_member_group`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_member_group`")  # noqa: E501
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_member_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}/member', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
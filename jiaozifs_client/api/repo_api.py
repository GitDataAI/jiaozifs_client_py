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


class RepoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_visible(self, owner, repository, visible, **kwargs):  # noqa: E501
        """change repository visible(true for public, false for private)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_visible(owner, repository, visible, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param bool visible: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_visible_with_http_info(owner, repository, visible, **kwargs)  # noqa: E501
        else:
            (data) = self.change_visible_with_http_info(owner, repository, visible, **kwargs)  # noqa: E501
            return data

    def change_visible_with_http_info(self, owner, repository, visible, **kwargs):  # noqa: E501
        """change repository visible(true for public, false for private)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_visible_with_http_info(owner, repository, visible, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param bool visible: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'visible']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_visible" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `change_visible`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `change_visible`")  # noqa: E501
        # verify the required parameter 'visible' is set
        if ('visible' not in params or
                params['visible'] is None):
            raise ValueError("Missing the required parameter `visible` when calling `change_visible`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'visible' in params:
            query_params.append(('visible', params['visible']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}/visible', 'POST',
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

    def create_repository(self, body, **kwargs):  # noqa: E501
        """create repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_repository(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRepository body: (required)
        :return: Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_repository_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_repository_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_repository_with_http_info(self, body, **kwargs):  # noqa: E501
        """create repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_repository_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRepository body: (required)
        :return: Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/users/repos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_repository(self, owner, repository, **kwargs):  # noqa: E501
        """delete repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param bool is_clean_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_repository_with_http_info(owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_repository_with_http_info(owner, repository, **kwargs)  # noqa: E501
            return data

    def delete_repository_with_http_info(self, owner, repository, **kwargs):  # noqa: E501
        """delete repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository_with_http_info(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param bool is_clean_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'is_clean_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `delete_repository`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `delete_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'is_clean_data' in params:
            query_params.append(('is_clean_data', params['is_clean_data']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}', 'DELETE',
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

    def get_commits_in_ref(self, owner, repository, **kwargs):  # noqa: E501
        """get commits in ref  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_commits_in_ref(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param int after: return items after this value
        :param int amount: how many items to return
        :param str ref_name: ref(branch/tag) name
        :return: list[Commit]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_commits_in_ref_with_http_info(owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.get_commits_in_ref_with_http_info(owner, repository, **kwargs)  # noqa: E501
            return data

    def get_commits_in_ref_with_http_info(self, owner, repository, **kwargs):  # noqa: E501
        """get commits in ref  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_commits_in_ref_with_http_info(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param int after: return items after this value
        :param int amount: how many items to return
        :param str ref_name: ref(branch/tag) name
        :return: list[Commit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'after', 'amount', 'ref_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_commits_in_ref" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_commits_in_ref`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_commits_in_ref`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'ref_name' in params:
            query_params.append(('refName', params['ref_name']))  # noqa: E501

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
            '/repos/{owner}/{repository}/commits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Commit]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_repository(self, owner, repository, **kwargs):  # noqa: E501
        """get repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repository(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :return: Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repository_with_http_info(owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.get_repository_with_http_info(owner, repository, **kwargs)  # noqa: E501
            return data

    def get_repository_with_http_info(self, owner, repository, **kwargs):  # noqa: E501
        """get repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repository_with_http_info(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :return: Repository
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
                    " to method get_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_repository`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_repository`")  # noqa: E501

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
            '/repos/{owner}/{repository}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_public_repository(self, **kwargs):  # noqa: E501
        """list public repository in all system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_public_repository(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: return items prefixed with this value
        :param int after: return items after this value
        :param int amount: how many items to return
        :return: RepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_public_repository_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_public_repository_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_public_repository_with_http_info(self, **kwargs):  # noqa: E501
        """list public repository in all system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_public_repository_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: return items prefixed with this value
        :param int after: return items after this value
        :param int amount: how many items to return
        :return: RepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prefix', 'after', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_public_repository" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501

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
            '/repos/public', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoryList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_repository(self, owner, **kwargs):  # noqa: E501
        """list repository in specific owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repository(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str prefix: return items prefixed with this value
        :param int after: return items after this value
        :param int amount: how many items to return
        :return: RepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_repository_with_http_info(owner, **kwargs)  # noqa: E501
        else:
            (data) = self.list_repository_with_http_info(owner, **kwargs)  # noqa: E501
            return data

    def list_repository_with_http_info(self, owner, **kwargs):  # noqa: E501
        """list repository in specific owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repository_with_http_info(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str prefix: return items prefixed with this value
        :param int after: return items after this value
        :param int amount: how many items to return
        :return: RepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'prefix', 'after', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `list_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501

        query_params = []
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501

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
            '/users/{owner}/repos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoryList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_repository_of_authenticated_user(self, **kwargs):  # noqa: E501
        """list repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repository_of_authenticated_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: return items prefixed with this value
        :param int after: return items after this value
        :param int amount: how many items to return
        :return: RepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_repository_of_authenticated_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_repository_of_authenticated_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_repository_of_authenticated_user_with_http_info(self, **kwargs):  # noqa: E501
        """list repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repository_of_authenticated_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: return items prefixed with this value
        :param int after: return items after this value
        :param int amount: how many items to return
        :return: RepositoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prefix', 'after', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_repository_of_authenticated_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501

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
            '/users/repos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoryList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_repository(self, body, owner, repository, **kwargs):  # noqa: E501
        """update repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repository(body, owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateRepository body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_repository_with_http_info(body, owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.update_repository_with_http_info(body, owner, repository, **kwargs)  # noqa: E501
            return data

    def update_repository_with_http_info(self, body, owner, repository, **kwargs):  # noqa: E501
        """update repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repository_with_http_info(body, owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateRepository body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'owner', 'repository']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_repository`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `update_repository`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `update_repository`")  # noqa: E501

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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}', 'POST',
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
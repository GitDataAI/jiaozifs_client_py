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


class MergerequestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_merge_request(self, body, owner, repository, **kwargs):  # noqa: E501
        """create merge request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_merge_request(body, owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMergeRequest body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :return: MergeRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_merge_request_with_http_info(body, owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.create_merge_request_with_http_info(body, owner, repository, **kwargs)  # noqa: E501
            return data

    def create_merge_request_with_http_info(self, body, owner, repository, **kwargs):  # noqa: E501
        """create merge request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_merge_request_with_http_info(body, owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMergeRequest body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :return: MergeRequest
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
                    " to method create_merge_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_merge_request`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `create_merge_request`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `create_merge_request`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/repos/{owner}/{repository}/mergerequest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MergeRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_merge_request(self, owner, repository, mr_seq, **kwargs):  # noqa: E501
        """get merge request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_merge_request(owner, repository, mr_seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param int mr_seq: (required)
        :return: MergeRequestFullState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_merge_request_with_http_info(owner, repository, mr_seq, **kwargs)  # noqa: E501
        else:
            (data) = self.get_merge_request_with_http_info(owner, repository, mr_seq, **kwargs)  # noqa: E501
            return data

    def get_merge_request_with_http_info(self, owner, repository, mr_seq, **kwargs):  # noqa: E501
        """get merge request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_merge_request_with_http_info(owner, repository, mr_seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param int mr_seq: (required)
        :return: MergeRequestFullState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'mr_seq']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_merge_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_merge_request`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_merge_request`")  # noqa: E501
        # verify the required parameter 'mr_seq' is set
        if ('mr_seq' not in params or
                params['mr_seq'] is None):
            raise ValueError("Missing the required parameter `mr_seq` when calling `get_merge_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'mr_seq' in params:
            path_params['mrSeq'] = params['mr_seq']  # noqa: E501

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
            '/repos/{owner}/{repository}/mergerequest/{mrSeq}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MergeRequestFullState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_merge_requests(self, owner, repository, **kwargs):  # noqa: E501
        """get list of merge request in repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_merge_requests(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param int after: return items after this value
        :param int amount: how many items to return
        :param int state:
        :return: MergeRequestList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_merge_requests_with_http_info(owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.list_merge_requests_with_http_info(owner, repository, **kwargs)  # noqa: E501
            return data

    def list_merge_requests_with_http_info(self, owner, repository, **kwargs):  # noqa: E501
        """get list of merge request in repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_merge_requests_with_http_info(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param int after: return items after this value
        :param int amount: how many items to return
        :param int state:
        :return: MergeRequestList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'after', 'amount', 'state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_merge_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `list_merge_requests`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `list_merge_requests`")  # noqa: E501

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
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501

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
            '/repos/{owner}/{repository}/mergerequest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MergeRequestList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def merge(self, body, owner, repository, mr_seq, **kwargs):  # noqa: E501
        """merge a mergerequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.merge(body, owner, repository, mr_seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MergeMergeRequest body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :param int mr_seq: (required)
        :return: list[Commit]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.merge_with_http_info(body, owner, repository, mr_seq, **kwargs)  # noqa: E501
        else:
            (data) = self.merge_with_http_info(body, owner, repository, mr_seq, **kwargs)  # noqa: E501
            return data

    def merge_with_http_info(self, body, owner, repository, mr_seq, **kwargs):  # noqa: E501
        """merge a mergerequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.merge_with_http_info(body, owner, repository, mr_seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MergeMergeRequest body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :param int mr_seq: (required)
        :return: list[Commit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'owner', 'repository', 'mr_seq']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method merge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `merge`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `merge`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `merge`")  # noqa: E501
        # verify the required parameter 'mr_seq' is set
        if ('mr_seq' not in params or
                params['mr_seq'] is None):
            raise ValueError("Missing the required parameter `mr_seq` when calling `merge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'mr_seq' in params:
            path_params['mrSeq'] = params['mr_seq']  # noqa: E501

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
            '/repos/{owner}/{repository}/mergerequest/{mrSeq}/merge', 'POST',
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

    def update_merge_request(self, body, owner, repository, mr_seq, **kwargs):  # noqa: E501
        """update merge request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_merge_request(body, owner, repository, mr_seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateMergeRequest body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :param int mr_seq: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_merge_request_with_http_info(body, owner, repository, mr_seq, **kwargs)  # noqa: E501
        else:
            (data) = self.update_merge_request_with_http_info(body, owner, repository, mr_seq, **kwargs)  # noqa: E501
            return data

    def update_merge_request_with_http_info(self, body, owner, repository, mr_seq, **kwargs):  # noqa: E501
        """update merge request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_merge_request_with_http_info(body, owner, repository, mr_seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateMergeRequest body: (required)
        :param str owner: (required)
        :param str repository: (required)
        :param int mr_seq: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'owner', 'repository', 'mr_seq']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_merge_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_merge_request`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `update_merge_request`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `update_merge_request`")  # noqa: E501
        # verify the required parameter 'mr_seq' is set
        if ('mr_seq' not in params or
                params['mr_seq'] is None):
            raise ValueError("Missing the required parameter `mr_seq` when calling `update_merge_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'mr_seq' in params:
            path_params['mrSeq'] = params['mr_seq']  # noqa: E501

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
            '/repos/{owner}/{repository}/mergerequest/{mrSeq}', 'POST',
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
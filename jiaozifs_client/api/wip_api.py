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


class WipApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def commit_wip(self, owner, repository, ref_name, msg, **kwargs):  # noqa: E501
        """commit working in process to branch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commit_wip(owner, repository, ref_name, msg, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str ref_name: ref name (required)
        :param str msg: commit message (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commit_wip_with_http_info(owner, repository, ref_name, msg, **kwargs)  # noqa: E501
        else:
            (data) = self.commit_wip_with_http_info(owner, repository, ref_name, msg, **kwargs)  # noqa: E501
            return data

    def commit_wip_with_http_info(self, owner, repository, ref_name, msg, **kwargs):  # noqa: E501
        """commit working in process to branch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commit_wip_with_http_info(owner, repository, ref_name, msg, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str ref_name: ref name (required)
        :param str msg: commit message (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'ref_name', 'msg']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commit_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `commit_wip`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `commit_wip`")  # noqa: E501
        # verify the required parameter 'ref_name' is set
        if ('ref_name' not in params or
                params['ref_name'] is None):
            raise ValueError("Missing the required parameter `ref_name` when calling `commit_wip`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `commit_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'ref_name' in params:
            query_params.append(('refName', params['ref_name']))  # noqa: E501
        if 'msg' in params:
            query_params.append(('msg', params['msg']))  # noqa: E501

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
            '/wip/{owner}/{repository}/commit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wip',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_wip(self, repository, owner, ref_name, **kwargs):  # noqa: E501
        """remove working in process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wip(repository, owner, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: (required)
        :param str owner: (required)
        :param str ref_name: ref name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_wip_with_http_info(repository, owner, ref_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_wip_with_http_info(repository, owner, ref_name, **kwargs)  # noqa: E501
            return data

    def delete_wip_with_http_info(self, repository, owner, ref_name, **kwargs):  # noqa: E501
        """remove working in process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wip_with_http_info(repository, owner, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: (required)
        :param str owner: (required)
        :param str ref_name: ref name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'owner', 'ref_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `delete_wip`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `delete_wip`")  # noqa: E501
        # verify the required parameter 'ref_name' is set
        if ('ref_name' not in params or
                params['ref_name'] is None):
            raise ValueError("Missing the required parameter `ref_name` when calling `delete_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501

        query_params = []
        if 'ref_name' in params:
            query_params.append(('refName', params['ref_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/wip/{owner}/{repository}', 'DELETE',
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

    def get_wip(self, repository, owner, ref_name, **kwargs):  # noqa: E501
        """get working in process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wip(repository, owner, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: (required)
        :param str owner: (required)
        :param str ref_name: ref name (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_wip_with_http_info(repository, owner, ref_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_wip_with_http_info(repository, owner, ref_name, **kwargs)  # noqa: E501
            return data

    def get_wip_with_http_info(self, repository, owner, ref_name, **kwargs):  # noqa: E501
        """get working in process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wip_with_http_info(repository, owner, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: (required)
        :param str owner: (required)
        :param str ref_name: ref name (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'owner', 'ref_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_wip`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_wip`")  # noqa: E501
        # verify the required parameter 'ref_name' is set
        if ('ref_name' not in params or
                params['ref_name'] is None):
            raise ValueError("Missing the required parameter `ref_name` when calling `get_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501

        query_params = []
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
            '/wip/{owner}/{repository}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wip',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wip_changes(self, owner, repository, ref_name, **kwargs):  # noqa: E501
        """get working in process changes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wip_changes(owner, repository, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str ref_name: ref name (required)
        :param str path: path
        :return: list[Change]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_wip_changes_with_http_info(owner, repository, ref_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_wip_changes_with_http_info(owner, repository, ref_name, **kwargs)  # noqa: E501
            return data

    def get_wip_changes_with_http_info(self, owner, repository, ref_name, **kwargs):  # noqa: E501
        """get working in process changes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wip_changes_with_http_info(owner, repository, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :param str ref_name: ref name (required)
        :param str path: path
        :return: list[Change]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repository', 'ref_name', 'path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wip_changes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_wip_changes`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `get_wip_changes`")  # noqa: E501
        # verify the required parameter 'ref_name' is set
        if ('ref_name' not in params or
                params['ref_name'] is None):
            raise ValueError("Missing the required parameter `ref_name` when calling `get_wip_changes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501

        query_params = []
        if 'ref_name' in params:
            query_params.append(('refName', params['ref_name']))  # noqa: E501
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501

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
            '/wip/{owner}/{repository}/changes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Change]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_wip(self, owner, repository, **kwargs):  # noqa: E501
        """list wip in specific project and user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_wip(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :return: list[Wip]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_wip_with_http_info(owner, repository, **kwargs)  # noqa: E501
        else:
            (data) = self.list_wip_with_http_info(owner, repository, **kwargs)  # noqa: E501
            return data

    def list_wip_with_http_info(self, owner, repository, **kwargs):  # noqa: E501
        """list wip in specific project and user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_wip_with_http_info(owner, repository, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: (required)
        :param str repository: (required)
        :return: list[Wip]
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
                    " to method list_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `list_wip`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `list_wip`")  # noqa: E501

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
            '/wip/{owner}/{repository}/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Wip]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revert_wip_changes(self, repository, owner, ref_name, **kwargs):  # noqa: E501
        """revert changes in working in process, empty path will revert all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revert_wip_changes(repository, owner, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: (required)
        :param str owner: (required)
        :param str ref_name: ref name (required)
        :param str path_prefix: prefix of path
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revert_wip_changes_with_http_info(repository, owner, ref_name, **kwargs)  # noqa: E501
        else:
            (data) = self.revert_wip_changes_with_http_info(repository, owner, ref_name, **kwargs)  # noqa: E501
            return data

    def revert_wip_changes_with_http_info(self, repository, owner, ref_name, **kwargs):  # noqa: E501
        """revert changes in working in process, empty path will revert all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revert_wip_changes_with_http_info(repository, owner, ref_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: (required)
        :param str owner: (required)
        :param str ref_name: ref name (required)
        :param str path_prefix: prefix of path
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'owner', 'ref_name', 'path_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revert_wip_changes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `revert_wip_changes`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `revert_wip_changes`")  # noqa: E501
        # verify the required parameter 'ref_name' is set
        if ('ref_name' not in params or
                params['ref_name'] is None):
            raise ValueError("Missing the required parameter `ref_name` when calling `revert_wip_changes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501

        query_params = []
        if 'ref_name' in params:
            query_params.append(('refName', params['ref_name']))  # noqa: E501
        if 'path_prefix' in params:
            query_params.append(('pathPrefix', params['path_prefix']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basic_auth', 'cookie_auth', 'jwt_token']  # noqa: E501

        return self.api_client.call_api(
            '/wip/{owner}/{repository}/revert', 'POST',
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

    def update_wip(self, body, ref_name, repository, owner, **kwargs):  # noqa: E501
        """update wip  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_wip(body, ref_name, repository, owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateWip body: (required)
        :param str ref_name: ref name (required)
        :param str repository: (required)
        :param str owner: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_wip_with_http_info(body, ref_name, repository, owner, **kwargs)  # noqa: E501
        else:
            (data) = self.update_wip_with_http_info(body, ref_name, repository, owner, **kwargs)  # noqa: E501
            return data

    def update_wip_with_http_info(self, body, ref_name, repository, owner, **kwargs):  # noqa: E501
        """update wip  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_wip_with_http_info(body, ref_name, repository, owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateWip body: (required)
        :param str ref_name: ref name (required)
        :param str repository: (required)
        :param str owner: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'ref_name', 'repository', 'owner']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_wip`")  # noqa: E501
        # verify the required parameter 'ref_name' is set
        if ('ref_name' not in params or
                params['ref_name'] is None):
            raise ValueError("Missing the required parameter `ref_name` when calling `update_wip`")  # noqa: E501
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `update_wip`")  # noqa: E501
        # verify the required parameter 'owner' is set
        if ('owner' not in params or
                params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `update_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'owner' in params:
            path_params['owner'] = params['owner']  # noqa: E501

        query_params = []
        if 'ref_name' in params:
            query_params.append(('refName', params['ref_name']))  # noqa: E501

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
            '/wip/{owner}/{repository}', 'POST',
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
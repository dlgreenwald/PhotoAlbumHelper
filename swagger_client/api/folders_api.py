# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FoldersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def folder_cover(self, uid, token, size, **kwargs):  # noqa: E501
        """returns a folder cover image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_cover(uid, token, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: folder uid (required)
        :param str token: user-specific security token provided with session or 'public' when running PhotoPrism in public mode (required)
        :param str size: thumbnail size (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.folder_cover_with_http_info(uid, token, size, **kwargs)  # noqa: E501
        else:
            (data) = self.folder_cover_with_http_info(uid, token, size, **kwargs)  # noqa: E501
            return data

    def folder_cover_with_http_info(self, uid, token, size, **kwargs):  # noqa: E501
        """returns a folder cover image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.folder_cover_with_http_info(uid, token, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: folder uid (required)
        :param str token: user-specific security token provided with session or 'public' when running PhotoPrism in public mode (required)
        :param str size: thumbnail size (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'token', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method folder_cover" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `folder_cover`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `folder_cover`")  # noqa: E501
        # verify the required parameter 'size' is set
        if self.api_client.client_side_validation and ('size' not in params or
                                                       params['size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `size` when calling `folder_cover`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501
        if 'size' in params:
            path_params['size'] = params['size']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/jpeg', 'image/svg+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/folders/t/{uid}/{token}/{size}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

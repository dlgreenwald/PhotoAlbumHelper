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


class StacksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def photo_primary(self, uid, fileuid, **kwargs):  # noqa: E501
        """sets the primary file for a photo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.photo_primary(uid, fileuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: photo uid (required)
        :param str fileuid: file uid (required)
        :return: EntityPhoto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.photo_primary_with_http_info(uid, fileuid, **kwargs)  # noqa: E501
        else:
            (data) = self.photo_primary_with_http_info(uid, fileuid, **kwargs)  # noqa: E501
            return data

    def photo_primary_with_http_info(self, uid, fileuid, **kwargs):  # noqa: E501
        """sets the primary file for a photo  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.photo_primary_with_http_info(uid, fileuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: photo uid (required)
        :param str fileuid: file uid (required)
        :return: EntityPhoto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'fileuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method photo_primary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `photo_primary`")  # noqa: E501
        # verify the required parameter 'fileuid' is set
        if self.api_client.client_side_validation and ('fileuid' not in params or
                                                       params['fileuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fileuid` when calling `photo_primary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'fileuid' in params:
            path_params['fileuid'] = params['fileuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/photos/{uid}/files/{fileuid}/primary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityPhoto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def photo_unstack(self, uid, fileuid, **kwargs):  # noqa: E501
        """removes a file from an existing photo stack  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.photo_unstack(uid, fileuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: photo uid (required)
        :param str fileuid: file uid (required)
        :return: EntityPhoto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.photo_unstack_with_http_info(uid, fileuid, **kwargs)  # noqa: E501
        else:
            (data) = self.photo_unstack_with_http_info(uid, fileuid, **kwargs)  # noqa: E501
            return data

    def photo_unstack_with_http_info(self, uid, fileuid, **kwargs):  # noqa: E501
        """removes a file from an existing photo stack  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.photo_unstack_with_http_info(uid, fileuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: photo uid (required)
        :param str fileuid: file uid (required)
        :return: EntityPhoto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'fileuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method photo_unstack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `photo_unstack`")  # noqa: E501
        # verify the required parameter 'fileuid' is set
        if self.api_client.client_side_validation and ('fileuid' not in params or
                                                       params['fileuid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fileuid` when calling `photo_unstack`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'fileuid' in params:
            path_params['fileuid'] = params['fileuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/photos/{uid}/files/{fileuid}/unstack', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityPhoto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
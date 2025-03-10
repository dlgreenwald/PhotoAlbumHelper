# coding: utf-8

"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class FormLink(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_comment': 'bool',
        'can_edit': 'bool',
        'expires': 'int',
        'max_views': 'int',
        'password': 'str',
        'slug': 'str',
        'token': 'str'
    }

    attribute_map = {
        'can_comment': 'CanComment',
        'can_edit': 'CanEdit',
        'expires': 'Expires',
        'max_views': 'MaxViews',
        'password': 'Password',
        'slug': 'Slug',
        'token': 'Token'
    }

    def __init__(self, can_comment=None, can_edit=None, expires=None, max_views=None, password=None, slug=None, token=None, _configuration=None):  # noqa: E501
        """FormLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_comment = None
        self._can_edit = None
        self._expires = None
        self._max_views = None
        self._password = None
        self._slug = None
        self._token = None
        self.discriminator = None

        if can_comment is not None:
            self.can_comment = can_comment
        if can_edit is not None:
            self.can_edit = can_edit
        if expires is not None:
            self.expires = expires
        if max_views is not None:
            self.max_views = max_views
        if password is not None:
            self.password = password
        if slug is not None:
            self.slug = slug
        if token is not None:
            self.token = token

    @property
    def can_comment(self):
        """Gets the can_comment of this FormLink.  # noqa: E501


        :return: The can_comment of this FormLink.  # noqa: E501
        :rtype: bool
        """
        return self._can_comment

    @can_comment.setter
    def can_comment(self, can_comment):
        """Sets the can_comment of this FormLink.


        :param can_comment: The can_comment of this FormLink.  # noqa: E501
        :type: bool
        """

        self._can_comment = can_comment

    @property
    def can_edit(self):
        """Gets the can_edit of this FormLink.  # noqa: E501


        :return: The can_edit of this FormLink.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this FormLink.


        :param can_edit: The can_edit of this FormLink.  # noqa: E501
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def expires(self):
        """Gets the expires of this FormLink.  # noqa: E501


        :return: The expires of this FormLink.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this FormLink.


        :param expires: The expires of this FormLink.  # noqa: E501
        :type: int
        """

        self._expires = expires

    @property
    def max_views(self):
        """Gets the max_views of this FormLink.  # noqa: E501


        :return: The max_views of this FormLink.  # noqa: E501
        :rtype: int
        """
        return self._max_views

    @max_views.setter
    def max_views(self, max_views):
        """Sets the max_views of this FormLink.


        :param max_views: The max_views of this FormLink.  # noqa: E501
        :type: int
        """

        self._max_views = max_views

    @property
    def password(self):
        """Gets the password of this FormLink.  # noqa: E501


        :return: The password of this FormLink.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this FormLink.


        :param password: The password of this FormLink.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def slug(self):
        """Gets the slug of this FormLink.  # noqa: E501


        :return: The slug of this FormLink.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FormLink.


        :param slug: The slug of this FormLink.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def token(self):
        """Gets the token of this FormLink.  # noqa: E501


        :return: The token of this FormLink.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this FormLink.


        :param token: The token of this FormLink.  # noqa: E501
        :type: str
        """

        self._token = token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FormLink, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FormLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormLink):
            return True

        return self.to_dict() != other.to_dict()

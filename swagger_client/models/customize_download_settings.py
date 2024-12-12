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


class CustomizeDownloadSettings(object):
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
        'disabled': 'bool',
        'media_raw': 'bool',
        'media_sidecar': 'bool',
        'name': 'CustomizeDownloadName',
        'originals': 'bool'
    }

    attribute_map = {
        'disabled': 'disabled',
        'media_raw': 'mediaRaw',
        'media_sidecar': 'mediaSidecar',
        'name': 'name',
        'originals': 'originals'
    }

    def __init__(self, disabled=None, media_raw=None, media_sidecar=None, name=None, originals=None, _configuration=None):  # noqa: E501
        """CustomizeDownloadSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._disabled = None
        self._media_raw = None
        self._media_sidecar = None
        self._name = None
        self._originals = None
        self.discriminator = None

        if disabled is not None:
            self.disabled = disabled
        if media_raw is not None:
            self.media_raw = media_raw
        if media_sidecar is not None:
            self.media_sidecar = media_sidecar
        if name is not None:
            self.name = name
        if originals is not None:
            self.originals = originals

    @property
    def disabled(self):
        """Gets the disabled of this CustomizeDownloadSettings.  # noqa: E501


        :return: The disabled of this CustomizeDownloadSettings.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this CustomizeDownloadSettings.


        :param disabled: The disabled of this CustomizeDownloadSettings.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def media_raw(self):
        """Gets the media_raw of this CustomizeDownloadSettings.  # noqa: E501


        :return: The media_raw of this CustomizeDownloadSettings.  # noqa: E501
        :rtype: bool
        """
        return self._media_raw

    @media_raw.setter
    def media_raw(self, media_raw):
        """Sets the media_raw of this CustomizeDownloadSettings.


        :param media_raw: The media_raw of this CustomizeDownloadSettings.  # noqa: E501
        :type: bool
        """

        self._media_raw = media_raw

    @property
    def media_sidecar(self):
        """Gets the media_sidecar of this CustomizeDownloadSettings.  # noqa: E501


        :return: The media_sidecar of this CustomizeDownloadSettings.  # noqa: E501
        :rtype: bool
        """
        return self._media_sidecar

    @media_sidecar.setter
    def media_sidecar(self, media_sidecar):
        """Sets the media_sidecar of this CustomizeDownloadSettings.


        :param media_sidecar: The media_sidecar of this CustomizeDownloadSettings.  # noqa: E501
        :type: bool
        """

        self._media_sidecar = media_sidecar

    @property
    def name(self):
        """Gets the name of this CustomizeDownloadSettings.  # noqa: E501


        :return: The name of this CustomizeDownloadSettings.  # noqa: E501
        :rtype: CustomizeDownloadName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomizeDownloadSettings.


        :param name: The name of this CustomizeDownloadSettings.  # noqa: E501
        :type: CustomizeDownloadName
        """

        self._name = name

    @property
    def originals(self):
        """Gets the originals of this CustomizeDownloadSettings.  # noqa: E501


        :return: The originals of this CustomizeDownloadSettings.  # noqa: E501
        :rtype: bool
        """
        return self._originals

    @originals.setter
    def originals(self, originals):
        """Sets the originals of this CustomizeDownloadSettings.


        :param originals: The originals of this CustomizeDownloadSettings.  # noqa: E501
        :type: bool
        """

        self._originals = originals

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
        if issubclass(CustomizeDownloadSettings, dict):
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
        if not isinstance(other, CustomizeDownloadSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomizeDownloadSettings):
            return True

        return self.to_dict() != other.to_dict()

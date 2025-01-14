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


class FormFace(object):
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
        'hidden': 'bool',
        'subj_uid': 'str'
    }

    attribute_map = {
        'hidden': 'Hidden',
        'subj_uid': 'SubjUID'
    }

    def __init__(self, hidden=None, subj_uid=None, _configuration=None):  # noqa: E501
        """FormFace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hidden = None
        self._subj_uid = None
        self.discriminator = None

        if hidden is not None:
            self.hidden = hidden
        if subj_uid is not None:
            self.subj_uid = subj_uid

    @property
    def hidden(self):
        """Gets the hidden of this FormFace.  # noqa: E501


        :return: The hidden of this FormFace.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this FormFace.


        :param hidden: The hidden of this FormFace.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def subj_uid(self):
        """Gets the subj_uid of this FormFace.  # noqa: E501


        :return: The subj_uid of this FormFace.  # noqa: E501
        :rtype: str
        """
        return self._subj_uid

    @subj_uid.setter
    def subj_uid(self, subj_uid):
        """Sets the subj_uid of this FormFace.


        :param subj_uid: The subj_uid of this FormFace.  # noqa: E501
        :type: str
        """

        self._subj_uid = subj_uid

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
        if issubclass(FormFace, dict):
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
        if not isinstance(other, FormFace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormFace):
            return True

        return self.to_dict() != other.to_dict()

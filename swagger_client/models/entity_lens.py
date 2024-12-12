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


class EntityLens(object):
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
        'description': 'str',
        'id': 'int',
        'make': 'str',
        'model': 'str',
        'name': 'str',
        'notes': 'str',
        'slug': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'id': 'ID',
        'make': 'Make',
        'model': 'Model',
        'name': 'Name',
        'notes': 'Notes',
        'slug': 'Slug',
        'type': 'Type'
    }

    def __init__(self, description=None, id=None, make=None, model=None, name=None, notes=None, slug=None, type=None, _configuration=None):  # noqa: E501
        """EntityLens - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._id = None
        self._make = None
        self._model = None
        self._name = None
        self._notes = None
        self._slug = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if slug is not None:
            self.slug = slug
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this EntityLens.  # noqa: E501


        :return: The description of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EntityLens.


        :param description: The description of this EntityLens.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this EntityLens.  # noqa: E501


        :return: The id of this EntityLens.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityLens.


        :param id: The id of this EntityLens.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def make(self):
        """Gets the make of this EntityLens.  # noqa: E501


        :return: The make of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this EntityLens.


        :param make: The make of this EntityLens.  # noqa: E501
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this EntityLens.  # noqa: E501


        :return: The model of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this EntityLens.


        :param model: The model of this EntityLens.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """Gets the name of this EntityLens.  # noqa: E501


        :return: The name of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityLens.


        :param name: The name of this EntityLens.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this EntityLens.  # noqa: E501


        :return: The notes of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EntityLens.


        :param notes: The notes of this EntityLens.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def slug(self):
        """Gets the slug of this EntityLens.  # noqa: E501


        :return: The slug of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this EntityLens.


        :param slug: The slug of this EntityLens.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def type(self):
        """Gets the type of this EntityLens.  # noqa: E501


        :return: The type of this EntityLens.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityLens.


        :param type: The type of this EntityLens.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(EntityLens, dict):
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
        if not isinstance(other, EntityLens):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityLens):
            return True

        return self.to_dict() != other.to_dict()

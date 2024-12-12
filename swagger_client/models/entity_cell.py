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


class EntityCell(object):
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
        'category': 'str',
        'created_at': 'str',
        'id': 'str',
        'name': 'str',
        'place': 'EntityPlace',
        'postcode': 'str',
        'street': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'category': 'Category',
        'created_at': 'CreatedAt',
        'id': 'ID',
        'name': 'Name',
        'place': 'Place',
        'postcode': 'Postcode',
        'street': 'Street',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, category=None, created_at=None, id=None, name=None, place=None, postcode=None, street=None, updated_at=None, _configuration=None):  # noqa: E501
        """EntityCell - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._category = None
        self._created_at = None
        self._id = None
        self._name = None
        self._place = None
        self._postcode = None
        self._street = None
        self._updated_at = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if place is not None:
            self.place = place
        if postcode is not None:
            self.postcode = postcode
        if street is not None:
            self.street = street
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def category(self):
        """Gets the category of this EntityCell.  # noqa: E501


        :return: The category of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EntityCell.


        :param category: The category of this EntityCell.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def created_at(self):
        """Gets the created_at of this EntityCell.  # noqa: E501


        :return: The created_at of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EntityCell.


        :param created_at: The created_at of this EntityCell.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this EntityCell.  # noqa: E501


        :return: The id of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityCell.


        :param id: The id of this EntityCell.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EntityCell.  # noqa: E501


        :return: The name of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityCell.


        :param name: The name of this EntityCell.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def place(self):
        """Gets the place of this EntityCell.  # noqa: E501


        :return: The place of this EntityCell.  # noqa: E501
        :rtype: EntityPlace
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this EntityCell.


        :param place: The place of this EntityCell.  # noqa: E501
        :type: EntityPlace
        """

        self._place = place

    @property
    def postcode(self):
        """Gets the postcode of this EntityCell.  # noqa: E501


        :return: The postcode of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this EntityCell.


        :param postcode: The postcode of this EntityCell.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def street(self):
        """Gets the street of this EntityCell.  # noqa: E501


        :return: The street of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this EntityCell.


        :param street: The street of this EntityCell.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def updated_at(self):
        """Gets the updated_at of this EntityCell.  # noqa: E501


        :return: The updated_at of this EntityCell.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EntityCell.


        :param updated_at: The updated_at of this EntityCell.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(EntityCell, dict):
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
        if not isinstance(other, EntityCell):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityCell):
            return True

        return self.to_dict() != other.to_dict()
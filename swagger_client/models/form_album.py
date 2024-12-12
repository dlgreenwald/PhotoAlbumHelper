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


class FormAlbum(object):
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
        'caption': 'str',
        'category': 'str',
        'country': 'str',
        'description': 'str',
        'favorite': 'bool',
        'filter': 'str',
        'location': 'str',
        'notes': 'str',
        'order': 'str',
        'private': 'bool',
        'template': 'str',
        'thumb': 'str',
        'thumb_src': 'str',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'caption': 'Caption',
        'category': 'Category',
        'country': 'Country',
        'description': 'Description',
        'favorite': 'Favorite',
        'filter': 'Filter',
        'location': 'Location',
        'notes': 'Notes',
        'order': 'Order',
        'private': 'Private',
        'template': 'Template',
        'thumb': 'Thumb',
        'thumb_src': 'ThumbSrc',
        'title': 'Title',
        'type': 'Type'
    }

    def __init__(self, caption=None, category=None, country=None, description=None, favorite=None, filter=None, location=None, notes=None, order=None, private=None, template=None, thumb=None, thumb_src=None, title=None, type=None, _configuration=None):  # noqa: E501
        """FormAlbum - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._caption = None
        self._category = None
        self._country = None
        self._description = None
        self._favorite = None
        self._filter = None
        self._location = None
        self._notes = None
        self._order = None
        self._private = None
        self._template = None
        self._thumb = None
        self._thumb_src = None
        self._title = None
        self._type = None
        self.discriminator = None

        if caption is not None:
            self.caption = caption
        if category is not None:
            self.category = category
        if country is not None:
            self.country = country
        if description is not None:
            self.description = description
        if favorite is not None:
            self.favorite = favorite
        if filter is not None:
            self.filter = filter
        if location is not None:
            self.location = location
        if notes is not None:
            self.notes = notes
        if order is not None:
            self.order = order
        if private is not None:
            self.private = private
        if template is not None:
            self.template = template
        if thumb is not None:
            self.thumb = thumb
        if thumb_src is not None:
            self.thumb_src = thumb_src
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def caption(self):
        """Gets the caption of this FormAlbum.  # noqa: E501


        :return: The caption of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this FormAlbum.


        :param caption: The caption of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def category(self):
        """Gets the category of this FormAlbum.  # noqa: E501


        :return: The category of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this FormAlbum.


        :param category: The category of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def country(self):
        """Gets the country of this FormAlbum.  # noqa: E501


        :return: The country of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this FormAlbum.


        :param country: The country of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def description(self):
        """Gets the description of this FormAlbum.  # noqa: E501


        :return: The description of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FormAlbum.


        :param description: The description of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def favorite(self):
        """Gets the favorite of this FormAlbum.  # noqa: E501


        :return: The favorite of this FormAlbum.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this FormAlbum.


        :param favorite: The favorite of this FormAlbum.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def filter(self):
        """Gets the filter of this FormAlbum.  # noqa: E501


        :return: The filter of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this FormAlbum.


        :param filter: The filter of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def location(self):
        """Gets the location of this FormAlbum.  # noqa: E501


        :return: The location of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FormAlbum.


        :param location: The location of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def notes(self):
        """Gets the notes of this FormAlbum.  # noqa: E501


        :return: The notes of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this FormAlbum.


        :param notes: The notes of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def order(self):
        """Gets the order of this FormAlbum.  # noqa: E501


        :return: The order of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this FormAlbum.


        :param order: The order of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def private(self):
        """Gets the private of this FormAlbum.  # noqa: E501


        :return: The private of this FormAlbum.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this FormAlbum.


        :param private: The private of this FormAlbum.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def template(self):
        """Gets the template of this FormAlbum.  # noqa: E501


        :return: The template of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this FormAlbum.


        :param template: The template of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def thumb(self):
        """Gets the thumb of this FormAlbum.  # noqa: E501


        :return: The thumb of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this FormAlbum.


        :param thumb: The thumb of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._thumb = thumb

    @property
    def thumb_src(self):
        """Gets the thumb_src of this FormAlbum.  # noqa: E501


        :return: The thumb_src of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._thumb_src

    @thumb_src.setter
    def thumb_src(self, thumb_src):
        """Sets the thumb_src of this FormAlbum.


        :param thumb_src: The thumb_src of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._thumb_src = thumb_src

    @property
    def title(self):
        """Gets the title of this FormAlbum.  # noqa: E501


        :return: The title of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FormAlbum.


        :param title: The title of this FormAlbum.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this FormAlbum.  # noqa: E501


        :return: The type of this FormAlbum.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormAlbum.


        :param type: The type of this FormAlbum.  # noqa: E501
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
        if issubclass(FormAlbum, dict):
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
        if not isinstance(other, FormAlbum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormAlbum):
            return True

        return self.to_dict() != other.to_dict()

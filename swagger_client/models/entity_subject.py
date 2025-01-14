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


class EntitySubject(object):
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
        'about': 'str',
        'alias': 'str',
        'bio': 'str',
        'created_at': 'str',
        'deleted_at': 'str',
        'excluded': 'bool',
        'favorite': 'bool',
        'file_count': 'int',
        'hidden': 'bool',
        'name': 'str',
        'notes': 'str',
        'photo_count': 'int',
        'private': 'bool',
        'slug': 'str',
        'src': 'str',
        'thumb': 'str',
        'thumb_src': 'str',
        'type': 'str',
        'uid': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'about': 'About',
        'alias': 'Alias',
        'bio': 'Bio',
        'created_at': 'CreatedAt',
        'deleted_at': 'DeletedAt',
        'excluded': 'Excluded',
        'favorite': 'Favorite',
        'file_count': 'FileCount',
        'hidden': 'Hidden',
        'name': 'Name',
        'notes': 'Notes',
        'photo_count': 'PhotoCount',
        'private': 'Private',
        'slug': 'Slug',
        'src': 'Src',
        'thumb': 'Thumb',
        'thumb_src': 'ThumbSrc',
        'type': 'Type',
        'uid': 'UID',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, about=None, alias=None, bio=None, created_at=None, deleted_at=None, excluded=None, favorite=None, file_count=None, hidden=None, name=None, notes=None, photo_count=None, private=None, slug=None, src=None, thumb=None, thumb_src=None, type=None, uid=None, updated_at=None, _configuration=None):  # noqa: E501
        """EntitySubject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._about = None
        self._alias = None
        self._bio = None
        self._created_at = None
        self._deleted_at = None
        self._excluded = None
        self._favorite = None
        self._file_count = None
        self._hidden = None
        self._name = None
        self._notes = None
        self._photo_count = None
        self._private = None
        self._slug = None
        self._src = None
        self._thumb = None
        self._thumb_src = None
        self._type = None
        self._uid = None
        self._updated_at = None
        self.discriminator = None

        if about is not None:
            self.about = about
        if alias is not None:
            self.alias = alias
        if bio is not None:
            self.bio = bio
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if excluded is not None:
            self.excluded = excluded
        if favorite is not None:
            self.favorite = favorite
        if file_count is not None:
            self.file_count = file_count
        if hidden is not None:
            self.hidden = hidden
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if photo_count is not None:
            self.photo_count = photo_count
        if private is not None:
            self.private = private
        if slug is not None:
            self.slug = slug
        if src is not None:
            self.src = src
        if thumb is not None:
            self.thumb = thumb
        if thumb_src is not None:
            self.thumb_src = thumb_src
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def about(self):
        """Gets the about of this EntitySubject.  # noqa: E501


        :return: The about of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this EntitySubject.


        :param about: The about of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def alias(self):
        """Gets the alias of this EntitySubject.  # noqa: E501


        :return: The alias of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this EntitySubject.


        :param alias: The alias of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def bio(self):
        """Gets the bio of this EntitySubject.  # noqa: E501


        :return: The bio of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this EntitySubject.


        :param bio: The bio of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._bio = bio

    @property
    def created_at(self):
        """Gets the created_at of this EntitySubject.  # noqa: E501


        :return: The created_at of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EntitySubject.


        :param created_at: The created_at of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this EntitySubject.  # noqa: E501


        :return: The deleted_at of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this EntitySubject.


        :param deleted_at: The deleted_at of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def excluded(self):
        """Gets the excluded of this EntitySubject.  # noqa: E501


        :return: The excluded of this EntitySubject.  # noqa: E501
        :rtype: bool
        """
        return self._excluded

    @excluded.setter
    def excluded(self, excluded):
        """Sets the excluded of this EntitySubject.


        :param excluded: The excluded of this EntitySubject.  # noqa: E501
        :type: bool
        """

        self._excluded = excluded

    @property
    def favorite(self):
        """Gets the favorite of this EntitySubject.  # noqa: E501


        :return: The favorite of this EntitySubject.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this EntitySubject.


        :param favorite: The favorite of this EntitySubject.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def file_count(self):
        """Gets the file_count of this EntitySubject.  # noqa: E501


        :return: The file_count of this EntitySubject.  # noqa: E501
        :rtype: int
        """
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        """Sets the file_count of this EntitySubject.


        :param file_count: The file_count of this EntitySubject.  # noqa: E501
        :type: int
        """

        self._file_count = file_count

    @property
    def hidden(self):
        """Gets the hidden of this EntitySubject.  # noqa: E501


        :return: The hidden of this EntitySubject.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this EntitySubject.


        :param hidden: The hidden of this EntitySubject.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def name(self):
        """Gets the name of this EntitySubject.  # noqa: E501


        :return: The name of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntitySubject.


        :param name: The name of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this EntitySubject.  # noqa: E501


        :return: The notes of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EntitySubject.


        :param notes: The notes of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def photo_count(self):
        """Gets the photo_count of this EntitySubject.  # noqa: E501


        :return: The photo_count of this EntitySubject.  # noqa: E501
        :rtype: int
        """
        return self._photo_count

    @photo_count.setter
    def photo_count(self, photo_count):
        """Sets the photo_count of this EntitySubject.


        :param photo_count: The photo_count of this EntitySubject.  # noqa: E501
        :type: int
        """

        self._photo_count = photo_count

    @property
    def private(self):
        """Gets the private of this EntitySubject.  # noqa: E501


        :return: The private of this EntitySubject.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this EntitySubject.


        :param private: The private of this EntitySubject.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def slug(self):
        """Gets the slug of this EntitySubject.  # noqa: E501


        :return: The slug of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this EntitySubject.


        :param slug: The slug of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def src(self):
        """Gets the src of this EntitySubject.  # noqa: E501


        :return: The src of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this EntitySubject.


        :param src: The src of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._src = src

    @property
    def thumb(self):
        """Gets the thumb of this EntitySubject.  # noqa: E501


        :return: The thumb of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this EntitySubject.


        :param thumb: The thumb of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._thumb = thumb

    @property
    def thumb_src(self):
        """Gets the thumb_src of this EntitySubject.  # noqa: E501


        :return: The thumb_src of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._thumb_src

    @thumb_src.setter
    def thumb_src(self, thumb_src):
        """Sets the thumb_src of this EntitySubject.


        :param thumb_src: The thumb_src of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._thumb_src = thumb_src

    @property
    def type(self):
        """Gets the type of this EntitySubject.  # noqa: E501


        :return: The type of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntitySubject.


        :param type: The type of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this EntitySubject.  # noqa: E501


        :return: The uid of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EntitySubject.


        :param uid: The uid of this EntitySubject.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def updated_at(self):
        """Gets the updated_at of this EntitySubject.  # noqa: E501


        :return: The updated_at of this EntitySubject.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EntitySubject.


        :param updated_at: The updated_at of this EntitySubject.  # noqa: E501
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
        if issubclass(EntitySubject, dict):
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
        if not isinstance(other, EntitySubject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntitySubject):
            return True

        return self.to_dict() != other.to_dict()

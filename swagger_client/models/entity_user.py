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


class EntityUser(object):
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
        'id': 'int',
        'uid': 'str',
        'auth_provider': 'str',
        'auth_method': 'str',
        'auth_id': 'str',
        'name': 'str',
        'display_name': 'str',
        'email': 'str',
        'role': 'str',
        'attr': 'str',
        'super_admin': 'bool',
        'can_login': 'bool',
        'login_at': 'str',
        'web_dav': 'bool',
        'base_path': 'str',
        'upload_path': 'str',
        'can_invite': 'bool',
        'verified_at': 'str',
        'details': 'EntityUserDetails',
        'settings': 'EntitySettings',
        'thumb': 'str',
        'thumb_src': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'uid': 'UID',
        'auth_provider': 'AuthProvider',
        'auth_method': 'AuthMethod',
        'auth_id': 'AuthID',
        'name': 'Name',
        'display_name': 'DisplayName',
        'email': 'Email',
        'role': 'Role',
        'attr': 'Attr',
        'super_admin': 'SuperAdmin',
        'can_login': 'CanLogin',
        'login_at': 'LoginAt',
        'web_dav': 'WebDav',
        'base_path': 'BasePath',
        'upload_path': 'UploadPath',
        'can_invite': 'CanInvite',
        'verified_at': 'VerifiedAt',
        'details': 'Details',
        'settings': 'Settings',
        'thumb': 'Thumb',
        'thumb_src': 'ThumbSrc',
        'created_at': 'CreatedAt',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, id=None, uid=None, auth_provider=None, auth_method=None, auth_id=None, name=None, display_name=None, email=None, role=None, attr=None, super_admin=None, can_login=None, login_at=None, web_dav=None, base_path=None, upload_path=None, can_invite=None, verified_at=None, details=None, settings=None, thumb=None, thumb_src=None, created_at=None, updated_at=None, _configuration=None):  # noqa: E501
        """EntityUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._uid = None
        self._auth_provider = None
        self._auth_method = None
        self._auth_id = None
        self._name = None
        self._display_name = None
        self._email = None
        self._role = None
        self._attr = None
        self._super_admin = None
        self._can_login = None
        self._login_at = None
        self._web_dav = None
        self._base_path = None
        self._upload_path = None
        self._can_invite = None
        self._verified_at = None
        self._details = None
        self._settings = None
        self._thumb = None
        self._thumb_src = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if auth_provider is not None:
            self.auth_provider = auth_provider
        if auth_method is not None:
            self.auth_method = auth_method
        if auth_id is not None:
            self.auth_id = auth_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if email is not None:
            self.email = email
        if role is not None:
            self.role = role
        if attr is not None:
            self.attr = attr
        if super_admin is not None:
            self.super_admin = super_admin
        if can_login is not None:
            self.can_login = can_login
        if login_at is not None:
            self.login_at = login_at
        if web_dav is not None:
            self.web_dav = web_dav
        if base_path is not None:
            self.base_path = base_path
        if upload_path is not None:
            self.upload_path = upload_path
        if can_invite is not None:
            self.can_invite = can_invite
        if verified_at is not None:
            self.verified_at = verified_at
        if details is not None:
            self.details = details
        if settings is not None:
            self.settings = settings
        if thumb is not None:
            self.thumb = thumb
        if thumb_src is not None:
            self.thumb_src = thumb_src
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this EntityUser.  # noqa: E501


        :return: The id of this EntityUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityUser.


        :param id: The id of this EntityUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this EntityUser.  # noqa: E501


        :return: The uid of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EntityUser.


        :param uid: The uid of this EntityUser.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def auth_provider(self):
        """Gets the auth_provider of this EntityUser.  # noqa: E501


        :return: The auth_provider of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, auth_provider):
        """Sets the auth_provider of this EntityUser.


        :param auth_provider: The auth_provider of this EntityUser.  # noqa: E501
        :type: str
        """

        self._auth_provider = auth_provider

    @property
    def auth_method(self):
        """Gets the auth_method of this EntityUser.  # noqa: E501


        :return: The auth_method of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this EntityUser.


        :param auth_method: The auth_method of this EntityUser.  # noqa: E501
        :type: str
        """

        self._auth_method = auth_method

    @property
    def auth_id(self):
        """Gets the auth_id of this EntityUser.  # noqa: E501


        :return: The auth_id of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._auth_id

    @auth_id.setter
    def auth_id(self, auth_id):
        """Sets the auth_id of this EntityUser.


        :param auth_id: The auth_id of this EntityUser.  # noqa: E501
        :type: str
        """

        self._auth_id = auth_id

    @property
    def name(self):
        """Gets the name of this EntityUser.  # noqa: E501


        :return: The name of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityUser.


        :param name: The name of this EntityUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this EntityUser.  # noqa: E501


        :return: The display_name of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EntityUser.


        :param display_name: The display_name of this EntityUser.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this EntityUser.  # noqa: E501


        :return: The email of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EntityUser.


        :param email: The email of this EntityUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this EntityUser.  # noqa: E501


        :return: The role of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this EntityUser.


        :param role: The role of this EntityUser.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def attr(self):
        """Gets the attr of this EntityUser.  # noqa: E501


        :return: The attr of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        """Sets the attr of this EntityUser.


        :param attr: The attr of this EntityUser.  # noqa: E501
        :type: str
        """

        self._attr = attr

    @property
    def super_admin(self):
        """Gets the super_admin of this EntityUser.  # noqa: E501


        :return: The super_admin of this EntityUser.  # noqa: E501
        :rtype: bool
        """
        return self._super_admin

    @super_admin.setter
    def super_admin(self, super_admin):
        """Sets the super_admin of this EntityUser.


        :param super_admin: The super_admin of this EntityUser.  # noqa: E501
        :type: bool
        """

        self._super_admin = super_admin

    @property
    def can_login(self):
        """Gets the can_login of this EntityUser.  # noqa: E501


        :return: The can_login of this EntityUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_login

    @can_login.setter
    def can_login(self, can_login):
        """Sets the can_login of this EntityUser.


        :param can_login: The can_login of this EntityUser.  # noqa: E501
        :type: bool
        """

        self._can_login = can_login

    @property
    def login_at(self):
        """Gets the login_at of this EntityUser.  # noqa: E501


        :return: The login_at of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._login_at

    @login_at.setter
    def login_at(self, login_at):
        """Sets the login_at of this EntityUser.


        :param login_at: The login_at of this EntityUser.  # noqa: E501
        :type: str
        """

        self._login_at = login_at

    @property
    def web_dav(self):
        """Gets the web_dav of this EntityUser.  # noqa: E501


        :return: The web_dav of this EntityUser.  # noqa: E501
        :rtype: bool
        """
        return self._web_dav

    @web_dav.setter
    def web_dav(self, web_dav):
        """Sets the web_dav of this EntityUser.


        :param web_dav: The web_dav of this EntityUser.  # noqa: E501
        :type: bool
        """

        self._web_dav = web_dav

    @property
    def base_path(self):
        """Gets the base_path of this EntityUser.  # noqa: E501


        :return: The base_path of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this EntityUser.


        :param base_path: The base_path of this EntityUser.  # noqa: E501
        :type: str
        """

        self._base_path = base_path

    @property
    def upload_path(self):
        """Gets the upload_path of this EntityUser.  # noqa: E501


        :return: The upload_path of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._upload_path

    @upload_path.setter
    def upload_path(self, upload_path):
        """Sets the upload_path of this EntityUser.


        :param upload_path: The upload_path of this EntityUser.  # noqa: E501
        :type: str
        """

        self._upload_path = upload_path

    @property
    def can_invite(self):
        """Gets the can_invite of this EntityUser.  # noqa: E501


        :return: The can_invite of this EntityUser.  # noqa: E501
        :rtype: bool
        """
        return self._can_invite

    @can_invite.setter
    def can_invite(self, can_invite):
        """Sets the can_invite of this EntityUser.


        :param can_invite: The can_invite of this EntityUser.  # noqa: E501
        :type: bool
        """

        self._can_invite = can_invite

    @property
    def verified_at(self):
        """Gets the verified_at of this EntityUser.  # noqa: E501


        :return: The verified_at of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._verified_at

    @verified_at.setter
    def verified_at(self, verified_at):
        """Sets the verified_at of this EntityUser.


        :param verified_at: The verified_at of this EntityUser.  # noqa: E501
        :type: str
        """

        self._verified_at = verified_at

    @property
    def details(self):
        """Gets the details of this EntityUser.  # noqa: E501


        :return: The details of this EntityUser.  # noqa: E501
        :rtype: EntityUserDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this EntityUser.


        :param details: The details of this EntityUser.  # noqa: E501
        :type: EntityUserDetails
        """

        self._details = details

    @property
    def settings(self):
        """Gets the settings of this EntityUser.  # noqa: E501


        :return: The settings of this EntityUser.  # noqa: E501
        :rtype: EntitySettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this EntityUser.


        :param settings: The settings of this EntityUser.  # noqa: E501
        :type: EntitySettings
        """

        self._settings = settings

    @property
    def thumb(self):
        """Gets the thumb of this EntityUser.  # noqa: E501


        :return: The thumb of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this EntityUser.


        :param thumb: The thumb of this EntityUser.  # noqa: E501
        :type: str
        """

        self._thumb = thumb

    @property
    def thumb_src(self):
        """Gets the thumb_src of this EntityUser.  # noqa: E501


        :return: The thumb_src of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._thumb_src

    @thumb_src.setter
    def thumb_src(self, thumb_src):
        """Sets the thumb_src of this EntityUser.


        :param thumb_src: The thumb_src of this EntityUser.  # noqa: E501
        :type: str
        """

        self._thumb_src = thumb_src

    @property
    def created_at(self):
        """Gets the created_at of this EntityUser.  # noqa: E501


        :return: The created_at of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EntityUser.


        :param created_at: The created_at of this EntityUser.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EntityUser.  # noqa: E501


        :return: The updated_at of this EntityUser.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EntityUser.


        :param updated_at: The updated_at of this EntityUser.  # noqa: E501
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
        if issubclass(EntityUser, dict):
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
        if not isinstance(other, EntityUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityUser):
            return True

        return self.to_dict() != other.to_dict()

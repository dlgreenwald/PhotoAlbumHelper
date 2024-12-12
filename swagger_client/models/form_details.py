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


class FormDetails(object):
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
        'artist': 'str',
        'artist_src': 'str',
        'copyright': 'str',
        'copyright_src': 'str',
        'keywords': 'str',
        'keywords_src': 'str',
        'license': 'str',
        'license_src': 'str',
        'notes': 'str',
        'notes_src': 'str',
        'photo_id': 'int',
        'subject': 'str',
        'subject_src': 'str'
    }

    attribute_map = {
        'artist': 'Artist',
        'artist_src': 'ArtistSrc',
        'copyright': 'Copyright',
        'copyright_src': 'CopyrightSrc',
        'keywords': 'Keywords',
        'keywords_src': 'KeywordsSrc',
        'license': 'License',
        'license_src': 'LicenseSrc',
        'notes': 'Notes',
        'notes_src': 'NotesSrc',
        'photo_id': 'PhotoID',
        'subject': 'Subject',
        'subject_src': 'SubjectSrc'
    }

    def __init__(self, artist=None, artist_src=None, copyright=None, copyright_src=None, keywords=None, keywords_src=None, license=None, license_src=None, notes=None, notes_src=None, photo_id=None, subject=None, subject_src=None, _configuration=None):  # noqa: E501
        """FormDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._artist = None
        self._artist_src = None
        self._copyright = None
        self._copyright_src = None
        self._keywords = None
        self._keywords_src = None
        self._license = None
        self._license_src = None
        self._notes = None
        self._notes_src = None
        self._photo_id = None
        self._subject = None
        self._subject_src = None
        self.discriminator = None

        if artist is not None:
            self.artist = artist
        if artist_src is not None:
            self.artist_src = artist_src
        if copyright is not None:
            self.copyright = copyright
        if copyright_src is not None:
            self.copyright_src = copyright_src
        if keywords is not None:
            self.keywords = keywords
        if keywords_src is not None:
            self.keywords_src = keywords_src
        if license is not None:
            self.license = license
        if license_src is not None:
            self.license_src = license_src
        if notes is not None:
            self.notes = notes
        if notes_src is not None:
            self.notes_src = notes_src
        if photo_id is not None:
            self.photo_id = photo_id
        if subject is not None:
            self.subject = subject
        if subject_src is not None:
            self.subject_src = subject_src

    @property
    def artist(self):
        """Gets the artist of this FormDetails.  # noqa: E501


        :return: The artist of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._artist

    @artist.setter
    def artist(self, artist):
        """Sets the artist of this FormDetails.


        :param artist: The artist of this FormDetails.  # noqa: E501
        :type: str
        """

        self._artist = artist

    @property
    def artist_src(self):
        """Gets the artist_src of this FormDetails.  # noqa: E501


        :return: The artist_src of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._artist_src

    @artist_src.setter
    def artist_src(self, artist_src):
        """Sets the artist_src of this FormDetails.


        :param artist_src: The artist_src of this FormDetails.  # noqa: E501
        :type: str
        """

        self._artist_src = artist_src

    @property
    def copyright(self):
        """Gets the copyright of this FormDetails.  # noqa: E501


        :return: The copyright of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this FormDetails.


        :param copyright: The copyright of this FormDetails.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def copyright_src(self):
        """Gets the copyright_src of this FormDetails.  # noqa: E501


        :return: The copyright_src of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._copyright_src

    @copyright_src.setter
    def copyright_src(self, copyright_src):
        """Sets the copyright_src of this FormDetails.


        :param copyright_src: The copyright_src of this FormDetails.  # noqa: E501
        :type: str
        """

        self._copyright_src = copyright_src

    @property
    def keywords(self):
        """Gets the keywords of this FormDetails.  # noqa: E501


        :return: The keywords of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this FormDetails.


        :param keywords: The keywords of this FormDetails.  # noqa: E501
        :type: str
        """

        self._keywords = keywords

    @property
    def keywords_src(self):
        """Gets the keywords_src of this FormDetails.  # noqa: E501


        :return: The keywords_src of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._keywords_src

    @keywords_src.setter
    def keywords_src(self, keywords_src):
        """Sets the keywords_src of this FormDetails.


        :param keywords_src: The keywords_src of this FormDetails.  # noqa: E501
        :type: str
        """

        self._keywords_src = keywords_src

    @property
    def license(self):
        """Gets the license of this FormDetails.  # noqa: E501


        :return: The license of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this FormDetails.


        :param license: The license of this FormDetails.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def license_src(self):
        """Gets the license_src of this FormDetails.  # noqa: E501


        :return: The license_src of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._license_src

    @license_src.setter
    def license_src(self, license_src):
        """Sets the license_src of this FormDetails.


        :param license_src: The license_src of this FormDetails.  # noqa: E501
        :type: str
        """

        self._license_src = license_src

    @property
    def notes(self):
        """Gets the notes of this FormDetails.  # noqa: E501


        :return: The notes of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this FormDetails.


        :param notes: The notes of this FormDetails.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def notes_src(self):
        """Gets the notes_src of this FormDetails.  # noqa: E501


        :return: The notes_src of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._notes_src

    @notes_src.setter
    def notes_src(self, notes_src):
        """Sets the notes_src of this FormDetails.


        :param notes_src: The notes_src of this FormDetails.  # noqa: E501
        :type: str
        """

        self._notes_src = notes_src

    @property
    def photo_id(self):
        """Gets the photo_id of this FormDetails.  # noqa: E501


        :return: The photo_id of this FormDetails.  # noqa: E501
        :rtype: int
        """
        return self._photo_id

    @photo_id.setter
    def photo_id(self, photo_id):
        """Sets the photo_id of this FormDetails.


        :param photo_id: The photo_id of this FormDetails.  # noqa: E501
        :type: int
        """

        self._photo_id = photo_id

    @property
    def subject(self):
        """Gets the subject of this FormDetails.  # noqa: E501


        :return: The subject of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this FormDetails.


        :param subject: The subject of this FormDetails.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def subject_src(self):
        """Gets the subject_src of this FormDetails.  # noqa: E501


        :return: The subject_src of this FormDetails.  # noqa: E501
        :rtype: str
        """
        return self._subject_src

    @subject_src.setter
    def subject_src(self, subject_src):
        """Sets the subject_src of this FormDetails.


        :param subject_src: The subject_src of this FormDetails.  # noqa: E501
        :type: str
        """

        self._subject_src = subject_src

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
        if issubclass(FormDetails, dict):
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
        if not isinstance(other, FormDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormDetails):
            return True

        return self.to_dict() != other.to_dict()
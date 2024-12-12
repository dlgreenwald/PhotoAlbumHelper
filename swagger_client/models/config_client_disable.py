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


class ConfigClientDisable(object):
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
        'backups': 'bool',
        'classification': 'bool',
        'darktable': 'bool',
        'exiftool': 'bool',
        'faces': 'bool',
        'ffmpeg': 'bool',
        'heifconvert': 'bool',
        'imagemagick': 'bool',
        'jpegxl': 'bool',
        'places': 'bool',
        'raw': 'bool',
        'rawtherapee': 'bool',
        'restart': 'bool',
        'settings': 'bool',
        'sips': 'bool',
        'tensorflow': 'bool',
        'vectors': 'bool',
        'vips': 'bool',
        'webdav': 'bool'
    }

    attribute_map = {
        'backups': 'backups',
        'classification': 'classification',
        'darktable': 'darktable',
        'exiftool': 'exiftool',
        'faces': 'faces',
        'ffmpeg': 'ffmpeg',
        'heifconvert': 'heifconvert',
        'imagemagick': 'imagemagick',
        'jpegxl': 'jpegxl',
        'places': 'places',
        'raw': 'raw',
        'rawtherapee': 'rawtherapee',
        'restart': 'restart',
        'settings': 'settings',
        'sips': 'sips',
        'tensorflow': 'tensorflow',
        'vectors': 'vectors',
        'vips': 'vips',
        'webdav': 'webdav'
    }

    def __init__(self, backups=None, classification=None, darktable=None, exiftool=None, faces=None, ffmpeg=None, heifconvert=None, imagemagick=None, jpegxl=None, places=None, raw=None, rawtherapee=None, restart=None, settings=None, sips=None, tensorflow=None, vectors=None, vips=None, webdav=None, _configuration=None):  # noqa: E501
        """ConfigClientDisable - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backups = None
        self._classification = None
        self._darktable = None
        self._exiftool = None
        self._faces = None
        self._ffmpeg = None
        self._heifconvert = None
        self._imagemagick = None
        self._jpegxl = None
        self._places = None
        self._raw = None
        self._rawtherapee = None
        self._restart = None
        self._settings = None
        self._sips = None
        self._tensorflow = None
        self._vectors = None
        self._vips = None
        self._webdav = None
        self.discriminator = None

        if backups is not None:
            self.backups = backups
        if classification is not None:
            self.classification = classification
        if darktable is not None:
            self.darktable = darktable
        if exiftool is not None:
            self.exiftool = exiftool
        if faces is not None:
            self.faces = faces
        if ffmpeg is not None:
            self.ffmpeg = ffmpeg
        if heifconvert is not None:
            self.heifconvert = heifconvert
        if imagemagick is not None:
            self.imagemagick = imagemagick
        if jpegxl is not None:
            self.jpegxl = jpegxl
        if places is not None:
            self.places = places
        if raw is not None:
            self.raw = raw
        if rawtherapee is not None:
            self.rawtherapee = rawtherapee
        if restart is not None:
            self.restart = restart
        if settings is not None:
            self.settings = settings
        if sips is not None:
            self.sips = sips
        if tensorflow is not None:
            self.tensorflow = tensorflow
        if vectors is not None:
            self.vectors = vectors
        if vips is not None:
            self.vips = vips
        if webdav is not None:
            self.webdav = webdav

    @property
    def backups(self):
        """Gets the backups of this ConfigClientDisable.  # noqa: E501


        :return: The backups of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this ConfigClientDisable.


        :param backups: The backups of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._backups = backups

    @property
    def classification(self):
        """Gets the classification of this ConfigClientDisable.  # noqa: E501


        :return: The classification of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this ConfigClientDisable.


        :param classification: The classification of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._classification = classification

    @property
    def darktable(self):
        """Gets the darktable of this ConfigClientDisable.  # noqa: E501


        :return: The darktable of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._darktable

    @darktable.setter
    def darktable(self, darktable):
        """Sets the darktable of this ConfigClientDisable.


        :param darktable: The darktable of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._darktable = darktable

    @property
    def exiftool(self):
        """Gets the exiftool of this ConfigClientDisable.  # noqa: E501


        :return: The exiftool of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._exiftool

    @exiftool.setter
    def exiftool(self, exiftool):
        """Sets the exiftool of this ConfigClientDisable.


        :param exiftool: The exiftool of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._exiftool = exiftool

    @property
    def faces(self):
        """Gets the faces of this ConfigClientDisable.  # noqa: E501


        :return: The faces of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this ConfigClientDisable.


        :param faces: The faces of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._faces = faces

    @property
    def ffmpeg(self):
        """Gets the ffmpeg of this ConfigClientDisable.  # noqa: E501


        :return: The ffmpeg of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._ffmpeg

    @ffmpeg.setter
    def ffmpeg(self, ffmpeg):
        """Sets the ffmpeg of this ConfigClientDisable.


        :param ffmpeg: The ffmpeg of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._ffmpeg = ffmpeg

    @property
    def heifconvert(self):
        """Gets the heifconvert of this ConfigClientDisable.  # noqa: E501


        :return: The heifconvert of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._heifconvert

    @heifconvert.setter
    def heifconvert(self, heifconvert):
        """Sets the heifconvert of this ConfigClientDisable.


        :param heifconvert: The heifconvert of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._heifconvert = heifconvert

    @property
    def imagemagick(self):
        """Gets the imagemagick of this ConfigClientDisable.  # noqa: E501


        :return: The imagemagick of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._imagemagick

    @imagemagick.setter
    def imagemagick(self, imagemagick):
        """Sets the imagemagick of this ConfigClientDisable.


        :param imagemagick: The imagemagick of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._imagemagick = imagemagick

    @property
    def jpegxl(self):
        """Gets the jpegxl of this ConfigClientDisable.  # noqa: E501


        :return: The jpegxl of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._jpegxl

    @jpegxl.setter
    def jpegxl(self, jpegxl):
        """Sets the jpegxl of this ConfigClientDisable.


        :param jpegxl: The jpegxl of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._jpegxl = jpegxl

    @property
    def places(self):
        """Gets the places of this ConfigClientDisable.  # noqa: E501


        :return: The places of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._places

    @places.setter
    def places(self, places):
        """Sets the places of this ConfigClientDisable.


        :param places: The places of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._places = places

    @property
    def raw(self):
        """Gets the raw of this ConfigClientDisable.  # noqa: E501


        :return: The raw of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this ConfigClientDisable.


        :param raw: The raw of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._raw = raw

    @property
    def rawtherapee(self):
        """Gets the rawtherapee of this ConfigClientDisable.  # noqa: E501


        :return: The rawtherapee of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._rawtherapee

    @rawtherapee.setter
    def rawtherapee(self, rawtherapee):
        """Sets the rawtherapee of this ConfigClientDisable.


        :param rawtherapee: The rawtherapee of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._rawtherapee = rawtherapee

    @property
    def restart(self):
        """Gets the restart of this ConfigClientDisable.  # noqa: E501


        :return: The restart of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._restart

    @restart.setter
    def restart(self, restart):
        """Sets the restart of this ConfigClientDisable.


        :param restart: The restart of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._restart = restart

    @property
    def settings(self):
        """Gets the settings of this ConfigClientDisable.  # noqa: E501


        :return: The settings of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ConfigClientDisable.


        :param settings: The settings of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._settings = settings

    @property
    def sips(self):
        """Gets the sips of this ConfigClientDisable.  # noqa: E501


        :return: The sips of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._sips

    @sips.setter
    def sips(self, sips):
        """Sets the sips of this ConfigClientDisable.


        :param sips: The sips of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._sips = sips

    @property
    def tensorflow(self):
        """Gets the tensorflow of this ConfigClientDisable.  # noqa: E501


        :return: The tensorflow of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._tensorflow

    @tensorflow.setter
    def tensorflow(self, tensorflow):
        """Sets the tensorflow of this ConfigClientDisable.


        :param tensorflow: The tensorflow of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._tensorflow = tensorflow

    @property
    def vectors(self):
        """Gets the vectors of this ConfigClientDisable.  # noqa: E501


        :return: The vectors of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._vectors

    @vectors.setter
    def vectors(self, vectors):
        """Sets the vectors of this ConfigClientDisable.


        :param vectors: The vectors of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._vectors = vectors

    @property
    def vips(self):
        """Gets the vips of this ConfigClientDisable.  # noqa: E501


        :return: The vips of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._vips

    @vips.setter
    def vips(self, vips):
        """Sets the vips of this ConfigClientDisable.


        :param vips: The vips of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._vips = vips

    @property
    def webdav(self):
        """Gets the webdav of this ConfigClientDisable.  # noqa: E501


        :return: The webdav of this ConfigClientDisable.  # noqa: E501
        :rtype: bool
        """
        return self._webdav

    @webdav.setter
    def webdav(self, webdav):
        """Sets the webdav of this ConfigClientDisable.


        :param webdav: The webdav of this ConfigClientDisable.  # noqa: E501
        :type: bool
        """

        self._webdav = webdav

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
        if issubclass(ConfigClientDisable, dict):
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
        if not isinstance(other, ConfigClientDisable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigClientDisable):
            return True

        return self.to_dict() != other.to_dict()

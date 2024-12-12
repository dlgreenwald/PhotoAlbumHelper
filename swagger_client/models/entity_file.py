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


class EntityFile(object):
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
        'aspect_ratio': 'float',
        'chroma': 'int',
        'codec': 'str',
        'color_profile': 'str',
        'colors': 'str',
        'created_at': 'str',
        'created_in': 'int',
        'deleted_at': 'str',
        'diff': 'int',
        'duration': 'TimeDuration',
        'error': 'str',
        'fps': 'float',
        'file_type': 'str',
        'frames': 'int',
        'hdr': 'bool',
        'hash': 'str',
        'height': 'int',
        'instance_id': 'str',
        'luminance': 'str',
        'main_color': 'str',
        'media_id': 'str',
        'media_type': 'str',
        'media_utc': 'int',
        'mime': 'str',
        'missing': 'bool',
        'mod_time': 'int',
        'name': 'str',
        'orientation': 'int',
        'orientation_src': 'str',
        'original_name': 'str',
        'photo_uid': 'str',
        'portrait': 'bool',
        'primary': 'bool',
        'projection': 'str',
        'published_at': 'str',
        'root': 'str',
        'sidecar': 'bool',
        'size': 'int',
        'software': 'str',
        'taken_at': 'str',
        'time_index': 'str',
        'uid': 'str',
        'updated_at': 'str',
        'updated_in': 'int',
        'video': 'bool',
        'watermark': 'bool',
        'width': 'int'
    }

    attribute_map = {
        'aspect_ratio': 'AspectRatio',
        'chroma': 'Chroma',
        'codec': 'Codec',
        'color_profile': 'ColorProfile',
        'colors': 'Colors',
        'created_at': 'CreatedAt',
        'created_in': 'CreatedIn',
        'deleted_at': 'DeletedAt',
        'diff': 'Diff',
        'duration': 'Duration',
        'error': 'Error',
        'fps': 'FPS',
        'file_type': 'FileType',
        'frames': 'Frames',
        'hdr': 'HDR',
        'hash': 'Hash',
        'height': 'Height',
        'instance_id': 'InstanceID',
        'luminance': 'Luminance',
        'main_color': 'MainColor',
        'media_id': 'MediaID',
        'media_type': 'MediaType',
        'media_utc': 'MediaUTC',
        'mime': 'Mime',
        'missing': 'Missing',
        'mod_time': 'ModTime',
        'name': 'Name',
        'orientation': 'Orientation',
        'orientation_src': 'OrientationSrc',
        'original_name': 'OriginalName',
        'photo_uid': 'PhotoUID',
        'portrait': 'Portrait',
        'primary': 'Primary',
        'projection': 'Projection',
        'published_at': 'PublishedAt',
        'root': 'Root',
        'sidecar': 'Sidecar',
        'size': 'Size',
        'software': 'Software',
        'taken_at': 'TakenAt',
        'time_index': 'TimeIndex',
        'uid': 'UID',
        'updated_at': 'UpdatedAt',
        'updated_in': 'UpdatedIn',
        'video': 'Video',
        'watermark': 'Watermark',
        'width': 'Width'
    }

    def __init__(self, aspect_ratio=None, chroma=None, codec=None, color_profile=None, colors=None, created_at=None, created_in=None, deleted_at=None, diff=None, duration=None, error=None, fps=None, file_type=None, frames=None, hdr=None, hash=None, height=None, instance_id=None, luminance=None, main_color=None, media_id=None, media_type=None, media_utc=None, mime=None, missing=None, mod_time=None, name=None, orientation=None, orientation_src=None, original_name=None, photo_uid=None, portrait=None, primary=None, projection=None, published_at=None, root=None, sidecar=None, size=None, software=None, taken_at=None, time_index=None, uid=None, updated_at=None, updated_in=None, video=None, watermark=None, width=None, _configuration=None):  # noqa: E501
        """EntityFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aspect_ratio = None
        self._chroma = None
        self._codec = None
        self._color_profile = None
        self._colors = None
        self._created_at = None
        self._created_in = None
        self._deleted_at = None
        self._diff = None
        self._duration = None
        self._error = None
        self._fps = None
        self._file_type = None
        self._frames = None
        self._hdr = None
        self._hash = None
        self._height = None
        self._instance_id = None
        self._luminance = None
        self._main_color = None
        self._media_id = None
        self._media_type = None
        self._media_utc = None
        self._mime = None
        self._missing = None
        self._mod_time = None
        self._name = None
        self._orientation = None
        self._orientation_src = None
        self._original_name = None
        self._photo_uid = None
        self._portrait = None
        self._primary = None
        self._projection = None
        self._published_at = None
        self._root = None
        self._sidecar = None
        self._size = None
        self._software = None
        self._taken_at = None
        self._time_index = None
        self._uid = None
        self._updated_at = None
        self._updated_in = None
        self._video = None
        self._watermark = None
        self._width = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if chroma is not None:
            self.chroma = chroma
        if codec is not None:
            self.codec = codec
        if color_profile is not None:
            self.color_profile = color_profile
        if colors is not None:
            self.colors = colors
        if created_at is not None:
            self.created_at = created_at
        if created_in is not None:
            self.created_in = created_in
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if diff is not None:
            self.diff = diff
        if duration is not None:
            self.duration = duration
        if error is not None:
            self.error = error
        if fps is not None:
            self.fps = fps
        if file_type is not None:
            self.file_type = file_type
        if frames is not None:
            self.frames = frames
        if hdr is not None:
            self.hdr = hdr
        if hash is not None:
            self.hash = hash
        if height is not None:
            self.height = height
        if instance_id is not None:
            self.instance_id = instance_id
        if luminance is not None:
            self.luminance = luminance
        if main_color is not None:
            self.main_color = main_color
        if media_id is not None:
            self.media_id = media_id
        if media_type is not None:
            self.media_type = media_type
        if media_utc is not None:
            self.media_utc = media_utc
        if mime is not None:
            self.mime = mime
        if missing is not None:
            self.missing = missing
        if mod_time is not None:
            self.mod_time = mod_time
        if name is not None:
            self.name = name
        if orientation is not None:
            self.orientation = orientation
        if orientation_src is not None:
            self.orientation_src = orientation_src
        if original_name is not None:
            self.original_name = original_name
        if photo_uid is not None:
            self.photo_uid = photo_uid
        if portrait is not None:
            self.portrait = portrait
        if primary is not None:
            self.primary = primary
        if projection is not None:
            self.projection = projection
        if published_at is not None:
            self.published_at = published_at
        if root is not None:
            self.root = root
        if sidecar is not None:
            self.sidecar = sidecar
        if size is not None:
            self.size = size
        if software is not None:
            self.software = software
        if taken_at is not None:
            self.taken_at = taken_at
        if time_index is not None:
            self.time_index = time_index
        if uid is not None:
            self.uid = uid
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_in is not None:
            self.updated_in = updated_in
        if video is not None:
            self.video = video
        if watermark is not None:
            self.watermark = watermark
        if width is not None:
            self.width = width

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this EntityFile.  # noqa: E501


        :return: The aspect_ratio of this EntityFile.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this EntityFile.


        :param aspect_ratio: The aspect_ratio of this EntityFile.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def chroma(self):
        """Gets the chroma of this EntityFile.  # noqa: E501


        :return: The chroma of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._chroma

    @chroma.setter
    def chroma(self, chroma):
        """Sets the chroma of this EntityFile.


        :param chroma: The chroma of this EntityFile.  # noqa: E501
        :type: int
        """

        self._chroma = chroma

    @property
    def codec(self):
        """Gets the codec of this EntityFile.  # noqa: E501


        :return: The codec of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this EntityFile.


        :param codec: The codec of this EntityFile.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def color_profile(self):
        """Gets the color_profile of this EntityFile.  # noqa: E501


        :return: The color_profile of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._color_profile

    @color_profile.setter
    def color_profile(self, color_profile):
        """Sets the color_profile of this EntityFile.


        :param color_profile: The color_profile of this EntityFile.  # noqa: E501
        :type: str
        """

        self._color_profile = color_profile

    @property
    def colors(self):
        """Gets the colors of this EntityFile.  # noqa: E501


        :return: The colors of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this EntityFile.


        :param colors: The colors of this EntityFile.  # noqa: E501
        :type: str
        """

        self._colors = colors

    @property
    def created_at(self):
        """Gets the created_at of this EntityFile.  # noqa: E501


        :return: The created_at of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EntityFile.


        :param created_at: The created_at of this EntityFile.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_in(self):
        """Gets the created_in of this EntityFile.  # noqa: E501


        :return: The created_in of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._created_in

    @created_in.setter
    def created_in(self, created_in):
        """Sets the created_in of this EntityFile.


        :param created_in: The created_in of this EntityFile.  # noqa: E501
        :type: int
        """

        self._created_in = created_in

    @property
    def deleted_at(self):
        """Gets the deleted_at of this EntityFile.  # noqa: E501


        :return: The deleted_at of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this EntityFile.


        :param deleted_at: The deleted_at of this EntityFile.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def diff(self):
        """Gets the diff of this EntityFile.  # noqa: E501


        :return: The diff of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this EntityFile.


        :param diff: The diff of this EntityFile.  # noqa: E501
        :type: int
        """

        self._diff = diff

    @property
    def duration(self):
        """Gets the duration of this EntityFile.  # noqa: E501


        :return: The duration of this EntityFile.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this EntityFile.


        :param duration: The duration of this EntityFile.  # noqa: E501
        :type: TimeDuration
        """

        self._duration = duration

    @property
    def error(self):
        """Gets the error of this EntityFile.  # noqa: E501


        :return: The error of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EntityFile.


        :param error: The error of this EntityFile.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def fps(self):
        """Gets the fps of this EntityFile.  # noqa: E501


        :return: The fps of this EntityFile.  # noqa: E501
        :rtype: float
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this EntityFile.


        :param fps: The fps of this EntityFile.  # noqa: E501
        :type: float
        """

        self._fps = fps

    @property
    def file_type(self):
        """Gets the file_type of this EntityFile.  # noqa: E501


        :return: The file_type of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this EntityFile.


        :param file_type: The file_type of this EntityFile.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def frames(self):
        """Gets the frames of this EntityFile.  # noqa: E501


        :return: The frames of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._frames

    @frames.setter
    def frames(self, frames):
        """Sets the frames of this EntityFile.


        :param frames: The frames of this EntityFile.  # noqa: E501
        :type: int
        """

        self._frames = frames

    @property
    def hdr(self):
        """Gets the hdr of this EntityFile.  # noqa: E501


        :return: The hdr of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._hdr

    @hdr.setter
    def hdr(self, hdr):
        """Sets the hdr of this EntityFile.


        :param hdr: The hdr of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._hdr = hdr

    @property
    def hash(self):
        """Gets the hash of this EntityFile.  # noqa: E501


        :return: The hash of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this EntityFile.


        :param hash: The hash of this EntityFile.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def height(self):
        """Gets the height of this EntityFile.  # noqa: E501


        :return: The height of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this EntityFile.


        :param height: The height of this EntityFile.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def instance_id(self):
        """Gets the instance_id of this EntityFile.  # noqa: E501


        :return: The instance_id of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EntityFile.


        :param instance_id: The instance_id of this EntityFile.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def luminance(self):
        """Gets the luminance of this EntityFile.  # noqa: E501


        :return: The luminance of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._luminance

    @luminance.setter
    def luminance(self, luminance):
        """Sets the luminance of this EntityFile.


        :param luminance: The luminance of this EntityFile.  # noqa: E501
        :type: str
        """

        self._luminance = luminance

    @property
    def main_color(self):
        """Gets the main_color of this EntityFile.  # noqa: E501


        :return: The main_color of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._main_color

    @main_color.setter
    def main_color(self, main_color):
        """Sets the main_color of this EntityFile.


        :param main_color: The main_color of this EntityFile.  # noqa: E501
        :type: str
        """

        self._main_color = main_color

    @property
    def media_id(self):
        """Gets the media_id of this EntityFile.  # noqa: E501


        :return: The media_id of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this EntityFile.


        :param media_id: The media_id of this EntityFile.  # noqa: E501
        :type: str
        """

        self._media_id = media_id

    @property
    def media_type(self):
        """Gets the media_type of this EntityFile.  # noqa: E501


        :return: The media_type of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this EntityFile.


        :param media_type: The media_type of this EntityFile.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def media_utc(self):
        """Gets the media_utc of this EntityFile.  # noqa: E501


        :return: The media_utc of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._media_utc

    @media_utc.setter
    def media_utc(self, media_utc):
        """Sets the media_utc of this EntityFile.


        :param media_utc: The media_utc of this EntityFile.  # noqa: E501
        :type: int
        """

        self._media_utc = media_utc

    @property
    def mime(self):
        """Gets the mime of this EntityFile.  # noqa: E501


        :return: The mime of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._mime

    @mime.setter
    def mime(self, mime):
        """Sets the mime of this EntityFile.


        :param mime: The mime of this EntityFile.  # noqa: E501
        :type: str
        """

        self._mime = mime

    @property
    def missing(self):
        """Gets the missing of this EntityFile.  # noqa: E501


        :return: The missing of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this EntityFile.


        :param missing: The missing of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._missing = missing

    @property
    def mod_time(self):
        """Gets the mod_time of this EntityFile.  # noqa: E501


        :return: The mod_time of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """Sets the mod_time of this EntityFile.


        :param mod_time: The mod_time of this EntityFile.  # noqa: E501
        :type: int
        """

        self._mod_time = mod_time

    @property
    def name(self):
        """Gets the name of this EntityFile.  # noqa: E501


        :return: The name of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityFile.


        :param name: The name of this EntityFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def orientation(self):
        """Gets the orientation of this EntityFile.  # noqa: E501


        :return: The orientation of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this EntityFile.


        :param orientation: The orientation of this EntityFile.  # noqa: E501
        :type: int
        """

        self._orientation = orientation

    @property
    def orientation_src(self):
        """Gets the orientation_src of this EntityFile.  # noqa: E501


        :return: The orientation_src of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._orientation_src

    @orientation_src.setter
    def orientation_src(self, orientation_src):
        """Sets the orientation_src of this EntityFile.


        :param orientation_src: The orientation_src of this EntityFile.  # noqa: E501
        :type: str
        """

        self._orientation_src = orientation_src

    @property
    def original_name(self):
        """Gets the original_name of this EntityFile.  # noqa: E501


        :return: The original_name of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this EntityFile.


        :param original_name: The original_name of this EntityFile.  # noqa: E501
        :type: str
        """

        self._original_name = original_name

    @property
    def photo_uid(self):
        """Gets the photo_uid of this EntityFile.  # noqa: E501


        :return: The photo_uid of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._photo_uid

    @photo_uid.setter
    def photo_uid(self, photo_uid):
        """Sets the photo_uid of this EntityFile.


        :param photo_uid: The photo_uid of this EntityFile.  # noqa: E501
        :type: str
        """

        self._photo_uid = photo_uid

    @property
    def portrait(self):
        """Gets the portrait of this EntityFile.  # noqa: E501


        :return: The portrait of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._portrait

    @portrait.setter
    def portrait(self, portrait):
        """Sets the portrait of this EntityFile.


        :param portrait: The portrait of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._portrait = portrait

    @property
    def primary(self):
        """Gets the primary of this EntityFile.  # noqa: E501


        :return: The primary of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this EntityFile.


        :param primary: The primary of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    @property
    def projection(self):
        """Gets the projection of this EntityFile.  # noqa: E501


        :return: The projection of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._projection

    @projection.setter
    def projection(self, projection):
        """Sets the projection of this EntityFile.


        :param projection: The projection of this EntityFile.  # noqa: E501
        :type: str
        """

        self._projection = projection

    @property
    def published_at(self):
        """Gets the published_at of this EntityFile.  # noqa: E501


        :return: The published_at of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this EntityFile.


        :param published_at: The published_at of this EntityFile.  # noqa: E501
        :type: str
        """

        self._published_at = published_at

    @property
    def root(self):
        """Gets the root of this EntityFile.  # noqa: E501


        :return: The root of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this EntityFile.


        :param root: The root of this EntityFile.  # noqa: E501
        :type: str
        """

        self._root = root

    @property
    def sidecar(self):
        """Gets the sidecar of this EntityFile.  # noqa: E501


        :return: The sidecar of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._sidecar

    @sidecar.setter
    def sidecar(self, sidecar):
        """Sets the sidecar of this EntityFile.


        :param sidecar: The sidecar of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._sidecar = sidecar

    @property
    def size(self):
        """Gets the size of this EntityFile.  # noqa: E501


        :return: The size of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EntityFile.


        :param size: The size of this EntityFile.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def software(self):
        """Gets the software of this EntityFile.  # noqa: E501


        :return: The software of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this EntityFile.


        :param software: The software of this EntityFile.  # noqa: E501
        :type: str
        """

        self._software = software

    @property
    def taken_at(self):
        """Gets the taken_at of this EntityFile.  # noqa: E501


        :return: The taken_at of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._taken_at

    @taken_at.setter
    def taken_at(self, taken_at):
        """Sets the taken_at of this EntityFile.


        :param taken_at: The taken_at of this EntityFile.  # noqa: E501
        :type: str
        """

        self._taken_at = taken_at

    @property
    def time_index(self):
        """Gets the time_index of this EntityFile.  # noqa: E501


        :return: The time_index of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._time_index

    @time_index.setter
    def time_index(self, time_index):
        """Sets the time_index of this EntityFile.


        :param time_index: The time_index of this EntityFile.  # noqa: E501
        :type: str
        """

        self._time_index = time_index

    @property
    def uid(self):
        """Gets the uid of this EntityFile.  # noqa: E501


        :return: The uid of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EntityFile.


        :param uid: The uid of this EntityFile.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def updated_at(self):
        """Gets the updated_at of this EntityFile.  # noqa: E501


        :return: The updated_at of this EntityFile.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EntityFile.


        :param updated_at: The updated_at of this EntityFile.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def updated_in(self):
        """Gets the updated_in of this EntityFile.  # noqa: E501


        :return: The updated_in of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._updated_in

    @updated_in.setter
    def updated_in(self, updated_in):
        """Sets the updated_in of this EntityFile.


        :param updated_in: The updated_in of this EntityFile.  # noqa: E501
        :type: int
        """

        self._updated_in = updated_in

    @property
    def video(self):
        """Gets the video of this EntityFile.  # noqa: E501


        :return: The video of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this EntityFile.


        :param video: The video of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._video = video

    @property
    def watermark(self):
        """Gets the watermark of this EntityFile.  # noqa: E501


        :return: The watermark of this EntityFile.  # noqa: E501
        :rtype: bool
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """Sets the watermark of this EntityFile.


        :param watermark: The watermark of this EntityFile.  # noqa: E501
        :type: bool
        """

        self._watermark = watermark

    @property
    def width(self):
        """Gets the width of this EntityFile.  # noqa: E501


        :return: The width of this EntityFile.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this EntityFile.


        :param width: The width of this EntityFile.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(EntityFile, dict):
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
        if not isinstance(other, EntityFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityFile):
            return True

        return self.to_dict() != other.to_dict()

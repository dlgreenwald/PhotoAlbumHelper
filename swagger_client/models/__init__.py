# coding: utf-8

# flake8: noqa
"""
    PhotoPrism API

    API request bodies and responses are usually JSON-encoded, except for binary data and some of the OAuth2 endpoints. Note that the `Content-Type` header must be set to `application/json` for this, as the request may otherwise fail with error 400. When clients have a valid access token, e.g. obtained through the `POST /api/v1/session` or `POST /api/v1/oauth/token` endpoint, they can use a standard Bearer Authorization header to authenticate their requests. Submitting the access token with a custom `X-Auth-Token` header is supported as well.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.acl_grant import AclGrant
from swagger_client.models.acl_grants import AclGrants
from swagger_client.models.config_category_label import ConfigCategoryLabel
from swagger_client.models.config_client_config import ConfigClientConfig
from swagger_client.models.config_client_counts import ConfigClientCounts
from swagger_client.models.config_client_disable import ConfigClientDisable
from swagger_client.models.config_client_position import ConfigClientPosition
from swagger_client.models.config_map import ConfigMap
from swagger_client.models.config_options import ConfigOptions
from swagger_client.models.config_thumb_size import ConfigThumbSize
from swagger_client.models.customize_download_name import CustomizeDownloadName
from swagger_client.models.customize_download_settings import CustomizeDownloadSettings
from swagger_client.models.customize_feature_settings import CustomizeFeatureSettings
from swagger_client.models.customize_import_settings import CustomizeImportSettings
from swagger_client.models.customize_index_settings import CustomizeIndexSettings
from swagger_client.models.customize_maps_settings import CustomizeMapsSettings
from swagger_client.models.customize_search_settings import CustomizeSearchSettings
from swagger_client.models.customize_settings import CustomizeSettings
from swagger_client.models.customize_share_settings import CustomizeShareSettings
from swagger_client.models.customize_stack_settings import CustomizeStackSettings
from swagger_client.models.customize_template_settings import CustomizeTemplateSettings
from swagger_client.models.customize_ui_settings import CustomizeUISettings
from swagger_client.models.entity_album import EntityAlbum
from swagger_client.models.entity_camera import EntityCamera
from swagger_client.models.entity_cell import EntityCell
from swagger_client.models.entity_country import EntityCountry
from swagger_client.models.entity_details import EntityDetails
from swagger_client.models.entity_error import EntityError
from swagger_client.models.entity_face import EntityFace
from swagger_client.models.entity_file import EntityFile
from swagger_client.models.entity_label import EntityLabel
from swagger_client.models.entity_lens import EntityLens
from swagger_client.models.entity_link import EntityLink
from swagger_client.models.entity_marker import EntityMarker
from swagger_client.models.entity_person import EntityPerson
from swagger_client.models.entity_photo import EntityPhoto
from swagger_client.models.entity_photo_label import EntityPhotoLabel
from swagger_client.models.entity_place import EntityPlace
from swagger_client.models.entity_service import EntityService
from swagger_client.models.entity_session import EntitySession
from swagger_client.models.entity_session_data import EntitySessionData
from swagger_client.models.entity_settings import EntitySettings
from swagger_client.models.entity_subject import EntitySubject
from swagger_client.models.entity_user import EntityUser
from swagger_client.models.entity_user_details import EntityUserDetails
from swagger_client.models.env_resources import EnvResources
from swagger_client.models.env_resources_memory import EnvResourcesMemory
from swagger_client.models.form_album import FormAlbum
from swagger_client.models.form_details import FormDetails
from swagger_client.models.form_face import FormFace
from swagger_client.models.form_file import FormFile
from swagger_client.models.form_label import FormLabel
from swagger_client.models.form_link import FormLink
from swagger_client.models.form_marker import FormMarker
from swagger_client.models.form_photo import FormPhoto
from swagger_client.models.form_selection import FormSelection
from swagger_client.models.form_service import FormService
from swagger_client.models.form_subject import FormSubject
from swagger_client.models.gin_h import GinH
from swagger_client.models.i18n_response import I18nResponse
from swagger_client.models.search_album import SearchAlbum
from swagger_client.models.search_face import SearchFace
from swagger_client.models.search_geo_result import SearchGeoResult
from swagger_client.models.search_label import SearchLabel
from swagger_client.models.search_photo import SearchPhoto
from swagger_client.models.search_subject import SearchSubject
from swagger_client.models.sql_null_time import SqlNullTime
from swagger_client.models.time_duration import TimeDuration

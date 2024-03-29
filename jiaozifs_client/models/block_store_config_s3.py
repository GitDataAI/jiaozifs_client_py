# coding: utf-8

"""
    jiaozifs API

    jiaozifs HTTP API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BlockStoreConfigS3(object):
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
        'credentials': 'Credential',
        'web_identity': 'WebIdentity',
        'discover_bucket_region': 'bool',
        'endpoint': 'str',
        'force_path_style': 'bool',
        'region': 'str'
    }

    attribute_map = {
        'credentials': 'credentials',
        'web_identity': 'web_identity',
        'discover_bucket_region': 'discover_bucket_region',
        'endpoint': 'endpoint',
        'force_path_style': 'force_path_style',
        'region': 'region'
    }

    def __init__(self, credentials=None, web_identity=None, discover_bucket_region=None, endpoint=None, force_path_style=None, region=None):  # noqa: E501
        """BlockStoreConfigS3 - a model defined in Swagger"""  # noqa: E501
        self._credentials = None
        self._web_identity = None
        self._discover_bucket_region = None
        self._endpoint = None
        self._force_path_style = None
        self._region = None
        self.discriminator = None
        self.credentials = credentials
        if web_identity is not None:
            self.web_identity = web_identity
        self.discover_bucket_region = discover_bucket_region
        self.endpoint = endpoint
        if force_path_style is not None:
            self.force_path_style = force_path_style
        if region is not None:
            self.region = region

    @property
    def credentials(self):
        """Gets the credentials of this BlockStoreConfigS3.  # noqa: E501


        :return: The credentials of this BlockStoreConfigS3.  # noqa: E501
        :rtype: Credential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this BlockStoreConfigS3.


        :param credentials: The credentials of this BlockStoreConfigS3.  # noqa: E501
        :type: Credential
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def web_identity(self):
        """Gets the web_identity of this BlockStoreConfigS3.  # noqa: E501


        :return: The web_identity of this BlockStoreConfigS3.  # noqa: E501
        :rtype: WebIdentity
        """
        return self._web_identity

    @web_identity.setter
    def web_identity(self, web_identity):
        """Sets the web_identity of this BlockStoreConfigS3.


        :param web_identity: The web_identity of this BlockStoreConfigS3.  # noqa: E501
        :type: WebIdentity
        """

        self._web_identity = web_identity

    @property
    def discover_bucket_region(self):
        """Gets the discover_bucket_region of this BlockStoreConfigS3.  # noqa: E501


        :return: The discover_bucket_region of this BlockStoreConfigS3.  # noqa: E501
        :rtype: bool
        """
        return self._discover_bucket_region

    @discover_bucket_region.setter
    def discover_bucket_region(self, discover_bucket_region):
        """Sets the discover_bucket_region of this BlockStoreConfigS3.


        :param discover_bucket_region: The discover_bucket_region of this BlockStoreConfigS3.  # noqa: E501
        :type: bool
        """
        if discover_bucket_region is None:
            raise ValueError("Invalid value for `discover_bucket_region`, must not be `None`")  # noqa: E501

        self._discover_bucket_region = discover_bucket_region

    @property
    def endpoint(self):
        """Gets the endpoint of this BlockStoreConfigS3.  # noqa: E501


        :return: The endpoint of this BlockStoreConfigS3.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this BlockStoreConfigS3.


        :param endpoint: The endpoint of this BlockStoreConfigS3.  # noqa: E501
        :type: str
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501

        self._endpoint = endpoint

    @property
    def force_path_style(self):
        """Gets the force_path_style of this BlockStoreConfigS3.  # noqa: E501


        :return: The force_path_style of this BlockStoreConfigS3.  # noqa: E501
        :rtype: bool
        """
        return self._force_path_style

    @force_path_style.setter
    def force_path_style(self, force_path_style):
        """Sets the force_path_style of this BlockStoreConfigS3.


        :param force_path_style: The force_path_style of this BlockStoreConfigS3.  # noqa: E501
        :type: bool
        """

        self._force_path_style = force_path_style

    @property
    def region(self):
        """Gets the region of this BlockStoreConfigS3.  # noqa: E501


        :return: The region of this BlockStoreConfigS3.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BlockStoreConfigS3.


        :param region: The region of this BlockStoreConfigS3.  # noqa: E501
        :type: str
        """

        self._region = region

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
        if issubclass(BlockStoreConfigS3, dict):
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
        if not isinstance(other, BlockStoreConfigS3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

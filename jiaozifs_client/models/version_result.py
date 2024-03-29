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

class VersionResult(object):
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
        'version': 'str',
        'api_version': 'str',
        'latest_version': 'str'
    }

    attribute_map = {
        'version': 'version',
        'api_version': 'api_version',
        'latest_version': 'latest_version'
    }

    def __init__(self, version=None, api_version=None, latest_version=None):  # noqa: E501
        """VersionResult - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._api_version = None
        self._latest_version = None
        self.discriminator = None
        self.version = version
        self.api_version = api_version
        if latest_version is not None:
            self.latest_version = latest_version

    @property
    def version(self):
        """Gets the version of this VersionResult.  # noqa: E501

        program version  # noqa: E501

        :return: The version of this VersionResult.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionResult.

        program version  # noqa: E501

        :param version: The version of this VersionResult.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def api_version(self):
        """Gets the api_version of this VersionResult.  # noqa: E501

        runtime version  # noqa: E501

        :return: The api_version of this VersionResult.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this VersionResult.

        runtime version  # noqa: E501

        :param api_version: The api_version of this VersionResult.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def latest_version(self):
        """Gets the latest_version of this VersionResult.  # noqa: E501


        :return: The latest_version of this VersionResult.  # noqa: E501
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this VersionResult.


        :param latest_version: The latest_version of this VersionResult.  # noqa: E501
        :type: str
        """

        self._latest_version = latest_version

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
        if issubclass(VersionResult, dict):
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
        if not isinstance(other, VersionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

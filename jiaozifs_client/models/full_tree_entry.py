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

class FullTreeEntry(object):
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
        'name': 'str',
        'hash': 'str',
        'is_dir': 'bool',
        'size': 'int',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'name': 'name',
        'hash': 'hash',
        'is_dir': 'is_dir',
        'size': 'size',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, name=None, hash=None, is_dir=None, size=None, created_at=None, updated_at=None):  # noqa: E501
        """FullTreeEntry - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._hash = None
        self._is_dir = None
        self._size = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.name = name
        self.hash = hash
        self.is_dir = is_dir
        self.size = size
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this FullTreeEntry.  # noqa: E501


        :return: The name of this FullTreeEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FullTreeEntry.


        :param name: The name of this FullTreeEntry.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def hash(self):
        """Gets the hash of this FullTreeEntry.  # noqa: E501


        :return: The hash of this FullTreeEntry.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this FullTreeEntry.


        :param hash: The hash of this FullTreeEntry.  # noqa: E501
        :type: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def is_dir(self):
        """Gets the is_dir of this FullTreeEntry.  # noqa: E501


        :return: The is_dir of this FullTreeEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_dir

    @is_dir.setter
    def is_dir(self, is_dir):
        """Sets the is_dir of this FullTreeEntry.


        :param is_dir: The is_dir of this FullTreeEntry.  # noqa: E501
        :type: bool
        """
        if is_dir is None:
            raise ValueError("Invalid value for `is_dir`, must not be `None`")  # noqa: E501

        self._is_dir = is_dir

    @property
    def size(self):
        """Gets the size of this FullTreeEntry.  # noqa: E501


        :return: The size of this FullTreeEntry.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FullTreeEntry.


        :param size: The size of this FullTreeEntry.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def created_at(self):
        """Gets the created_at of this FullTreeEntry.  # noqa: E501


        :return: The created_at of this FullTreeEntry.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FullTreeEntry.


        :param created_at: The created_at of this FullTreeEntry.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FullTreeEntry.  # noqa: E501


        :return: The updated_at of this FullTreeEntry.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FullTreeEntry.


        :param updated_at: The updated_at of this FullTreeEntry.  # noqa: E501
        :type: int
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

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
        if issubclass(FullTreeEntry, dict):
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
        if not isinstance(other, FullTreeEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

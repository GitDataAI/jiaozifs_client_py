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

class Wip(object):
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
        'id': 'str',
        'current_tree': 'str',
        'base_commit': 'str',
        'repository_id': 'str',
        'ref_id': 'str',
        'state': 'int',
        'creator_id': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'current_tree': 'current_tree',
        'base_commit': 'base_commit',
        'repository_id': 'repository_id',
        'ref_id': 'ref_id',
        'state': 'state',
        'creator_id': 'creator_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, current_tree=None, base_commit=None, repository_id=None, ref_id=None, state=None, creator_id=None, created_at=None, updated_at=None):  # noqa: E501
        """Wip - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._current_tree = None
        self._base_commit = None
        self._repository_id = None
        self._ref_id = None
        self._state = None
        self._creator_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        self.current_tree = current_tree
        self.base_commit = base_commit
        self.repository_id = repository_id
        self.ref_id = ref_id
        self.state = state
        self.creator_id = creator_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Wip.  # noqa: E501


        :return: The id of this Wip.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Wip.


        :param id: The id of this Wip.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def current_tree(self):
        """Gets the current_tree of this Wip.  # noqa: E501


        :return: The current_tree of this Wip.  # noqa: E501
        :rtype: str
        """
        return self._current_tree

    @current_tree.setter
    def current_tree(self, current_tree):
        """Sets the current_tree of this Wip.


        :param current_tree: The current_tree of this Wip.  # noqa: E501
        :type: str
        """
        if current_tree is None:
            raise ValueError("Invalid value for `current_tree`, must not be `None`")  # noqa: E501

        self._current_tree = current_tree

    @property
    def base_commit(self):
        """Gets the base_commit of this Wip.  # noqa: E501


        :return: The base_commit of this Wip.  # noqa: E501
        :rtype: str
        """
        return self._base_commit

    @base_commit.setter
    def base_commit(self, base_commit):
        """Sets the base_commit of this Wip.


        :param base_commit: The base_commit of this Wip.  # noqa: E501
        :type: str
        """
        if base_commit is None:
            raise ValueError("Invalid value for `base_commit`, must not be `None`")  # noqa: E501

        self._base_commit = base_commit

    @property
    def repository_id(self):
        """Gets the repository_id of this Wip.  # noqa: E501


        :return: The repository_id of this Wip.  # noqa: E501
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this Wip.


        :param repository_id: The repository_id of this Wip.  # noqa: E501
        :type: str
        """
        if repository_id is None:
            raise ValueError("Invalid value for `repository_id`, must not be `None`")  # noqa: E501

        self._repository_id = repository_id

    @property
    def ref_id(self):
        """Gets the ref_id of this Wip.  # noqa: E501


        :return: The ref_id of this Wip.  # noqa: E501
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this Wip.


        :param ref_id: The ref_id of this Wip.  # noqa: E501
        :type: str
        """
        if ref_id is None:
            raise ValueError("Invalid value for `ref_id`, must not be `None`")  # noqa: E501

        self._ref_id = ref_id

    @property
    def state(self):
        """Gets the state of this Wip.  # noqa: E501


        :return: The state of this Wip.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Wip.


        :param state: The state of this Wip.  # noqa: E501
        :type: int
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def creator_id(self):
        """Gets the creator_id of this Wip.  # noqa: E501


        :return: The creator_id of this Wip.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Wip.


        :param creator_id: The creator_id of this Wip.  # noqa: E501
        :type: str
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def created_at(self):
        """Gets the created_at of this Wip.  # noqa: E501


        :return: The created_at of this Wip.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Wip.


        :param created_at: The created_at of this Wip.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Wip.  # noqa: E501


        :return: The updated_at of this Wip.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Wip.


        :param updated_at: The updated_at of this Wip.  # noqa: E501
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
        if issubclass(Wip, dict):
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
        if not isinstance(other, Wip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class LoginConfig(object):
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
        'rbac': 'str',
        'login_url': 'str',
        'login_failed_message': 'str',
        'fallback_login_url': 'str',
        'fallback_login_label': 'str',
        'login_cookie_names': 'list[str]',
        'logout_url': 'str'
    }

    attribute_map = {
        'rbac': 'RBAC',
        'login_url': 'login_url',
        'login_failed_message': 'login_failed_message',
        'fallback_login_url': 'fallback_login_url',
        'fallback_login_label': 'fallback_login_label',
        'login_cookie_names': 'login_cookie_names',
        'logout_url': 'logout_url'
    }

    def __init__(self, rbac=None, login_url=None, login_failed_message=None, fallback_login_url=None, fallback_login_label=None, login_cookie_names=None, logout_url=None):  # noqa: E501
        """LoginConfig - a model defined in Swagger"""  # noqa: E501
        self._rbac = None
        self._login_url = None
        self._login_failed_message = None
        self._fallback_login_url = None
        self._fallback_login_label = None
        self._login_cookie_names = None
        self._logout_url = None
        self.discriminator = None
        if rbac is not None:
            self.rbac = rbac
        self.login_url = login_url
        if login_failed_message is not None:
            self.login_failed_message = login_failed_message
        if fallback_login_url is not None:
            self.fallback_login_url = fallback_login_url
        if fallback_login_label is not None:
            self.fallback_login_label = fallback_login_label
        self.login_cookie_names = login_cookie_names
        self.logout_url = logout_url

    @property
    def rbac(self):
        """Gets the rbac of this LoginConfig.  # noqa: E501

        RBAC will remain enabled on GUI if \"external\".  That only works with an external auth service.   # noqa: E501

        :return: The rbac of this LoginConfig.  # noqa: E501
        :rtype: str
        """
        return self._rbac

    @rbac.setter
    def rbac(self, rbac):
        """Sets the rbac of this LoginConfig.

        RBAC will remain enabled on GUI if \"external\".  That only works with an external auth service.   # noqa: E501

        :param rbac: The rbac of this LoginConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["simplified", "external"]  # noqa: E501
        if rbac not in allowed_values:
            raise ValueError(
                "Invalid value for `rbac` ({0}), must be one of {1}"  # noqa: E501
                .format(rbac, allowed_values)
            )

        self._rbac = rbac

    @property
    def login_url(self):
        """Gets the login_url of this LoginConfig.  # noqa: E501

        primary URL to use for login.  # noqa: E501

        :return: The login_url of this LoginConfig.  # noqa: E501
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        """Sets the login_url of this LoginConfig.

        primary URL to use for login.  # noqa: E501

        :param login_url: The login_url of this LoginConfig.  # noqa: E501
        :type: str
        """
        if login_url is None:
            raise ValueError("Invalid value for `login_url`, must not be `None`")  # noqa: E501

        self._login_url = login_url

    @property
    def login_failed_message(self):
        """Gets the login_failed_message of this LoginConfig.  # noqa: E501

        message to display to users who fail to login; a full sentence that is rendered in HTML and may contain a link to a secondary login method   # noqa: E501

        :return: The login_failed_message of this LoginConfig.  # noqa: E501
        :rtype: str
        """
        return self._login_failed_message

    @login_failed_message.setter
    def login_failed_message(self, login_failed_message):
        """Sets the login_failed_message of this LoginConfig.

        message to display to users who fail to login; a full sentence that is rendered in HTML and may contain a link to a secondary login method   # noqa: E501

        :param login_failed_message: The login_failed_message of this LoginConfig.  # noqa: E501
        :type: str
        """

        self._login_failed_message = login_failed_message

    @property
    def fallback_login_url(self):
        """Gets the fallback_login_url of this LoginConfig.  # noqa: E501

        secondary URL to offer users to use for login.  # noqa: E501

        :return: The fallback_login_url of this LoginConfig.  # noqa: E501
        :rtype: str
        """
        return self._fallback_login_url

    @fallback_login_url.setter
    def fallback_login_url(self, fallback_login_url):
        """Sets the fallback_login_url of this LoginConfig.

        secondary URL to offer users to use for login.  # noqa: E501

        :param fallback_login_url: The fallback_login_url of this LoginConfig.  # noqa: E501
        :type: str
        """

        self._fallback_login_url = fallback_login_url

    @property
    def fallback_login_label(self):
        """Gets the fallback_login_label of this LoginConfig.  # noqa: E501

        label to place on fallback_login_url.  # noqa: E501

        :return: The fallback_login_label of this LoginConfig.  # noqa: E501
        :rtype: str
        """
        return self._fallback_login_label

    @fallback_login_label.setter
    def fallback_login_label(self, fallback_login_label):
        """Sets the fallback_login_label of this LoginConfig.

        label to place on fallback_login_url.  # noqa: E501

        :param fallback_login_label: The fallback_login_label of this LoginConfig.  # noqa: E501
        :type: str
        """

        self._fallback_login_label = fallback_login_label

    @property
    def login_cookie_names(self):
        """Gets the login_cookie_names of this LoginConfig.  # noqa: E501

        cookie names used to store JWT  # noqa: E501

        :return: The login_cookie_names of this LoginConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._login_cookie_names

    @login_cookie_names.setter
    def login_cookie_names(self, login_cookie_names):
        """Sets the login_cookie_names of this LoginConfig.

        cookie names used to store JWT  # noqa: E501

        :param login_cookie_names: The login_cookie_names of this LoginConfig.  # noqa: E501
        :type: list[str]
        """
        if login_cookie_names is None:
            raise ValueError("Invalid value for `login_cookie_names`, must not be `None`")  # noqa: E501

        self._login_cookie_names = login_cookie_names

    @property
    def logout_url(self):
        """Gets the logout_url of this LoginConfig.  # noqa: E501

        URL to use for logging out.  # noqa: E501

        :return: The logout_url of this LoginConfig.  # noqa: E501
        :rtype: str
        """
        return self._logout_url

    @logout_url.setter
    def logout_url(self, logout_url):
        """Sets the logout_url of this LoginConfig.

        URL to use for logging out.  # noqa: E501

        :param logout_url: The logout_url of this LoginConfig.  # noqa: E501
        :type: str
        """
        if logout_url is None:
            raise ValueError("Invalid value for `logout_url`, must not be `None`")  # noqa: E501

        self._logout_url = logout_url

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
        if issubclass(LoginConfig, dict):
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
        if not isinstance(other, LoginConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

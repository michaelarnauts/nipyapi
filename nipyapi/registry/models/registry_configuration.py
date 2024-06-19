# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.26.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RegistryConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'supports_managed_authorizer': 'bool',
        'supports_configurable_authorizer': 'bool',
        'supports_configurable_users_and_groups': 'bool'
    }

    attribute_map = {
        'supports_managed_authorizer': 'supportsManagedAuthorizer',
        'supports_configurable_authorizer': 'supportsConfigurableAuthorizer',
        'supports_configurable_users_and_groups': 'supportsConfigurableUsersAndGroups'
    }

    def __init__(self, supports_managed_authorizer=None, supports_configurable_authorizer=None, supports_configurable_users_and_groups=None):
        """
        RegistryConfiguration - a model defined in Swagger
        """

        self._supports_managed_authorizer = None
        self._supports_configurable_authorizer = None
        self._supports_configurable_users_and_groups = None

        if supports_managed_authorizer is not None:
          self.supports_managed_authorizer = supports_managed_authorizer
        if supports_configurable_authorizer is not None:
          self.supports_configurable_authorizer = supports_configurable_authorizer
        if supports_configurable_users_and_groups is not None:
          self.supports_configurable_users_and_groups = supports_configurable_users_and_groups

    @property
    def supports_managed_authorizer(self):
        """
        Gets the supports_managed_authorizer of this RegistryConfiguration.
        Whether this NiFi Registry supports a managed authorizer. Managed authorizers can visualize users, groups, and policies in the UI.

        :return: The supports_managed_authorizer of this RegistryConfiguration.
        :rtype: bool
        """
        return self._supports_managed_authorizer

    @supports_managed_authorizer.setter
    def supports_managed_authorizer(self, supports_managed_authorizer):
        """
        Sets the supports_managed_authorizer of this RegistryConfiguration.
        Whether this NiFi Registry supports a managed authorizer. Managed authorizers can visualize users, groups, and policies in the UI.

        :param supports_managed_authorizer: The supports_managed_authorizer of this RegistryConfiguration.
        :type: bool
        """

        self._supports_managed_authorizer = supports_managed_authorizer

    @property
    def supports_configurable_authorizer(self):
        """
        Gets the supports_configurable_authorizer of this RegistryConfiguration.
        Whether this NiFi Registry supports a configurable authorizer.

        :return: The supports_configurable_authorizer of this RegistryConfiguration.
        :rtype: bool
        """
        return self._supports_configurable_authorizer

    @supports_configurable_authorizer.setter
    def supports_configurable_authorizer(self, supports_configurable_authorizer):
        """
        Sets the supports_configurable_authorizer of this RegistryConfiguration.
        Whether this NiFi Registry supports a configurable authorizer.

        :param supports_configurable_authorizer: The supports_configurable_authorizer of this RegistryConfiguration.
        :type: bool
        """

        self._supports_configurable_authorizer = supports_configurable_authorizer

    @property
    def supports_configurable_users_and_groups(self):
        """
        Gets the supports_configurable_users_and_groups of this RegistryConfiguration.
        Whether this NiFi Registry supports configurable users and groups.

        :return: The supports_configurable_users_and_groups of this RegistryConfiguration.
        :rtype: bool
        """
        return self._supports_configurable_users_and_groups

    @supports_configurable_users_and_groups.setter
    def supports_configurable_users_and_groups(self, supports_configurable_users_and_groups):
        """
        Sets the supports_configurable_users_and_groups of this RegistryConfiguration.
        Whether this NiFi Registry supports configurable users and groups.

        :param supports_configurable_users_and_groups: The supports_configurable_users_and_groups of this RegistryConfiguration.
        :type: bool
        """

        self._supports_configurable_users_and_groups = supports_configurable_users_and_groups

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RegistryConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class VersionedPropertyDescriptor(object):
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
        'name': 'str',
        'display_name': 'str',
        'identifies_controller_service': 'bool',
        'sensitive': 'bool',
        'resource_definition': 'VersionedResourceDefinition'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'identifies_controller_service': 'identifiesControllerService',
        'sensitive': 'sensitive',
        'resource_definition': 'resourceDefinition'
    }

    def __init__(self, name=None, display_name=None, identifies_controller_service=None, sensitive=None, resource_definition=None):
        """
        VersionedPropertyDescriptor - a model defined in Swagger
        """

        self._name = None
        self._display_name = None
        self._identifies_controller_service = None
        self._sensitive = None
        self._resource_definition = None

        if name is not None:
          self.name = name
        if display_name is not None:
          self.display_name = display_name
        if identifies_controller_service is not None:
          self.identifies_controller_service = identifies_controller_service
        if sensitive is not None:
          self.sensitive = sensitive
        if resource_definition is not None:
          self.resource_definition = resource_definition

    @property
    def name(self):
        """
        Gets the name of this VersionedPropertyDescriptor.
        The name of the property

        :return: The name of this VersionedPropertyDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VersionedPropertyDescriptor.
        The name of the property

        :param name: The name of this VersionedPropertyDescriptor.
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this VersionedPropertyDescriptor.
        The display name of the property

        :return: The display_name of this VersionedPropertyDescriptor.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VersionedPropertyDescriptor.
        The display name of the property

        :param display_name: The display_name of this VersionedPropertyDescriptor.
        :type: str
        """

        self._display_name = display_name

    @property
    def identifies_controller_service(self):
        """
        Gets the identifies_controller_service of this VersionedPropertyDescriptor.
        Whether or not the property provides the identifier of a Controller Service

        :return: The identifies_controller_service of this VersionedPropertyDescriptor.
        :rtype: bool
        """
        return self._identifies_controller_service

    @identifies_controller_service.setter
    def identifies_controller_service(self, identifies_controller_service):
        """
        Sets the identifies_controller_service of this VersionedPropertyDescriptor.
        Whether or not the property provides the identifier of a Controller Service

        :param identifies_controller_service: The identifies_controller_service of this VersionedPropertyDescriptor.
        :type: bool
        """

        self._identifies_controller_service = identifies_controller_service

    @property
    def sensitive(self):
        """
        Gets the sensitive of this VersionedPropertyDescriptor.
        Whether or not the property is considered sensitive

        :return: The sensitive of this VersionedPropertyDescriptor.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """
        Sets the sensitive of this VersionedPropertyDescriptor.
        Whether or not the property is considered sensitive

        :param sensitive: The sensitive of this VersionedPropertyDescriptor.
        :type: bool
        """

        self._sensitive = sensitive

    @property
    def resource_definition(self):
        """
        Gets the resource_definition of this VersionedPropertyDescriptor.
        Returns the Resource Definition that defines which type(s) of resource(s) this property references, if any

        :return: The resource_definition of this VersionedPropertyDescriptor.
        :rtype: VersionedResourceDefinition
        """
        return self._resource_definition

    @resource_definition.setter
    def resource_definition(self, resource_definition):
        """
        Sets the resource_definition of this VersionedPropertyDescriptor.
        Returns the Resource Definition that defines which type(s) of resource(s) this property references, if any

        :param resource_definition: The resource_definition of this VersionedPropertyDescriptor.
        :type: VersionedResourceDefinition
        """

        self._resource_definition = resource_definition

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
        if not isinstance(other, VersionedPropertyDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

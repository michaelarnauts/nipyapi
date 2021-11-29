# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.15.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Relationship(object):
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
        'description': 'str',
        'auto_terminated': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'auto_terminated': 'autoTerminated'
    }

    def __init__(self, name=None, description=None, auto_terminated=None):
        """
        Relationship - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._auto_terminated = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if auto_terminated is not None:
          self.auto_terminated = auto_terminated

    @property
    def name(self):
        """
        Gets the name of this Relationship.
        The name of the relationship

        :return: The name of this Relationship.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Relationship.
        The name of the relationship

        :param name: The name of this Relationship.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Relationship.
        The description of the relationship

        :return: The description of this Relationship.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Relationship.
        The description of the relationship

        :param description: The description of this Relationship.
        :type: str
        """

        self._description = description

    @property
    def auto_terminated(self):
        """
        Gets the auto_terminated of this Relationship.
        Whether or not the relationship is auto-terminated by default

        :return: The auto_terminated of this Relationship.
        :rtype: bool
        """
        return self._auto_terminated

    @auto_terminated.setter
    def auto_terminated(self, auto_terminated):
        """
        Sets the auto_terminated of this Relationship.
        Whether or not the relationship is auto-terminated by default

        :param auto_terminated: The auto_terminated of this Relationship.
        :type: bool
        """

        self._auto_terminated = auto_terminated

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
        if not isinstance(other, Relationship):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

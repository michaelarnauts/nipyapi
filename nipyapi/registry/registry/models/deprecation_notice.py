# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 0.8.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeprecationNotice(object):
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
        'reason': 'str',
        'alternatives': 'list[str]'
    }

    attribute_map = {
        'reason': 'reason',
        'alternatives': 'alternatives'
    }

    def __init__(self, reason=None, alternatives=None):
        """
        DeprecationNotice - a model defined in Swagger
        """

        self._reason = None
        self._alternatives = None

        if reason is not None:
          self.reason = reason
        if alternatives is not None:
          self.alternatives = alternatives

    @property
    def reason(self):
        """
        Gets the reason of this DeprecationNotice.
        The reason for the deprecation

        :return: The reason of this DeprecationNotice.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this DeprecationNotice.
        The reason for the deprecation

        :param reason: The reason of this DeprecationNotice.
        :type: str
        """

        self._reason = reason

    @property
    def alternatives(self):
        """
        Gets the alternatives of this DeprecationNotice.
        The alternatives to use

        :return: The alternatives of this DeprecationNotice.
        :rtype: list[str]
        """
        return self._alternatives

    @alternatives.setter
    def alternatives(self, alternatives):
        """
        Sets the alternatives of this DeprecationNotice.
        The alternatives to use

        :param alternatives: The alternatives of this DeprecationNotice.
        :type: list[str]
        """

        self._alternatives = alternatives

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
        if not isinstance(other, DeprecationNotice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

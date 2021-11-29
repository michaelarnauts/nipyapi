# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.15.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ActionEntity(object):
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
        'id': 'int',
        'timestamp': 'str',
        'source_id': 'str',
        'can_read': 'bool',
        'action': 'ActionDTO'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'source_id': 'sourceId',
        'can_read': 'canRead',
        'action': 'action'
    }

    def __init__(self, id=None, timestamp=None, source_id=None, can_read=None, action=None):
        """
        ActionEntity - a model defined in Swagger
        """

        self._id = None
        self._timestamp = None
        self._source_id = None
        self._can_read = None
        self._action = None

        if id is not None:
          self.id = id
        if timestamp is not None:
          self.timestamp = timestamp
        if source_id is not None:
          self.source_id = source_id
        if can_read is not None:
          self.can_read = can_read
        if action is not None:
          self.action = action

    @property
    def id(self):
        """
        Gets the id of this ActionEntity.

        :return: The id of this ActionEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActionEntity.

        :param id: The id of this ActionEntity.
        :type: int
        """

        self._id = id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ActionEntity.
        The timestamp of the action.

        :return: The timestamp of this ActionEntity.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ActionEntity.
        The timestamp of the action.

        :param timestamp: The timestamp of this ActionEntity.
        :type: str
        """

        self._timestamp = timestamp

    @property
    def source_id(self):
        """
        Gets the source_id of this ActionEntity.

        :return: The source_id of this ActionEntity.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this ActionEntity.

        :param source_id: The source_id of this ActionEntity.
        :type: str
        """

        self._source_id = source_id

    @property
    def can_read(self):
        """
        Gets the can_read of this ActionEntity.
        Indicates whether the user can read a given resource.

        :return: The can_read of this ActionEntity.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """
        Sets the can_read of this ActionEntity.
        Indicates whether the user can read a given resource.

        :param can_read: The can_read of this ActionEntity.
        :type: bool
        """

        self._can_read = can_read

    @property
    def action(self):
        """
        Gets the action of this ActionEntity.

        :return: The action of this ActionEntity.
        :rtype: ActionDTO
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ActionEntity.

        :param action: The action of this ActionEntity.
        :type: ActionDTO
        """

        self._action = action

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
        if not isinstance(other, ActionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

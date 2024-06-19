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


class DefaultSchedule(object):
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
        'strategy': 'str',
        'period': 'str',
        'concurrent_tasks': 'str'
    }

    attribute_map = {
        'strategy': 'strategy',
        'period': 'period',
        'concurrent_tasks': 'concurrentTasks'
    }

    def __init__(self, strategy=None, period=None, concurrent_tasks=None):
        """
        DefaultSchedule - a model defined in Swagger
        """

        self._strategy = None
        self._period = None
        self._concurrent_tasks = None

        if strategy is not None:
          self.strategy = strategy
        if period is not None:
          self.period = period
        if concurrent_tasks is not None:
          self.concurrent_tasks = concurrent_tasks

    @property
    def strategy(self):
        """
        Gets the strategy of this DefaultSchedule.
        The default scheduling strategy

        :return: The strategy of this DefaultSchedule.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Sets the strategy of this DefaultSchedule.
        The default scheduling strategy

        :param strategy: The strategy of this DefaultSchedule.
        :type: str
        """

        self._strategy = strategy

    @property
    def period(self):
        """
        Gets the period of this DefaultSchedule.
        The default scheduling period

        :return: The period of this DefaultSchedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this DefaultSchedule.
        The default scheduling period

        :param period: The period of this DefaultSchedule.
        :type: str
        """

        self._period = period

    @property
    def concurrent_tasks(self):
        """
        Gets the concurrent_tasks of this DefaultSchedule.
        The default concurrent tasks

        :return: The concurrent_tasks of this DefaultSchedule.
        :rtype: str
        """
        return self._concurrent_tasks

    @concurrent_tasks.setter
    def concurrent_tasks(self, concurrent_tasks):
        """
        Sets the concurrent_tasks of this DefaultSchedule.
        The default concurrent tasks

        :param concurrent_tasks: The concurrent_tasks of this DefaultSchedule.
        :type: str
        """

        self._concurrent_tasks = concurrent_tasks

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
        if not isinstance(other, DefaultSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

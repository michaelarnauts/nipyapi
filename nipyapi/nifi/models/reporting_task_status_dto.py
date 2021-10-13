# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.13.3-SNAPSHOT
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ReportingTaskStatusDTO(object):
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
        'run_status': 'str',
        'validation_status': 'str',
        'active_thread_count': 'int'
    }

    attribute_map = {
        'run_status': 'runStatus',
        'validation_status': 'validationStatus',
        'active_thread_count': 'activeThreadCount'
    }

    def __init__(self, run_status=None, validation_status=None, active_thread_count=None):
        """
        ReportingTaskStatusDTO - a model defined in Swagger
        """

        self._run_status = None
        self._validation_status = None
        self._active_thread_count = None

        if run_status is not None:
          self.run_status = run_status
        if validation_status is not None:
          self.validation_status = validation_status
        if active_thread_count is not None:
          self.active_thread_count = active_thread_count

    @property
    def run_status(self):
        """
        Gets the run_status of this ReportingTaskStatusDTO.
        The run status of this ReportingTask

        :return: The run_status of this ReportingTaskStatusDTO.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """
        Sets the run_status of this ReportingTaskStatusDTO.
        The run status of this ReportingTask

        :param run_status: The run_status of this ReportingTaskStatusDTO.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "DISABLED"]
        if run_status not in allowed_values:
            raise ValueError(
                "Invalid value for `run_status` ({0}), must be one of {1}"
                .format(run_status, allowed_values)
            )

        self._run_status = run_status

    @property
    def validation_status(self):
        """
        Gets the validation_status of this ReportingTaskStatusDTO.
        Indicates whether the component is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the component is valid)

        :return: The validation_status of this ReportingTaskStatusDTO.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this ReportingTaskStatusDTO.
        Indicates whether the component is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the component is valid)

        :param validation_status: The validation_status of this ReportingTaskStatusDTO.
        :type: str
        """
        allowed_values = ["VALID", "INVALID", "VALIDATING"]
        if validation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `validation_status` ({0}), must be one of {1}"
                .format(validation_status, allowed_values)
            )

        self._validation_status = validation_status

    @property
    def active_thread_count(self):
        """
        Gets the active_thread_count of this ReportingTaskStatusDTO.
        The number of active threads for the component.

        :return: The active_thread_count of this ReportingTaskStatusDTO.
        :rtype: int
        """
        return self._active_thread_count

    @active_thread_count.setter
    def active_thread_count(self, active_thread_count):
        """
        Sets the active_thread_count of this ReportingTaskStatusDTO.
        The number of active threads for the component.

        :param active_thread_count: The active_thread_count of this ReportingTaskStatusDTO.
        :type: int
        """

        self._active_thread_count = active_thread_count

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
        if not isinstance(other, ReportingTaskStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

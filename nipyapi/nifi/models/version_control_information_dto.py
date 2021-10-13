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


class VersionControlInformationDTO(object):
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
        'group_id': 'str',
        'registry_id': 'str',
        'registry_name': 'str',
        'bucket_id': 'str',
        'bucket_name': 'str',
        'flow_id': 'str',
        'flow_name': 'str',
        'flow_description': 'str',
        'version': 'int',
        'state': 'str',
        'state_explanation': 'str'
    }

    attribute_map = {
        'group_id': 'groupId',
        'registry_id': 'registryId',
        'registry_name': 'registryName',
        'bucket_id': 'bucketId',
        'bucket_name': 'bucketName',
        'flow_id': 'flowId',
        'flow_name': 'flowName',
        'flow_description': 'flowDescription',
        'version': 'version',
        'state': 'state',
        'state_explanation': 'stateExplanation'
    }

    def __init__(self, group_id=None, registry_id=None, registry_name=None, bucket_id=None, bucket_name=None, flow_id=None, flow_name=None, flow_description=None, version=None, state=None, state_explanation=None):
        """
        VersionControlInformationDTO - a model defined in Swagger
        """

        self._group_id = None
        self._registry_id = None
        self._registry_name = None
        self._bucket_id = None
        self._bucket_name = None
        self._flow_id = None
        self._flow_name = None
        self._flow_description = None
        self._version = None
        self._state = None
        self._state_explanation = None

        if group_id is not None:
          self.group_id = group_id
        if registry_id is not None:
          self.registry_id = registry_id
        if registry_name is not None:
          self.registry_name = registry_name
        if bucket_id is not None:
          self.bucket_id = bucket_id
        if bucket_name is not None:
          self.bucket_name = bucket_name
        if flow_id is not None:
          self.flow_id = flow_id
        if flow_name is not None:
          self.flow_name = flow_name
        if flow_description is not None:
          self.flow_description = flow_description
        if version is not None:
          self.version = version
        if state is not None:
          self.state = state
        if state_explanation is not None:
          self.state_explanation = state_explanation

    @property
    def group_id(self):
        """
        Gets the group_id of this VersionControlInformationDTO.
        The ID of the Process Group that is under version control

        :return: The group_id of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this VersionControlInformationDTO.
        The ID of the Process Group that is under version control

        :param group_id: The group_id of this VersionControlInformationDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def registry_id(self):
        """
        Gets the registry_id of this VersionControlInformationDTO.
        The ID of the registry that the flow is stored in

        :return: The registry_id of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """
        Sets the registry_id of this VersionControlInformationDTO.
        The ID of the registry that the flow is stored in

        :param registry_id: The registry_id of this VersionControlInformationDTO.
        :type: str
        """

        self._registry_id = registry_id

    @property
    def registry_name(self):
        """
        Gets the registry_name of this VersionControlInformationDTO.
        The name of the registry that the flow is stored in

        :return: The registry_name of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        """
        Sets the registry_name of this VersionControlInformationDTO.
        The name of the registry that the flow is stored in

        :param registry_name: The registry_name of this VersionControlInformationDTO.
        :type: str
        """

        self._registry_name = registry_name

    @property
    def bucket_id(self):
        """
        Gets the bucket_id of this VersionControlInformationDTO.
        The ID of the bucket that the flow is stored in

        :return: The bucket_id of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """
        Sets the bucket_id of this VersionControlInformationDTO.
        The ID of the bucket that the flow is stored in

        :param bucket_id: The bucket_id of this VersionControlInformationDTO.
        :type: str
        """

        self._bucket_id = bucket_id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this VersionControlInformationDTO.
        The name of the bucket that the flow is stored in

        :return: The bucket_name of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this VersionControlInformationDTO.
        The name of the bucket that the flow is stored in

        :param bucket_name: The bucket_name of this VersionControlInformationDTO.
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def flow_id(self):
        """
        Gets the flow_id of this VersionControlInformationDTO.
        The ID of the flow

        :return: The flow_id of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        """
        Sets the flow_id of this VersionControlInformationDTO.
        The ID of the flow

        :param flow_id: The flow_id of this VersionControlInformationDTO.
        :type: str
        """

        self._flow_id = flow_id

    @property
    def flow_name(self):
        """
        Gets the flow_name of this VersionControlInformationDTO.
        The name of the flow

        :return: The flow_name of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._flow_name

    @flow_name.setter
    def flow_name(self, flow_name):
        """
        Sets the flow_name of this VersionControlInformationDTO.
        The name of the flow

        :param flow_name: The flow_name of this VersionControlInformationDTO.
        :type: str
        """

        self._flow_name = flow_name

    @property
    def flow_description(self):
        """
        Gets the flow_description of this VersionControlInformationDTO.
        The description of the flow

        :return: The flow_description of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._flow_description

    @flow_description.setter
    def flow_description(self, flow_description):
        """
        Sets the flow_description of this VersionControlInformationDTO.
        The description of the flow

        :param flow_description: The flow_description of this VersionControlInformationDTO.
        :type: str
        """

        self._flow_description = flow_description

    @property
    def version(self):
        """
        Gets the version of this VersionControlInformationDTO.
        The version of the flow

        :return: The version of this VersionControlInformationDTO.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this VersionControlInformationDTO.
        The version of the flow

        :param version: The version of this VersionControlInformationDTO.
        :type: int
        """

        self._version = version

    @property
    def state(self):
        """
        Gets the state of this VersionControlInformationDTO.
        The current state of the Process Group, as it relates to the Versioned Flow

        :return: The state of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VersionControlInformationDTO.
        The current state of the Process Group, as it relates to the Versioned Flow

        :param state: The state of this VersionControlInformationDTO.
        :type: str
        """
        allowed_values = ["LOCALLY_MODIFIED", "STALE", "LOCALLY_MODIFIED_AND_STALE", "UP_TO_DATE", "SYNC_FAILURE"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_explanation(self):
        """
        Gets the state_explanation of this VersionControlInformationDTO.
        Explanation of why the group is in the specified state

        :return: The state_explanation of this VersionControlInformationDTO.
        :rtype: str
        """
        return self._state_explanation

    @state_explanation.setter
    def state_explanation(self, state_explanation):
        """
        Sets the state_explanation of this VersionControlInformationDTO.
        Explanation of why the group is in the specified state

        :param state_explanation: The state_explanation of this VersionControlInformationDTO.
        :type: str
        """

        self._state_explanation = state_explanation

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
        if not isinstance(other, VersionControlInformationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class CountersDTO(object):
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
        'aggregate_snapshot': 'CountersSnapshotDTO',
        'node_snapshots': 'list[NodeCountersSnapshotDTO]'
    }

    attribute_map = {
        'aggregate_snapshot': 'aggregateSnapshot',
        'node_snapshots': 'nodeSnapshots'
    }

    def __init__(self, aggregate_snapshot=None, node_snapshots=None):
        """
        CountersDTO - a model defined in Swagger
        """

        self._aggregate_snapshot = None
        self._node_snapshots = None

        if aggregate_snapshot is not None:
          self.aggregate_snapshot = aggregate_snapshot
        if node_snapshots is not None:
          self.node_snapshots = node_snapshots

    @property
    def aggregate_snapshot(self):
        """
        Gets the aggregate_snapshot of this CountersDTO.
        A Counters snapshot that represents the aggregate values of all nodes in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this represents the stats of the single instance.

        :return: The aggregate_snapshot of this CountersDTO.
        :rtype: CountersSnapshotDTO
        """
        return self._aggregate_snapshot

    @aggregate_snapshot.setter
    def aggregate_snapshot(self, aggregate_snapshot):
        """
        Sets the aggregate_snapshot of this CountersDTO.
        A Counters snapshot that represents the aggregate values of all nodes in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this represents the stats of the single instance.

        :param aggregate_snapshot: The aggregate_snapshot of this CountersDTO.
        :type: CountersSnapshotDTO
        """

        self._aggregate_snapshot = aggregate_snapshot

    @property
    def node_snapshots(self):
        """
        Gets the node_snapshots of this CountersDTO.
        A Counters snapshot for each node in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this may be null.

        :return: The node_snapshots of this CountersDTO.
        :rtype: list[NodeCountersSnapshotDTO]
        """
        return self._node_snapshots

    @node_snapshots.setter
    def node_snapshots(self, node_snapshots):
        """
        Sets the node_snapshots of this CountersDTO.
        A Counters snapshot for each node in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this may be null.

        :param node_snapshots: The node_snapshots of this CountersDTO.
        :type: list[NodeCountersSnapshotDTO]
        """

        self._node_snapshots = node_snapshots

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
        if not isinstance(other, CountersDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class SearchResultsDTO(object):
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
        'processor_results': 'list[ComponentSearchResultDTO]',
        'connection_results': 'list[ComponentSearchResultDTO]',
        'process_group_results': 'list[ComponentSearchResultDTO]',
        'input_port_results': 'list[ComponentSearchResultDTO]',
        'output_port_results': 'list[ComponentSearchResultDTO]',
        'remote_process_group_results': 'list[ComponentSearchResultDTO]',
        'funnel_results': 'list[ComponentSearchResultDTO]',
        'label_results': 'list[ComponentSearchResultDTO]',
        'controller_service_node_results': 'list[ComponentSearchResultDTO]',
        'parameter_context_results': 'list[ComponentSearchResultDTO]',
        'parameter_results': 'list[ComponentSearchResultDTO]'
    }

    attribute_map = {
        'processor_results': 'processorResults',
        'connection_results': 'connectionResults',
        'process_group_results': 'processGroupResults',
        'input_port_results': 'inputPortResults',
        'output_port_results': 'outputPortResults',
        'remote_process_group_results': 'remoteProcessGroupResults',
        'funnel_results': 'funnelResults',
        'label_results': 'labelResults',
        'controller_service_node_results': 'controllerServiceNodeResults',
        'parameter_context_results': 'parameterContextResults',
        'parameter_results': 'parameterResults'
    }

    def __init__(self, processor_results=None, connection_results=None, process_group_results=None, input_port_results=None, output_port_results=None, remote_process_group_results=None, funnel_results=None, label_results=None, controller_service_node_results=None, parameter_context_results=None, parameter_results=None):
        """
        SearchResultsDTO - a model defined in Swagger
        """

        self._processor_results = None
        self._connection_results = None
        self._process_group_results = None
        self._input_port_results = None
        self._output_port_results = None
        self._remote_process_group_results = None
        self._funnel_results = None
        self._label_results = None
        self._controller_service_node_results = None
        self._parameter_context_results = None
        self._parameter_results = None

        if processor_results is not None:
          self.processor_results = processor_results
        if connection_results is not None:
          self.connection_results = connection_results
        if process_group_results is not None:
          self.process_group_results = process_group_results
        if input_port_results is not None:
          self.input_port_results = input_port_results
        if output_port_results is not None:
          self.output_port_results = output_port_results
        if remote_process_group_results is not None:
          self.remote_process_group_results = remote_process_group_results
        if funnel_results is not None:
          self.funnel_results = funnel_results
        if label_results is not None:
          self.label_results = label_results
        if controller_service_node_results is not None:
          self.controller_service_node_results = controller_service_node_results
        if parameter_context_results is not None:
          self.parameter_context_results = parameter_context_results
        if parameter_results is not None:
          self.parameter_results = parameter_results

    @property
    def processor_results(self):
        """
        Gets the processor_results of this SearchResultsDTO.
        The processors that matched the search.

        :return: The processor_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._processor_results

    @processor_results.setter
    def processor_results(self, processor_results):
        """
        Sets the processor_results of this SearchResultsDTO.
        The processors that matched the search.

        :param processor_results: The processor_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._processor_results = processor_results

    @property
    def connection_results(self):
        """
        Gets the connection_results of this SearchResultsDTO.
        The connections that matched the search.

        :return: The connection_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._connection_results

    @connection_results.setter
    def connection_results(self, connection_results):
        """
        Sets the connection_results of this SearchResultsDTO.
        The connections that matched the search.

        :param connection_results: The connection_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._connection_results = connection_results

    @property
    def process_group_results(self):
        """
        Gets the process_group_results of this SearchResultsDTO.
        The process groups that matched the search.

        :return: The process_group_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._process_group_results

    @process_group_results.setter
    def process_group_results(self, process_group_results):
        """
        Sets the process_group_results of this SearchResultsDTO.
        The process groups that matched the search.

        :param process_group_results: The process_group_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._process_group_results = process_group_results

    @property
    def input_port_results(self):
        """
        Gets the input_port_results of this SearchResultsDTO.
        The input ports that matched the search.

        :return: The input_port_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._input_port_results

    @input_port_results.setter
    def input_port_results(self, input_port_results):
        """
        Sets the input_port_results of this SearchResultsDTO.
        The input ports that matched the search.

        :param input_port_results: The input_port_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._input_port_results = input_port_results

    @property
    def output_port_results(self):
        """
        Gets the output_port_results of this SearchResultsDTO.
        The output ports that matched the search.

        :return: The output_port_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._output_port_results

    @output_port_results.setter
    def output_port_results(self, output_port_results):
        """
        Sets the output_port_results of this SearchResultsDTO.
        The output ports that matched the search.

        :param output_port_results: The output_port_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._output_port_results = output_port_results

    @property
    def remote_process_group_results(self):
        """
        Gets the remote_process_group_results of this SearchResultsDTO.
        The remote process groups that matched the search.

        :return: The remote_process_group_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._remote_process_group_results

    @remote_process_group_results.setter
    def remote_process_group_results(self, remote_process_group_results):
        """
        Sets the remote_process_group_results of this SearchResultsDTO.
        The remote process groups that matched the search.

        :param remote_process_group_results: The remote_process_group_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._remote_process_group_results = remote_process_group_results

    @property
    def funnel_results(self):
        """
        Gets the funnel_results of this SearchResultsDTO.
        The funnels that matched the search.

        :return: The funnel_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._funnel_results

    @funnel_results.setter
    def funnel_results(self, funnel_results):
        """
        Sets the funnel_results of this SearchResultsDTO.
        The funnels that matched the search.

        :param funnel_results: The funnel_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._funnel_results = funnel_results

    @property
    def label_results(self):
        """
        Gets the label_results of this SearchResultsDTO.
        The labels that matched the search.

        :return: The label_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._label_results

    @label_results.setter
    def label_results(self, label_results):
        """
        Sets the label_results of this SearchResultsDTO.
        The labels that matched the search.

        :param label_results: The label_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._label_results = label_results

    @property
    def controller_service_node_results(self):
        """
        Gets the controller_service_node_results of this SearchResultsDTO.
        The controller service nodes that matched the search

        :return: The controller_service_node_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._controller_service_node_results

    @controller_service_node_results.setter
    def controller_service_node_results(self, controller_service_node_results):
        """
        Sets the controller_service_node_results of this SearchResultsDTO.
        The controller service nodes that matched the search

        :param controller_service_node_results: The controller_service_node_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._controller_service_node_results = controller_service_node_results

    @property
    def parameter_context_results(self):
        """
        Gets the parameter_context_results of this SearchResultsDTO.
        The parameter contexts that matched the search.

        :return: The parameter_context_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._parameter_context_results

    @parameter_context_results.setter
    def parameter_context_results(self, parameter_context_results):
        """
        Sets the parameter_context_results of this SearchResultsDTO.
        The parameter contexts that matched the search.

        :param parameter_context_results: The parameter_context_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._parameter_context_results = parameter_context_results

    @property
    def parameter_results(self):
        """
        Gets the parameter_results of this SearchResultsDTO.
        The parameters that matched the search.

        :return: The parameter_results of this SearchResultsDTO.
        :rtype: list[ComponentSearchResultDTO]
        """
        return self._parameter_results

    @parameter_results.setter
    def parameter_results(self, parameter_results):
        """
        Sets the parameter_results of this SearchResultsDTO.
        The parameters that matched the search.

        :param parameter_results: The parameter_results of this SearchResultsDTO.
        :type: list[ComponentSearchResultDTO]
        """

        self._parameter_results = parameter_results

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
        if not isinstance(other, SearchResultsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

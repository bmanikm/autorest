# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.paths_operations import PathsOperations
from . import models


class AutoRestParameterizedHostTestClientConfiguration(AzureConfiguration):
    """Configuration for AutoRestParameterizedHostTestClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Gets Azure subscription credentials.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, host, accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, filepath=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if host is None:
            raise ValueError("Parameter 'host' must not be None.")
        if not isinstance(host, str):
            raise TypeError("Parameter 'host' must be str.")
        if accept_language is not None and not isinstance(accept_language, str):
            raise TypeError("Optional parameter 'accept_language' must be str.")
        base_url = 'http://{accountName}{host}'

        super(AutoRestParameterizedHostTestClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('autorestparameterizedhosttestclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.host = host
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class AutoRestParameterizedHostTestClient(object):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestParameterizedHostTestClientConfiguration

    :ivar paths: Paths operations
    :vartype paths: .operations.PathsOperations

    :param credentials: Gets Azure subscription credentials.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, host, accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, filepath=None):

        self.config = AutoRestParameterizedHostTestClientConfiguration(credentials, host, accept_language, long_running_operation_retry_timeout, generate_client_request_id, filepath)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self.config, self._serialize, self._deserialize)
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

from .arm_base_model import ARMBaseModel


class DataBoxEdgeDeviceExtendedInfo(ARMBaseModel):
    """The extended Info of the Data Box Edge/Gateway device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The object name.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param encryption_key_thumbprint: The digital signature of encrypted
     certificate.
    :type encryption_key_thumbprint: str
    :param encryption_key: The public part of the encryption certificate.
     Client uses this to encrypt any secret.
    :type encryption_key: str
    :ivar resource_key: The Resource ID of the Resource.
    :vartype resource_key: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_key': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'encryption_key_thumbprint': {'key': 'properties.encryptionKeyThumbprint', 'type': 'str'},
        'encryption_key': {'key': 'properties.encryptionKey', 'type': 'str'},
        'resource_key': {'key': 'properties.resourceKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataBoxEdgeDeviceExtendedInfo, self).__init__(**kwargs)
        self.encryption_key_thumbprint = kwargs.get('encryption_key_thumbprint', None)
        self.encryption_key = kwargs.get('encryption_key', None)
        self.resource_key = None
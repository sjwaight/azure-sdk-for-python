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

from msrest.serialization import Model


class Address(Model):
    """The shipping address of the customer.

    All required parameters must be populated in order to send to Azure.

    :param address_line1: Required. The address line1.
    :type address_line1: str
    :param address_line2: The address line2.
    :type address_line2: str
    :param address_line3: The address line3.
    :type address_line3: str
    :param postal_code: Required. The postal code.
    :type postal_code: str
    :param city: Required. The city name.
    :type city: str
    :param state: Required. The state name.
    :type state: str
    :param country: Required. The country name.
    :type country: str
    """

    _validation = {
        'address_line1': {'required': True},
        'postal_code': {'required': True},
        'city': {'required': True},
        'state': {'required': True},
        'country': {'required': True},
    }

    _attribute_map = {
        'address_line1': {'key': 'addressLine1', 'type': 'str'},
        'address_line2': {'key': 'addressLine2', 'type': 'str'},
        'address_line3': {'key': 'addressLine3', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
    }

    def __init__(self, *, address_line1: str, postal_code: str, city: str, state: str, country: str, address_line2: str=None, address_line3: str=None, **kwargs) -> None:
        super(Address, self).__init__(**kwargs)
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country = country
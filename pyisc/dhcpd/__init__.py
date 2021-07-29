# Copyright 2021 Jonas Hallqvist

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Manipulates ISC dhcpd configuration files.

Enables the conversion of ISC dhcpd conf file to a tree like structure
of objects suitable for alteration and the conversation of that
structure to a string that can easily be written to a file and read by
dhcpd daemon.

Example:
    >>> from pyisc import dhcpd
    >>> parser = dhcpd.DhcpdParser()
    >>> with open('etc/dhcpd.conf', 'r') as infile:
    ...     isc_config = infile.read()
    >>> object_tree = parser.construct_tree(conf)
    >>> print(object_tree.to_isc())
    authoritative;
    log-facility local7;
    omapi-port 7911;
    omapi-key omapi_key;
    ddns-update-style none;
    default-lease-time 600;
    max-lease-time 7200;
    option domain-name "example.org";
    option domain-name-servers ns1.example.org, ns2.example.org;
    include "/home/bbaggins/redbook.conf";
    key omapi_key {
        algorithm hmac-md5;
        secret Ofakekeyfakekeyfakekey==;
    }

    >>> for subnet in object_tree.subnets:
    ...     subnet
        Subnet4(network="10.5.5.0/27")
        Subnet4(network="10.152.187.0/24")
        Subnet4(network="10.198.146.0/26")
        Subnet4(network="10.254.239.0/27")
        Subnet4(network="10.254.239.32/27")
    >>> new_network = dhcpd.nodes.Subnet4(network='192.168.0.0/24')
    >>> object_tree.add_subnet(new_network)
    >>> for subnet in object_tree.subnets:
    ...     subnet
        Subnet4(network="10.5.5.0/27")
        Subnet4(network="10.152.187.0/24")
        Subnet4(network="10.198.146.0/26")
        Subnet4(network="10.254.239.0/27")
        Subnet4(network="10.254.239.32/27")
        Subnet4(network="192.168.0.0/24")

    >>> print(object_tree.subnets[3].to_isc())
    subnet 10.254.239.0 netmask 255.255.255.224 {
        option routers rtr-239-0-1.example.org, rtr-239-0-2.example.org;
        range 10.254.239.10 10.254.239.20;
    }

    >>> object_tree.authoritative = False
    >>> print(object_tree.to_isc())
    not authoritative;
    log-facility local7;
    omapi-port 7911;
    omapi-key omapi_key;
    ddns-update-style none;
    default-lease-time 600;
    max-lease-time 7200;
    option domain-name "example.org";
    option domain-name-servers ns1.example.org, ns2.example.org;
    include "/home/bbaggins/redbook.conf";
    key omapi_key {
        algorithm hmac-md5;
        secret Ofakekeyfakekeyfakekey==;
    }


Attributes:
    dumps (object_tree): Returns a string created from a PyISC DHCPd object
        tree.
    loads (str): Returns a PyISC DHCPd object tree from a supplied string.

"""

__all__ = ['dumps', 'loads', 'DhcpdParser']
__version__ = '0.6.0'
__author__ = 'Jonas Hallqvist'

from pyisc.dhcpd.parsing import DhcpdParser
from pyisc.dhcpd.nodes import *


def loads(content):
    parser = DhcpdParser()
    return parser.construct_tree(content)


def dumps(object_tree):
    return object_tree.to_isc()

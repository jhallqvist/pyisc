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
    --Placeholder--

Attributes:
    --Placeholder--

"""

__all__ = []
__version__ = '0.4.0'
__author__ = 'Jonas Hallqvist'

from pyisc.dhcpd.parsing import DhcpdParser
from pyisc.dhcpd.nodes import *

def loads(content):
    parser = DhcpdParser()
    return parser.construct_tree(content)

def dumps(object_tree):
    return object_tree.to_isc()
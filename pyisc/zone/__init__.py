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

"""Manipulates ISC Zone files.

Enables the conversion of a ISC zone file to a tree like structure
of objects suitable for alteration and the conversation of that
structure to a string that can easily be written to a file.

Example:
    >>> from pyisc import zone
    >>> parser = zone.ZoneParser()
    >>> with open('etc/example.zone', 'r') as infile:
    ...     zone_file = infile.read()
    >>> object_tree = parser.construct_tree(zone_file)
    >>> print(object_tree.to_isc())

Attributes:
    dumps (object_tree): Returns a string created from a PyISC Zone object
        tree.
    loads (str): Returns a PyISC Zone object tree from a supplied string.

"""

__all__ = ['dumps', 'loads', 'ZoneParser']
__version__ = '0.6.0'
__author__ = 'Jonas Hallqvist'

from pyisc.zone.parsing import ZoneParser
from pyisc.zone.nodes import *


def loads(content):
    parser = ZoneParser()
    return parser.construct_tree(content)


def dumps(object_tree):
    return object_tree.to_isc()

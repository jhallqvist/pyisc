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
of objects suitable for alteration and the conversion of that
structure to a string that can easily be written to a file.

Example:
    >>> from pyisc import zone
    >>> with open('etc/example.zone', 'r') as infile:
    ...     zone_file = infile.read()
    >>> object_tree = zone.loads(zone_file)
    >>> print(object_tree.to_isc())

    >>> all_records = [record for record in object_tree.records]
    >>> for record in all_records:
    ...     record
    NS(label=example.com., record_class=IN, ttl=None, nsdname=ns2.example.)
    NS(label=example.com., record_class=IN, ttl=None, nsdname=ns1.example.)
    MX(label=example.com., record_class=IN, ttl=None, preference=10,
       exchange=mail.example.com.)
    MX(label=@, record_class=IN, ttl=None, preference=20,
       exchange=mail2.example.com.)
    MX(label=@, record_class=IN, ttl=None, preference=50, exchange=mail3)
    A(label=example.com., record_class=IN, ttl=None, address=192.0.2.1)
    AAAA(label=None, record_class=IN, ttl=None, address=2001:db8:10::1)
    A(label=ns, record_class=IN, ttl=None, address=192.0.2.2)
    AAAA(label=None, record_class=IN, ttl=None, address=2001:db8:10::2)
    CNAME(label=www, record_class=IN, ttl=None, cname=example.com.)
    CNAME(label=wwwtest, record_class=IN, ttl=None, cname=www)
    A(label=mail, record_class=IN, ttl=3600, address=192.0.2.3)
    A(label=mail2, record_class=IN, ttl=540, address=192.0.2.4)
    A(label=mail3, record_class=IN, ttl=None, address=192.0.2.5)

    >>> from pyisc.zone.nodes import A
    >>> new_record = A(label='new_host', ttl=1200, record_class='IN',
    ...                address='10.10.10.10')
    >>> object_tree.add_record(new_record)
    >>> all_records = [record for record in object_tree.records]
    >>> for record in all_records:
    ...     record
    ...
    NS(label=example.com., record_class=IN, ttl=None, nsdname=ns2.example.)
    NS(label=example.com., record_class=IN, ttl=None, nsdname=ns1.example.)
    MX(label=example.com., record_class=IN, ttl=None, preference=10,
       exchange=mail.example.com.)
    MX(label=@, record_class=IN, ttl=None, preference=20,
       exchange=mail2.example.com.)
    MX(label=@, record_class=IN, ttl=None, preference=50, exchange=mail3)
    A(label=example.com., record_class=IN, ttl=None, address=192.0.2.1)
    AAAA(label=None, record_class=IN, ttl=None, address=2001:db8:10::1)
    A(label=ns, record_class=IN, ttl=None, address=192.0.2.2)
    AAAA(label=None, record_class=IN, ttl=None, address=2001:db8:10::2)
    CNAME(label=www, record_class=IN, ttl=None, cname=example.com.)
    CNAME(label=wwwtest, record_class=IN, ttl=None, cname=www)
    A(label=mail, record_class=IN, ttl=3600, address=192.0.2.3)
    A(label=mail2, record_class=IN, ttl=540, address=192.0.2.4)
    A(label=mail3, record_class=IN, ttl=None, address=192.0.2.5)
    A(label=new_host, record_class=IN, ttl=1200, address=10.10.10.10)


Attributes:
    dumps (object_tree): Returns a string created from a PyISC Zone object
        tree.
    loads (str): Returns a PyISC Zone object tree from a supplied string.

"""

__all__ = ['dumps', 'loads', 'ZoneParser']
__version__ = '0.6.0'
__author__ = 'Jonas Hallqvist'

from pyisc.zone.parsing import ZoneParser


def loads(content):
    parser = ZoneParser()
    return parser.construct_tree(content)


def dumps(object_tree):
    return object_tree.to_isc()

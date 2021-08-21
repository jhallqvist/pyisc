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

from typing import Tuple, List
from pyisc.zone.nodes import A, AAAA, CNAME, MX, NS, SOA


class TokenProcessor:
    """A processor class for tokens.

    This class takes a token and uses the lowercase token name to match a
    method. If a method is found it proceeds to run that method an return
    the value or object and the method to add it to the current working node.

    """

    def switch(self, token) -> Tuple:
        """
        Returns a tuple of value/object and metod.

        Args:
            token (pyisc.zone.parsing.Token): A supplied token instance.

        Returns:
            tuple: Tuple containing value or object in first position
                and method in second position.

        Examples:
            >>> token = Token(type='A',
            ...               value='example.com. IN A 192.0.2.1',
            ...               line=11, column=47)
            >>> processor = TokenProcessor()
            >>> declaration, method = processor.switch(token)
            >>> declaration
            A(label=example.com., record_class=IN, ttl=None, address=192.0.2.1)
            >>> method
            'add_record'

        """
        self.token = token
        return getattr(self, str(token.type).lower(), self.not_found)()

    def not_found(self):
        raise AttributeError(
            f'Token {self.token.type} does not have a associated method.')

    def origin(self) -> Tuple:
        """Returns tuple for the Origin directive."""
        origin = self.token.value.split()[-1]
        return (origin, 'origin')

    def ttl(self) -> Tuple:
        """Returns tuple for the TTL directive."""
        ttl = self.token.value.split()[-1]
        return (ttl, 'ttl')

    def a(self) -> Tuple:
        """Returns tuple for the A record."""
        rr_list = rr_split(self.token.value)
        label, ttl, record_class, _, rdata = standardize_rr(rr_list)
        rdata = rdata.split()[0]
        record = A(
            label=label, record_class=record_class, ttl=ttl, address=rdata)
        return (record, 'add_record')

    def aaaa(self) -> Tuple:
        """Returns tuple for the AAAA record."""
        rr_list = rr_split(self.token.value)
        label, ttl, record_class, _, rdata = standardize_rr(rr_list)
        rdata = rdata.split()[0]
        record = AAAA(
            label=label, record_class=record_class, ttl=ttl, address=rdata)
        return (record, 'add_record')

    def cname(self) -> Tuple:
        """Returns tuple for the CNAME record."""
        rr_list = rr_split(self.token.value)
        label, ttl, record_class, _, rdata = standardize_rr(rr_list)
        rdata = rdata.split()[0]
        record = CNAME(
            label=label, record_class=record_class, ttl=ttl, cname=rdata)
        return (record, 'add_record')

    def mx(self) -> Tuple:
        """Returns tuple for the MX record."""
        rr_list = rr_split(self.token.value)
        label, ttl, record_class, _, rdata = standardize_rr(rr_list)
        preference, exchange = rdata.split()
        record = MX(
            label=label, record_class=record_class, ttl=ttl,
            preference=preference, exchange=exchange)
        return (record, 'add_record')

    def ns(self) -> Tuple:
        """Returns tuple for the NS record."""
        rr_list = rr_split(self.token.value)
        label, ttl, record_class, _, rdata = standardize_rr(rr_list)
        rdata = rdata.split()[0]
        record = NS(
            label=label, record_class=record_class, ttl=ttl, nsdname=rdata)
        return (record, 'add_record')

    def soa(self) -> Tuple:
        """Returns tuple for the SOA record."""
        rr_list = rr_split(self.token.value)
        label, ttl, record_class, _, rdata = standardize_rr(rr_list)
        rdata = rdata.replace('(', '').replace(')', '')
        mname, rname, serial, refresh, retry, expire, minimum = rdata.split()
        record = SOA(
            label=label, record_class=record_class, ttl=ttl, mname=mname,
            rname=rname, serial=serial, refresh=refresh, retry=retry,
            expire=expire, minimum=minimum)
        return (record, 'soa')


def partition_string(content: str) -> List:
    """Returns a list of zone file rows from supplied string."""
    result_array = []
    token_str = ''
    line_no = 1
    char_pos = 0
    str_idx = 1
    line_continuation = False
    scrub_comment = False

    if content[-1] != '\n':
        content += '\n'

    for char in content:
        str_idx += 1
        char_pos += 1
        # States
        if char == '(':
            line_continuation = True
        if char == ')':
            line_continuation = False
        if all((line_continuation, char == ';')):
            scrub_comment = True
        if all((line_continuation, char == '\n')):
            scrub_comment = False
        # Character processing
        if all((char in ('\n', ';'), not line_continuation, token_str != '')):
            sanitized_str = " ".join(token_str.split())
            result_array.append((line_no, sanitized_str, char_pos))
            line_no = line_no + 1 if char == '\n' else line_no
            char_pos = 0
            token_str = char if char == ';' else ''
        elif scrub_comment or ')' in token_str:
            continue
        else:
            token_str += char
    return result_array


def rr_split(rr_string: str) -> List:
    """Returns a list from a supplied resource record string.

    Since RData length can vary this function splits all components up to the
    RData of the string.

    """
    rr_types = ('NSEC3PARAM', 'OPENPGPKEY', 'IPSECKEY', 'CDNSKEY', 'DNSKEY',
                'SMIMEA', 'ZONEMD', 'AFSDB', 'CNAME', 'CSYNC', 'DHCID',
                'DNAME', 'EUI48', 'EUI64', 'HINFO', 'HTTPS', 'NAPTR', 'NSEC3',
                'RRSIG', 'SSHFP', 'AAAA', 'CERT', 'NSEC', 'SVCB', 'TKEY',
                'TLSA', 'TSIG', 'APL', 'CAA', 'CDS', 'DLV', 'HIP', 'KEY',
                'LOC', 'PTR', 'SIG', 'SOA', 'SRV', 'TXT', 'URI', 'DS', 'KX',
                'MX', 'NS', 'RP', 'TA', 'A')
    try:
        rr_type = next(rr_type for rr_type in rr_types if rr_type in rr_string)
        rr_idx = rr_string.find(rr_type)
        rr_len = len(rr_type)
        return rr_string[:rr_idx + rr_len].split() + \
            [rr_string[rr_idx + rr_len:]]
    except StopIteration:
        return ValueError('Provided string is not a valid Resource Record')


def has_class(rr_list: List) -> bool:
    """Determines if the list contains a resource class."""
    return any(r_class in rr_list for r_class in ('IN', 'CS', 'CH', 'HS'))


def has_ttl(rr_list: List) -> bool:
    """Determines if the list contains a TTL value."""
    return any(x.isdigit() for x in rr_list)


def has_name(rr_list: List) -> bool:
    """Determines if the list contains a label for the resource record."""
    return all((len(rr_list) > 2, not rr_list[0].isdigit(),
                rr_list[0] not in ('IN', 'CS', 'CH', 'HS')))


def standardize_rr(rr_list: List) -> List:
    """Returns a padded list of the supplied resource record list.

    The returned list will represent the five-tuple designated correct by
    RFC1035. This means ['label', 'ttl, 'class', 'type', 'rdata']. 
    Missing entries in the supplied list will be padded with None or, in the
    case of class, with 'IN'.

    """
    while len(rr_list) < 5:
        if not has_ttl(rr_list):
            rr_list.insert(-2, None)
        if not has_class(rr_list):
            rr_list.insert(-3, 'IN')
        if not has_name(rr_list):
            rr_list.insert(0, None)
        if all((has_class, has_name, has_ttl)):
            break
    if rr_list[2] not in ('IN', 'CS', 'CH', 'HS'):
        rr_list[1], rr_list[2] = rr_list[2], rr_list[1]
    return rr_list

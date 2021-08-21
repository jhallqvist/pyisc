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

from ipaddress import IPv4Address, IPv6Address
from typing import List, Union


class ResourceRecord:
    """A base for all the various record types.

    This class is not meant to be instantiated but only to serve as a
    foundation for the other record types in order to reduce repetitive code.
    """
    def __init__(
        self,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None,
    ) -> None:
        self.label = label
        self.record_class = record_class
        self.ttl = ttl

    def __str__(self, **kwargs) -> str:
        returned_str = (f'{self.label if self.label else "":<50} '
                        f'{self.ttl if self.ttl else "":>8} '
                        f'{self.record_class if self.record_class else "":>2} '
                        f'{self.__class__.__name__:<10} ')
        if kwargs:
            returned_str += " ".join(
                [f'{value}' for value in kwargs.values()])
        return returned_str

    def __repr__(self, **kwargs) -> str:
        returned_str = (f'{self.__class__.__name__}(label={self.label}, '
                        f'record_class={self.record_class}, '
                        f'ttl={self.ttl}')
        if kwargs:
            returned_str += ', '
            returned_str += ", ".join(
                [f'{key}={value}' for key, value in kwargs.items()])
        returned_str += ')'
        return returned_str

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        Examples:
            >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        return f'{self.__str__()}'


class A(ResourceRecord):
    """Represents the A record type"""
    def __init__(
        self,
        address:        IPv4Address,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.address = address
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(address=self.address)

    def __repr__(self) -> str:
        return super().__repr__(address=self.address)


class AAAA(ResourceRecord):
    """Represents the AAAA record type"""
    def __init__(
        self,
        address:        IPv6Address,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.address = address
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(address=self.address)

    def __repr__(self) -> str:
        return super().__repr__(address=self.address)


class AFSDB(ResourceRecord):
    """Represents the AFSDB record type"""
    def __init__(
        self,
        subtype:        str,
        hostname:       str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.subtype = subtype
        self.hostname = hostname
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(subtype=self.subtype, hostname=self.hostname)

    def __repr__(self) -> str:
        return super().__repr__(subtype=self.subtype, hostname=self.hostname)


class APL(ResourceRecord):
    """Represents the APL record type"""
    def __init__(
        self,
        address_family: str,
        prefix:         str,
        n:              str,
        afd_length:     str,
        afd_part:       str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.address_family = address_family
        self.prefix = prefix
        self.n = n
        self.afd_length = afd_length
        self.afd_part = afd_part
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        '''Might need a unique method because of the format of the rdata,
        see RFC3123'''
        return super().__str__(address_family=self.address_family,
                               prefix=self.prefix, n=self.n,
                               afd_length=self.afd_length,
                               afd_part=self.afd_part)

    def __repr__(self) -> str:
        return super().__repr__(address_family=self.address_family,
                                prefix=self.prefix, n=self.n,
                                afd_length=self.afd_length,
                                afd_part=self.afd_part)


class CAA(ResourceRecord):
    pass


class CDNSKEY(ResourceRecord):
    pass


class CDS(ResourceRecord):
    pass


class CERT(ResourceRecord):
    pass


class CNAME(ResourceRecord):
    """Represents the CNAME record type"""
    def __init__(
        self,
        cname:          str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.cname = cname
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(cname=self.cname)

    def __repr__(self) -> str:
        return super().__repr__(cname=self.cname)


class CSYNC(ResourceRecord):
    pass


class DHCID(ResourceRecord):
    pass


class DLV(ResourceRecord):
    pass


class DNAME(ResourceRecord):
    pass


class DNSKEY(ResourceRecord):
    pass


class DS(ResourceRecord):
    pass


class EUI48(ResourceRecord):
    pass


class EUI64(ResourceRecord):
    pass


class HINFO(ResourceRecord):
    """Represents the HINFO record type"""
    def __init__(
        self,
        cpu:            str,
        os:             str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.cpu = cpu
        self.os = os
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(cpu=self.cpu, os=self.os)

    def __repr__(self) -> str:
        return super().__repr__(cpu=self.cpu, os=self.os)


class HIP(ResourceRecord):
    pass


class IPSECKEY(ResourceRecord):
    pass


class KEY(ResourceRecord):
    pass


class KX(ResourceRecord):
    pass


class LOC(ResourceRecord):
    pass


class MX(ResourceRecord):
    """Represents the MX record type"""
    def __init__(
        self,
        preference:     int,
        exchange:       str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.preference = preference
        self.exchange = exchange
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(
            preference=self.preference, exchange=self.exchange)

    def __repr__(self) -> str:
        return super().__repr__(
            preference=self.preference, exchange=self.exchange)


class NAPTR(ResourceRecord):
    pass


class NS(ResourceRecord):
    """Represents the NS record type"""
    def __init__(
        self,
        nsdname:        str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.nsdname = nsdname
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(nsdname=self.nsdname)

    def __repr__(self) -> str:
        return super().__repr__(nsdname=self.nsdname)


class NSEC(ResourceRecord):
    pass


class NSEC3(ResourceRecord):
    pass


class NSEC3PARAM(ResourceRecord):
    pass


class OPENPGPKEY(ResourceRecord):
    pass


class PTR(ResourceRecord):
    """Represents the PTR record type"""
    def __init__(
        self,
        ptrdname:       str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.ptrdname = ptrdname
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(ptrdname=self.ptrdname)

    def __repr__(self) -> str:
        return super().__repr__(ptrdname=self.ptrdname)


class RRSIG(ResourceRecord):
    pass


class RP(ResourceRecord):
    """Represents the RP record type"""
    def __init__(
        self,
        mbox_dname:     str,
        txt_dname:      str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.mbox_dname = mbox_dname
        self.txt_dname = txt_dname
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(
            mbox_dname=self.mbox_dname, txt_dname=self.txt_dname)

    def __repr__(self) -> str:
        return super().__repr__(
            mbox_dname=self.mbox_dname, txt_dname=self.txt_dname)


class SIG(ResourceRecord):
    pass


class SMIMEA(ResourceRecord):
    pass


class SOA(ResourceRecord):
    """Represents the SOA record type"""
    def __init__(
        self,
        mname:          str,
        rname:          str,
        serial:         Union[int, str],
        refresh:        int,
        retry:          int,
        expire:         int,
        minimum:        int,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.mname = mname
        self.rname = rname
        self.serial = serial
        self.refresh = refresh
        self.retry = retry
        self.expire = expire
        self.minimum = minimum
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        newline = '\n'
        placeholder = f'{" ":<74}'
        return (f'{self.label if self.label else "":<50} '
                f'{self.ttl if self.ttl else "":>8} '
                f'{self.record_class if self.record_class else "":<2} '
                f'{self.__class__.__name__:<10} {self.mname:<25} '
                f'{self.rname} ({newline}'
                f'{placeholder}{self.serial:<25} ; serial{newline}'
                f'{placeholder}{self.refresh:<25} ; refresh {newline}'
                f'{placeholder}{self.retry:<25} ; retry {newline}'
                f'{placeholder}{self.expire:<25} ; expire {newline}'
                f'{placeholder}{str(self.minimum) + " )":<25} ; minimum TTL')

    def __repr__(self) -> str:
        return super().__repr__(mname=self.mname, rname=self.rname,
                                serial=self.serial, refresh=self.refresh,
                                retry=self.retry, expire=self.expire,
                                minimum=self.minimum)

    def update_serial(self, serial):
        pass


class SRV(ResourceRecord):
    pass


class SSHFP(ResourceRecord):
    pass


class TA(ResourceRecord):
    pass


class TKEY(ResourceRecord):
    pass


class TLSA(ResourceRecord):
    pass


class TSIG(ResourceRecord):
    pass


class TXT(ResourceRecord):
    """Represents the TXT record type"""
    def __init__(
        self,
        txtdata:        str,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.txtdata = txtdata
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(txtdata=self.txtdata)

    def __repr__(self) -> str:
        return super().__repr__(txtdata=self.txtdata)


class URI(ResourceRecord):
    pass


class ZONEMD(ResourceRecord):
    pass


class SVCB(ResourceRecord):
    pass


class HTTPS(ResourceRecord):
    pass


# Possibly Obsoleted RRs and Pseudo RRs
class AXFR(ResourceRecord):
    pass


class IXFR(ResourceRecord):
    pass


class OPT(ResourceRecord):
    pass


class WKS(ResourceRecord):
    """Represents the WKS record type"""
    def __init__(
        self,
        address:        IPv4Address,
        protocol:       int,
        bit_map:        bytes,
        label:          Union[str, None] = None,
        record_class:   Union[str, None] = None,
        ttl:            Union[int, None] = None
    ) -> None:
        self.address = address
        self.protocol = protocol
        self.bit_map = bit_map
        super().__init__(label=label, record_class=record_class, ttl=ttl)

    def __str__(self) -> str:
        return super().__str__(
            address=self.address, protocol=self.protocol, bit_map=self.bit_map)

    def __repr__(self) -> str:
        return super().__repr__(
            address=self.address, protocol=self.protocol, bit_map=self.bit_map)


class Zone:
    """Represents the Zone.

    This is the root of all the zone configuration and its records.
    """
    def __init__(
        self,
        origin:     Union[str, None] = None,
        ttl:        Union[int, None] = None,
        soa:        Union[SOA, None] = None,
        records:    Union[List, None] = None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            origin (str): The Origin of the zone.
            ttl (int)): The Time To Live for the zone.
            soa (pyisc.zone.nodes.SOA): The Start of Authority for the zone.
            records (list): List of all records in the zone.

        """
        self.origin = origin
        self.ttl = ttl
        self.soa = soa
        self.records = [] if not records else records

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        return f'Zone(origin={self.origin})'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        Examples:
            >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        newline = '\n'
        all_records = '\n'.join([record.to_isc() for record in self.records])
        return_string = (f'$ORIGIN {self.origin}{newline}'
                         f'$TTL {self.ttl}{newline*2}'
                         f'{self.soa}{newline}'
                         f'{all_records}')
        return f'{return_string}'

    def add_record(self, record: object, sort: bool = False):
        self.records.append(record)

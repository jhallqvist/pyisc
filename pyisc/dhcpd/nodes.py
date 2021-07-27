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

from typing import List, Union
from ipaddress import IPv4Network
from pyisc.dhcpd.mixin import ( KeyMixin, Parameters, OptionMixin, PoolMixin,
                                RangeMixin, SubnetMixin, SharedNetworkMixin,
                                GroupMixin, HostMixin, ClassMixin,
                                SubClassMixin, ZoneMixin, IncludeMixin)

# Parameter classes
class Hardware:
    """Represents an hardware parameter."""
    def __init__(
        self,
        type: Union[str, None],
        address: Union[str, None]
    ) -> None:
        """Initialize attributes for the class.

        Args:
            type (str): The type of the hardware instance.
            address (str): The address of the hardware instance.

        """
        self.type = type
        self.address = address
    def __str__(self) -> str:
        return f'hardware {self.type} {self.address}'
    def __repr__(self) -> str:
        return f'Hardware(type="{self.type}", address="{self.address}")'
    # def to_dict(self):
    #     return {}
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        return f'{" " * indent}{self.__str__()};'


class HostIdentifier:
    """Represents an host identifier parameter."""
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    # def to_dict(self):
    #     return {}
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        pass


class ServerDuid:
    """Represents an server DUID parameter."""
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        pass


class Option:
    """Represents an dhcp option."""
    def __init__(
        self,
        value: Union[str, None],
        name: Union[str, None]=None,
        number: Union[int, None]=None
    ) -> None:
        """Initialize attributes for the class.

        Name or number (or both) must be given. If value contains a comma it
        is assumed that the value will be a list and the submitted string will
        be saved accordingly.

        Args:
            name (str): The name of the dhcp option.
            number (str): The number of the dhcp option.
            value (str): The value of the option.

        """
        if not name and not number:
            raise TypeError('__init__() missing attribute: name or number')
        self.name = name
        self.number = number
        self.value = value
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        if ',' in value:
            self.__value = [x.strip() for x in value.split(',')]
        else:
            self.__value = value
    def __str__(self) -> str:
        if isinstance(self.value, list):
            return (f'option {self.name.replace("_","-") if self.name else self.number} '
                    f'{", ".join(self.value)}')
        else:
            return (f'option {self.name.replace("_","-") if self.name else self.number} '
                    f'{self.value}')
    def __repr__(self) -> str:
        key = f'name="{self.name}"' if self.name else f'number="{self.number}"'
        if isinstance(self.value, list):
            value = f'value={self.value}'
        else:
            value = f'value="{self.value}"'
        return f'Option({key}, {value})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        return f'{" " * indent}{self.__str__()};'


# Declarations
class Failover:
    """Represents the Failover declaration."""
    def __init__(
        self,
        name:                       str,
        role:                       Union[str, None]=None,
        address:                    Union[str, None]=None,
        peer_address:               Union[str, None]=None,
        port:                       Union[int, None]=None,
        peer_port:                  Union[int, None]=None,
        max_response_delay:         Union[int, None]=None,
        max_unacked_updates:        Union[int, None]=None,
        mclt:                       Union[int, None]=None,
        split:                      Union[int, None]=None,
        hba:                        Union[str, None]=None,
        load_balance_max_seconds:   Union[int, None]=None,
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): A name for the failover peer.
            role (str): Should be either primary or secondary.
            address (str): The IP address of the server in string format.
            peer_address (str): The IP address of the failover peer server
                                in string format.
            port (int): The TCP port that the server listens for connections
                                from failover peer.
            peer_port (int): The TCP port that the server connects to its
                                failover peer.
            max_response_delay (int): Sets maximum response delay.
            max_unacked_updates (int): Sets maximum for unacknowledged
                                messages.
            mclt (int): Sets maximum client lead time.
            split (int): Sets split load between primary and secondary
                                failover member.
            hba (str): Sets split load between primary and secondary
                                failover member as a bitmap.
            load_balance_max_seconds (int): Sets cutoff for disabling load 
                                balance.

        """
        self.name = name
        self.role  = role
        self.address = address
        self.peer_address = peer_address
        self.port = port
        self.peer_port = peer_port
        self.max_response_delay = max_response_delay
        self.max_unacked_updates = max_unacked_updates
        self.mclt = mclt
        self.split = split
        self.hba = hba
        self.load_balance_max_seconds = load_balance_max_seconds
    def __str__(self) -> str:
        return f'failover peer {self.name}'
    def __repr__(self) -> str:
        return f'Failover(name={self.name})'
    def object_tree(self, indent=0):
        """TEMP."""
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            new_key = key.replace("_"," ")
            if all((value, key == 'load_balance_max_seconds')):
                attrs.append(
                    f'{" " * child_indent}{new_key} {value};')
            elif all((value, key == 'role')):
                attrs.append(f'{" " * child_indent}{value};')
            elif all((value, key != 'name')):
                attrs.append(
                    f'{" " * child_indent}{key.replace("_","-")} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class Include:
    """Represents the include declaration."""
    def __init__(self, filename: str) -> None:
        """Initialize attributes for the class.

        Args:
            filename (str): A path to the file that is to be included.

        """
        self.filename = filename
    def __str__(self) -> str:
        return f'include {self.filename}'
    def __repr__(self) -> str:
        return f'Include(filename={self.filename})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        return f'{" " * indent}{self.__str__()};'

class Range4:
    """Represents the range declaration for IPv4 objects."""
    def __init__(
        self,
        start:  str,
        end:    Union[str, None]=None,
        flag:   Union[str, None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            start (str): The first IP address in the range.
            end (str): The last IP address in the range.
            flag (str): If set allows BOOTP clients to get dynamically
                        assigned addresses.

        """
        self.start = start
        self.end = end          # Can be omitted
        self.flag = flag        # Valid value dynamic-bootp or None.
    def __str__(self) -> str:
        list_comp = [x for x in (self.flag, self.start, self.end) if x]
        return f'range {" ".join(list_comp)}'
    def __repr__(self) -> str:
        string_repr = [f'{key}="{value}"' for key, value in self.__dict__.items() if value]
        return f'Range4({", ".join(string_repr)})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        return f'{" " * indent}{self.__str__()};'


class Range6:
    """Represents the range declaration for IPv6 objects."""
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        pass


class Pool6:
    """Represents an pool declaration for IPv6 objects."""
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        pass


class Subnet6:
    """Represents an subnet declaration for IPv6 objects."""
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        pass


class Key:
    """Represents an key declaration and parameter."""
    def __init__(
        self,
        name:       str,
        algorithm:  Union[str, None]=None,
        secret:     Union[str, None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): The name of the key instance.
            algorithm (str): The algorithm used for the key.
            secret (str): The secret used by the key.

        """
        self.name = name
        self.algorithm = algorithm
        self.secret = secret
    def __str__(self) -> str:
        return f'key {self.name}'
    def __repr__(self) -> str:
        return f'Key(name="{self.name}")'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class Zone:
    """Represents an zone declaration."""
    def __init__(
        self,
        name:       str,
        primary:    Union[str, None]=None,
        key:        Union[Key, None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): The name of the zone.
            primary (str): The IP address of the primary server for the zone
                            in string format.
            key (pyisc.dhcpd.nodes.Key): The key used to authenticate to the
                            primary server.

        """
        self.name = name
        self.primary = primary
        self.key = key
    def __str__(self) -> str:
        return f'zone {self.name}'
    def __repr__(self) -> str:
        return f'Zone(name={self.name})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if all((value, key != 'name', key != 'key')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        if self.key:
            attrs.append(f'{" " * child_indent}{value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class DhcpClass:
    """Represents an class declaration."""
    def __init__(
        self,
        name:               str,
        always_broadcast:   Union[bool, None]=None,
        match:              Union[str, None]=None,
        spawn:              Union[str, None]=None,
        lease_limit:        Union[int, None]=None,
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): The name of the zone.
            always_broadcast (boolean): Broadcast even if broadcast flag is
                        unset from clients.
            match (str): The conditional in the form of a string.
            spawn (str): The spawn argument in the form of a string.
            lease_limit (int): Sets the amount of clients that are allowed a
                        lease

        """
        self.name = name
        self.always_broadcast = always_broadcast
        self.match = match
        self.spawn = spawn
        self.lease_limit = lease_limit
    def __str__(self) -> str:
        return f'class {self.name}'
    def __repr__(self) -> str:
        return f'DhcpClass(name={self.name})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if key == 'lease_limit':
                new_key = key.replace("_", " ")
            else:
                new_key = key.replace("_", "-")
            if all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{new_key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class SubClass(Parameters, OptionMixin):
    """Represents an subclass declaration."""
    def __init__(
        self,
        name:           str,
        match_value:    str,
        lease_limit:    Union[int, None]=None,
        options:        Union[List[Option], None]=None,
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): The name of the zone.
            match_value (str): The conditional in the form of a string.
            lease_limit (int): Sets the amount of clients that are allowed a
                        lease
            options (list[pyisc.dhcpd.nodes.Option]): A list of options.

        """
        self.name = name
        self.match_value = match_value
        self.lease_limit = lease_limit
        self.options = [] if not options else options
        super().__init__()
    def __str__(self) -> str:
        return f'subclass {self.name} {self.match_value}'
    def __repr__(self) -> str:
        return f'SubClass(name={self.name}, match_value={self.match_value})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            new_key = key.replace("_", "-")
            if isinstance(value, list):
                for item in value:
                    attrs.append(item.to_isc(indent=child_indent))
            elif all((value, key != 'name', key != 'match_value')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        if len(attrs) == 0:
            return f'{" " * indent}{self.__str__()};'
        return_str = (f'{" " * indent}{self.__str__()}' ' {' '\n')
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')

class Host(Parameters):
    """Represents an host declaration.
    
    TODO:
        * Host Identifier is not present in to_isc method.
    """
    def __init__(
        self,
        name:               str,
        always_broadcast:   Union[bool, None]=None,
        fixed_address:      Union[str, None]=None,
        fixed_address6:     Union[str, None]=None,
        fixed_prefix6:      Union[str, None]=None,
        hardware:           Union[Hardware, None]=None,
        host_identifier:    Union[HostIdentifier, None]=None,
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): The name of the zone.
            always_broadcast (boolean): Broadcast even if broadcast flag is
                        unset from clients.
            fixed_address (str, list[str]): One or more IPv4 address in
                        string format.
            fixed_address6 (str): An IPv6 address in string format.
            fixed_prefix6 (str, list[str]): One or more IPv prefixes.
            hardware (pyisc.dhcpd.nodes.Hardware): The hardware address of
                        the client.
            host_identifier (pyisc.dhcpd.nodes.HostIdentifier): IPv6 
                        identifier for client

        """
        self.name = name
        self.always_broadcast = always_broadcast
        self.fixed_address = fixed_address
        self.fixed_address6 = fixed_address6
        self.fixed_prefix6 = fixed_prefix6
        self.hardware = hardware
        self.host_identifier = host_identifier
        super().__init__()
    def __str__(self) -> str:
        return f'host {self.name}'
    def __repr__(self) -> str:
        return f'Host(name={self.name})'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            new_key = key.replace("_", "-")
            # if isinstance(value, Hardware):
            if hasattr(value, 'to_isc'):
                attrs.append(f'{" " * child_indent}{value.to_isc()}')
            elif all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{new_key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')

class Pool4(RangeMixin):
    """Represents an pool declaration for IPv4 objects."""
    def __init__(
        self,
        known_clients:               Union[str, None]=None,
        unknown_clients:             Union[str, None]=None,
        allow_members_of:            Union[List[str], None]=None,
        deny_members_of:             Union[List[str], None]=None,
        dynamic_bootp_clients:       Union[str, None]=None,
        authenticated_clients:       Union[str, None]=None,
        unauthenticated_clients:     Union[str, None]=None,
        all_clients:                 Union[str, None]=None,
        allow_after:                 Union[int, None]=None,
        deny_after:                  Union[int, None]=None,
        failover:                    Union[Failover, None]=None,
        ranges:                      Union[List[Range4], None]=None,
    ) -> None:
        """Initialize attributes for the class.

        Args:
            known_clients (str): pass
            unknown_clients (str): pass
            allow_members_of (list[str]): pass
            deny_members_of (list[str]): pass
            dynamic_bootp_clients (str): pass
            authenticated_clients (str): pass
            unauthenticated_clients (str): pass
            all_clients (str): pass
            allow_after (int): pass
            deny_after (int): pass
            failover (pyisc.dhcpd.nodes.Failover): pass
            ranges (list[pyisc.dhcpd.nodes.Range4]): pass

        """
        self.known_clients = known_clients
        self.unknown_clients = unknown_clients
        self.allow_members_of = [] if not allow_members_of else allow_members_of
        self.deny_members_of = [] if not deny_members_of else deny_members_of
        self.dynamic_bootp_clients = dynamic_bootp_clients
        self.authenticated_clients = authenticated_clients
        self.unauthenticated_clients = unauthenticated_clients
        self.all_clients = all_clients
        self.allow_after = allow_after
        self.deny_after = deny_after
        self.failover = failover
        self.ranges = [] if not ranges else ranges
    def __str__(self) -> str:
        return f'pool'
    def __repr__(self) -> str:
        return f'Pool4()'
    def add_allowed_member(self, member: str) -> None:
        self.allow_members_of.append(member)
    def delete_allowed_member(self, member: str) -> None:
        self.allow_members_of.remove(member)
    def add_denied_member(self, member: str) -> None:
        self.deny_members_of.append(member)
    def delete_denied_member(self, member: str) -> None:
        self.deny_members_of.remove(member)
    def object_tree(self, indent=0):
        attrs = []
        child_indent = indent+4
        for dhcp_range in self.ranges:
            attrs.append(f'{" " * child_indent}{dhcp_range.object_tree()}')
        return_str = f'{" " * indent}{self.__repr__()}'
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        return f'{return_str}{attrs_str}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if 'known' in key:
                new_key = key.replace("_", "-")
            else:
                new_key = key.replace("_", " ")
            if all((value, 'members_of' in key)):
                temp = [f'{" " * child_indent}{new_key} {subvalue};' for subvalue in value]
                for statement in temp:
                    attrs.append(statement)
            elif all((value, key == 'ranges')):
                for dhcp_range in self.ranges:
                    attrs.append(f'{" " * child_indent}{dhcp_range.to_isc()}')
            elif all((value, key == 'failover')):
                attrs.append(f'{" " * child_indent}{value};')
            elif any((value=='allow', value=='deny')):
                attrs.append(f'{" " * child_indent}{value} {new_key};')
            elif all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{new_key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class Subnet4(Parameters, OptionMixin, RangeMixin, PoolMixin):
    """Represents an subnet declaration for IPv4 objects."""
    def __init__(
        self,
        network:            str,
        authoritative:      Union[bool, None]=None,
        server_id_check:    Union[bool, None]=None,
        options:            Union[List[Option], None]=None,
        ranges:             Union[List[Range4], None]=None,
        pools:              Union[List[Pool4], None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            network (str): pass
            authoritative (boolean): pass
            server_id_check (boolean): pass
            options (list[pyisc.dhcpd.nodes.Option]): pass
            ranges (list[pyisc.dhcpd.nodes.Range4]): pass
            pools (list[pyisc.dhcpd.nodes.Pool4]): pass

        """
        self.network = IPv4Network(network).with_prefixlen
        self.authoritative = authoritative
        self.server_id_check = server_id_check
        self.options = [] if not options else options
        self.ranges = [] if not ranges else ranges
        self.pools = [] if not pools else pools
        super().__init__()
    def __str__(self) -> str:
        ip_network = IPv4Network(self.network)
        subnet, netmask = ip_network.with_netmask.split('/')
        return f'subnet {subnet} netmask {netmask}'
    def __repr__(self) -> str:
        return f'Subnet4(network="{self.network}")'
    def object_tree(self, indent=0):
        return f'{" " * indent}{self.__repr__()}'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                for item in value:
                    attrs.append(item.to_isc(indent=child_indent))
            elif all((isinstance(value, bool), key == 'authoritative')):
                if value:
                    attrs.append(f'{" " * child_indent}{key};')
                else:
                    attrs.append(f'{" " * child_indent}not {key};')
            elif all((value, key != 'network')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')

class SharedNetwork(OptionMixin, SubnetMixin, PoolMixin):
    """Represents an shared network declaration."""
    def __init__(
        self,
        name:           str,
        authoritative:  Union[bool, None]=None,
        options:        Union[List[Option], None]=None,
        subnets:        Union[List[Subnet4], None]=None,
        pools:          Union[List[Pool4], None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            name (str): pass
            authoritative (boolean): pass
            options (list[pyisc.dhcpd.nodes.Option]): pass
            ranges (list[pyisc.dhcpd.nodes.Range4]): pass
            pools (list[pyisc.dhcpd.nodes.Pool4]): pass

        """
        self.name = name
        self.authoritative = authoritative
        self.options = [] if not options else options
        self.subnets = [] if not subnets else subnets
        self.pools = [] if not pools else pools
    def __str__(self) -> str:
        return f'shared-network {self.name}'
    def __repr__(self) -> str:
        return f'SharedNetwork(name={self.name})'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                for item in value:
                    attrs.append(item.to_isc(indent=child_indent))
            elif all((isinstance(value, bool), key == 'authoritative')):
                if value:
                    attrs.append(f'{key};')
                else:
                    attrs.append(f'not {key};')
            elif all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class Group(Parameters, SubnetMixin, SharedNetworkMixin, HostMixin, OptionMixin):
    """Represents an group declaration."""
    def __init__(
        self,
        options:            Union[List[Option], None]=None,
        subnets:            Union[List[Subnet4], None]=None,
        shared_networks:    Union[List[SharedNetwork], None]=None,
        hosts:              Union[List[Host], None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            options (list[pyisc.dhcpd.nodes.Option]): pass
            subnets (list[pyisc.dhcpd.nodes.Subnet4]): pass
            shared_networks (list[pyisc.dhcpd.nodes.SharedNetwork]): pass
            hosts (list[pyisc.dhcpd.nodes.Host]): pass

        """
        self.options = [] if not options else options
        self.subnets = [] if not subnets else subnets
        self.shared_networks = [] if not shared_networks else shared_networks
        # self.groups = [] if not groups else groups
        self.hosts = [] if not hosts else hosts
    def __str__(self) -> str:
        return f'group'
    def __repr__(self) -> str:
        return f'Group()'
    def to_isc(self, indent: int=0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent+4
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                for item in value:
                    attrs.append(item.to_isc(indent=child_indent))
            elif value:
                attrs.append(f'{" " * child_indent}{key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '}'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class Global(   Parameters, OptionMixin, SubnetMixin, SharedNetworkMixin,
                GroupMixin, HostMixin, ClassMixin, SubClassMixin, KeyMixin,
                ZoneMixin, IncludeMixin):
    """Represents the global dhcp server settings."""
    def __init__(
        self,
        abandon_lease_time:             Union[str, None]=None,
        authoritative:                  Union[bool, None]=None,
        db_time_format:                 Union[str, None]=None,
        ddns_dual_stack_mixed_mode:     Union[str, None]=None,
        ddns_guard_id_must_match:       Union[str, None]=None,
        ddns_other_guard_is_dynamic:    Union[str, None]=None,
        lease_file_name:                Union[str, None]=None,
        dhcpv6_lease_file_name:         Union[str, None]=None,
        local_port:                     Union[int, None]=None,
        local_address:                  Union[str, None]=None,
        local_address6:                 Union[str, None]=None,
        bind_local_address6:            Union[bool, None]=None,
        log_facility:                   Union[str, None]=None,
        omapi_port:                     Union[int, None]=None,
        omapi_key:                      Union[str, None]=None,
        persist_eui_64_leases:          Union[bool, None]=None,
        pid_file_name:                  Union[str, None]=None,
        dhcpv6_pid_file_name:           Union[str, None]=None,
        release_on_roam:                Union[bool, None]=None,
        remote_port:                    Union[int, None]=None,
        server_id_check:                Union[bool, None]=None,
        server_duid:                    Union[ServerDuid, None]=None,
        update_conflict_detection:      Union[bool, None]=None,
        use_eui_64:                     Union[bool, None]=None,
        options:                        Union[List[Option], None]=None,
        keys:                           Union[List[Key], None]=None,
        zones:                          Union[List[Zone], None]=None,
        failover:                       Union[Failover, None]=None,
        subnets:                        Union[List[Subnet4], None]=None,
        shared_networks:                Union[List[SharedNetwork], None]=None,
        groups:                         Union[List[Group], None]=None,
        hosts:                          Union[List[Host], None]=None,
        classes:                        Union[List[DhcpClass], None]=None,
        subclasses:                     Union[List[SubClass], None]=None,
        includes:                       Union[List[Include], None]=None
    ) -> None:
        """Initialize attributes for the class.

        Args:
            abandon_lease_time (str): pass
            authoritative (boolean): pass
            db_time_format (str): pass
            ddns_dual_stack_mixed_mode (str): pass

        """
        self.abandon_lease_time = abandon_lease_time
        self.authoritative = authoritative
        self.db_time_format = db_time_format
        self.ddns_dual_stack_mixed_mode = ddns_dual_stack_mixed_mode
        self.ddns_guard_id_must_match = ddns_guard_id_must_match
        self.ddns_other_guard_is_dynamic = ddns_other_guard_is_dynamic
        self.lease_file_name = lease_file_name
        self.dhcpv6_lease_file_name = dhcpv6_lease_file_name
        self.local_port = local_port
        self.local_address = local_address
        self.local_address6 = local_address6
        self.bind_local_address6 = bind_local_address6
        self.log_facility = log_facility
        self.omapi_port = omapi_port
        self.omapi_key = omapi_key
        self.pid_file_name =pid_file_name
        self.dhcpv6_pid_file_name = dhcpv6_pid_file_name
        self.release_on_roam = release_on_roam
        self.remote_port = remote_port
        self.server_id_check = server_id_check
        self.server_duid =server_duid
        self.update_conflict_detection =update_conflict_detection
        self.use_eui_64 =use_eui_64
        self.persist_eui_64_leases = persist_eui_64_leases
        self.options = [] if not options else options
        self.keys = [] if not keys else keys
        self.zones = [] if not zones else zones
        self.failover = failover
        self.subnets = [] if not subnets else subnets
        self.shared_networks = [] if not shared_networks else shared_networks
        self.groups = [] if not groups else groups
        self.hosts = [] if not hosts else hosts
        self.classes = [] if not classes else classes
        self.subclasses = [] if not subclasses else subclasses
        self.includes = [] if not includes else includes
        super().__init__()
    def __str__(self) -> str:
        return f'Global'
    def __repr__(self) -> str:
        return f'Global()'
    def to_isc(self):
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                            Default is 0.

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        sort_order = {
            'options': 1,
            'includes': 2,
            'keys': 3,
            'zones': 4,
            'failover': 5,
            'subnets': 6,
            'shared_networks': 7,
            'classes': 8,
            'subclasses': 9, 
            'hosts': 10,
            'groups': 11
            }
        sorted_dict = sorted(self.__dict__.items(), key=lambda x: sort_order.get(x[0], 0))
        for key, value in sorted_dict:
            new_key = key.replace("_", "-")
            if value and key == 'failover':
                attrs.append(value.to_isc())
            elif all((isinstance(value, bool), key == 'authoritative')):
                if value:
                    attrs.append(f'{key};')
                else:
                    attrs.append(f'not {key};')
            elif isinstance(value, list):
                for item in value:
                    attrs.append(item.to_isc())
            elif value:
                attrs.append(f'{new_key} {value};')
        attrs_str = "\n".join(attrs)
        return (f'{attrs_str}')
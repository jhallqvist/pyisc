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

from typing import List, Tuple, Union


# TODO - Maybe redo a few thing - create a to_isc that can be inherited that 
# for instance joins the values that are lists within brackets.

# Non regular parameters.
class BaseAML:
    """Represents an Address match statment.

    This class is not meant to be instantiated but to serve as a common base
    for other classes that has the same structure.

    """
    def __init__(self, elements: List[str] = None) -> None:
        """Initialize attributes for the class.

        Args:
            elements (List[str]): A list of addresses to match.
                The expected values for the entries in this list is:
                ip addresses, ip prefixes key IDs, another ACL or any or the
                predefined options (any, none, localhost, localnets).
                A leading exclamation mark in an element is also allowed to 
                negate the element.

        """
        self.elements = [] if not elements else elements

    def __str__(self, parameter=None) -> str:
        prefix = f'{parameter if parameter else self.__class__.__name__}'
        stmt_name = f'{" " + self.name if hasattr(self, "name") else ""}'
        return f'{prefix}{stmt_name}'

    def __repr__(self) -> str:
        stmt_name = f'{"name=" + self.name if hasattr(self, "name") else ""}'
        return f'{self.__class__.__name__}({stmt_name})'

    def to_isc(self, indent: int = 0, element_pos: int = -1) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        Examples:
            >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        excluded_attrs = ('name', 'elements')
        addr_str = ('{ ' f'{"; ".join(self.elements)};' ' }')
        for key, value in self.__dict__.items():
            key = key.replace('_', '-')
            if any((key in excluded_attrs, not value)):
                continue
            elif isinstance(value, list):
                attrs.append((f'{key} ' '{ ' f'{"; ".join(value)};' ' }'))
            else:
                attrs.append(f'{key} {value}')
        return_str = f'{" " * indent}{self.__str__()}'
        if element_pos == -1:
            position = len(attrs)
        else:
            position = element_pos
        attrs.insert(position, addr_str)
        attrs_str = " " + " ".join(attrs)
        section_end = ';'
        return (f'{return_str}{attrs_str}{section_end}')


# class AllowNotify(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-notify')


# class AllowQuery(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-query')


# class AllowQueryCache(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-query-cache')


# class AllowQueryCacheOn(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-query-cache-on')


# class AllowRecursion(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-recursion')


# class AllowRecursionOn(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-recursion-on')


# class AllowTransfer(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-transfer')


# class AllowUpdate(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-update')


# class AllowUpdateForwarding(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='allow-update-forwarding')


# class Blackhole(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='blackhole')


class DenyAnswerAddress(BaseAML):
    def __init__(
        self,
        elements:       List[str] = None,
        except_from:    List[str] = None
    ) -> None:
        self.except_from = [] if not except_from else except_from
        super().__init__(elements=elements)

    def __str__(self) -> str:
        return super().__str__(parameter='deny-answer-addresses')

    def to_isc(self, indent: int = 0, element_pos: int = 0) -> str:
        return super().to_isc(indent=indent, element_pos=element_pos)


# class Clients(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='clients')


# class Exclude(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='exclude')


# class Mapped(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='mapped')


# class KeepResponseOrder(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='keep-response-order')


class ListenOn(BaseAML):
    def __init__(
        self,
        port:       int = None,
        dscp:       int = None,
        tls:        str = None,
        http:       str = None,
        elements:   List[str] = None
    ) -> None:
        self.port = port
        self.dscp = dscp
        self.tls = tls
        self.http = http
        super().__init__(elements=elements)

    def __str__(self) -> str:
        return super().__str__(parameter='listen-on')


class ListenOnV6(ListenOn):
    def __str__(self) -> str:
        return super().__str__(parameter='listen-on-v6')


# class NoCaseCompress(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='no-case-compress')


# class ExemptClients(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='exempt-clients')


class ResponsePadding(BaseAML):
    def __init__(
        self,
        block_size: int,
        elements:   List[str] = None
    ) -> None:
        self.block_size = block_size
        super().__init__(elements=elements)

    def __str__(self) -> str:
        return super().__str__(parameter='response-padding')

    def to_isc(self, indent: int = 0, element_pos: int = 0) -> str:
        return super().to_isc(indent=indent, element_pos=element_pos)


class AltTransferSource:
    pass

# class SortList(BaseAML):
#     def __str__(self) -> str:
#         return super().__str__(parameter='sortlist')


# Statements
class Acl(BaseAML):
    def __init__(self, name: str, elements: List[str] = None) -> None:
        self.name = name
        super().__init__(elements=elements)

    def __str__(self) -> str:
        return super().__str__(parameter='acl')
# class Acl:
#     """Represents an ACL statment."""
#     def __init__(self, name: str, acl_elements: List[str] = None) -> None:
#         """Initialize attributes for the class.

#         Args:
#             name (str): The name of the ACL.
#             acl_elements (List[str]): A list of addresses to match.
#                 The expected values for the entries in this list is:
#                 ip addresses, ip prefixes key IDs, another ACL or any or the
#                 predefined options (any, none, localhost, localnets).
#                 A leading exclamation mark in an element is also allowed to 
#                 negate the element.

#         """
#         self.name = name
#         self.acl_elements = [] if not acl_elements else acl_elements

#     def __str__(self) -> str:
#         return f'acl {self.name}'

#     def __repr__(self) -> str:
#         return f'Acl(name={self.name})'

#     def to_isc(self, indent: int = 0) -> str:
#         """Returns valid ISC configuration as a string.

#         Args:
#             indent (int): Supply an integer to use as indentation offset.
#                 Default is 0.

#         Examples:
#             >>> pass

#         Returns:
#             str: A string representation of the object tree from this level.

#         """
#         child_indent = indent * 2 if indent > 0 else 4
#         addr_list = []
#         for addr in self.acl_elements:
#             addr_list.append(f'{" " * child_indent}{addr};')
#         return_str = (f'{" " * indent}{self.__str__()}' ' {')
#         if len(addr_list) > 0:
#             return_str += '\n'
#         addr_str = "\n".join(addr_list)
#         section_end = '};'
#         return (f'{return_str}{addr_str}' '\n' f'{" " * indent}{section_end}')


class ControlsInet:
    """Represents an INET controls statment."""
    def __init__(
        self,
        ip_addr:    str,
        allow:      List[str],
        ip_port:    Union[int, str, None] = None,
        keys:       Union[List[str], None] = None,
        read_only:  bool = False
    ) -> None:
        self.ip_addr = ip_addr
        self.allow = allow
        self.ip_port = ip_port
        self.keys = [] if not keys else keys
        self.read_only = read_only

    def __str__(self) -> str:
        return 'controls'

    def __repr__(self) -> str:
        return f'ControlsInet(ip_addr={self.ip_addr}, allow={self.allow})'

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
        child_indent = indent * 2 if indent > 0 else 4
        if self.allow:
            allow_str = (' allow { ' f'{"; ".join(self.allow)}' '; }')
        else:
            allow_str = ''
        if self.keys:
            keys_str = (' keys { ' f'{"; ".join(self.keys)}' '; }')
        else:
            keys_str = ''
        if self.read_only:
            read_only_str = (' read-only ' f'{str(self.read_only).lower()}')
        else:
            read_only_str = ''
        return_str = (f'{" " * indent}{self.__str__()}'
                      ' {\n'
                      f'{" " * child_indent}inet {self.ip_addr}'
                      f'{" " + str(self.ip_port) if self.ip_port else ""} '
                      f'{allow_str}'
                      f'{keys_str}'
                      f'{read_only_str}'
                      ';')
        section_end = '};'
        return (f'{return_str}' '\n' f'{" " * indent}{section_end}')


class ControlsUnix:
    """Represents an Unix controls statment."""
    def __init__(
        self,
        path:       str,
        permission: int,
        owner:      int,
        group:      int,
        keys:       Union[List[str], None] = None,
        read_only:  bool = False
    ) -> None:
        self.path = path
        self.permission = permission
        self.owner = owner
        self.group = group
        self.keys = [] if not keys else keys
        self.read_only = read_only

    def __str__(self) -> str:
        return 'controls'

    def __repr__(self) -> str:
        return (f'ControlsUnix(path={self.path}, permission={self.permission})'
                f',owner={self.owner}, group={self.group})')

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
        child_indent = indent * 2 if indent > 0 else 4
        if self.keys:
            keys_str = (' keys { ' f'{"; ".join(self.keys)}' '; }')
        else:
            keys_str = ''
        if self.read_only:
            read_only_str = (' read-only ' f'{str(self.read_only).lower()}')
        else:
            read_only_str = ''
        return_str = (f'{" " * indent}{self.__str__()}'
                      ' {\n'
                      f'{" " * child_indent}unix {self.path}'
                      f' perm {self.permission} owner {self.owner}'
                      f' group {self.group}'
                      f'{keys_str}'
                      f'{read_only_str}'
                      ';')
        section_end = '};'
        return (f'{return_str}' '\n' f'{" " * indent}{section_end}')


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

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        Examples:
            >>> include = Include(filename='/etc/rndc.key')
            >>> print(include.to_isc())
            include /etc/rndc.key;

        Returns:
            str: A string representation of the object tree from this level.

        """
        return f'{" " * indent}{self.__str__()};'


class Key:
    """Represents an key declaration and parameter."""
    def __init__(
        self,
        name:       str,
        algorithm:  Union[str, None] = None,
        secret:     Union[str, None] = None
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

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> key = Key(name='DHCP_UPDATER')
        >>> print(key.to_isc())
        key DHCP_UPDATER {
        }

        >>> key.secret = 'Ofakekeyfakekeyfakekey=='
        >>> print(key.to_isc())
        key DHCP_UPDATER {
            secret Ofakekeyfakekeyfakekey==;
        };

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent * 2 if indent > 0 else 4
        for key, value in self.__dict__.items():
            if all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '};'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class ChannelFile:
    """Represents the file parameter of the logging channel statement."""
    def __init__(
        self,
        name:       str,
        versions:   Union[str, int, None] = None,
        size:       Union[str, int, None] = None,
        suffix:     Union[str, None] = None
    ) -> None:
        self.name = name
        self.versions = versions
        self.size = size
        self.suffix = suffix

    def __str__(self) -> str:
        return f'file {self.name}'

    def __repr__(self) -> str:
        return f'ChannelFile(name={self.name})'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        return_str = f'{" " * indent}{self.__str__()}'
        for key, value in self.__dict__.items():
            if all((value, key != 'name')):
                attrs.append(f'{key} {value}')
        attrs_str = " " + " ".join(attrs) if attrs else ""
        section_end = ';'
        return f'{return_str}{attrs_str}{section_end}'


class LogChannel:
    """Represents the logging channel statement."""
    def __init__(
        self,
        name:           str,
        buffered:       Union[bool, None] = None,
        file:           Union[ChannelFile, None] = None,
        null:           Union[bool, None] = None,
        print_category: Union[bool, None] = None,
        print_severity: Union[bool, None] = None,
        print_time:     Union[str, bool, None] = None,
        severity:       Union[str, None] = None,
        stderr:         Union[bool, None] = None,
        syslog:         Union[str, None] = None
    ) -> None:
        self.name = name
        self.buffered = buffered
        self.file = file
        self.null = null
        self.print_category = print_category
        self.print_severity = print_severity
        self.print_time = print_time
        self.severity = severity
        self.stderr = stderr
        self.syslog = syslog

    def __str__(self) -> str:
        return f'channel {self.name}'

    def __repr__(self) -> str:
        return f'LogChannel(name={self.name})'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent * 2 if indent > 0 else 4
        for key, value in self.__dict__.items():
            if key in ('null', 'stderr'):
                attrs.append(f'{" " * child_indent}{key};')
            elif isinstance(value, bool):
                attrs.append(f'{" " * child_indent}{key} {str(value).lower()};')
            elif hasattr(value, 'to_isc'):
                attrs.append(f'{" " * child_indent}{value.to_isc()}')
            elif all((value, key != 'name')):
                attrs.append(f'{" " * child_indent}{key} {value};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '};'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class LogCategory:
    """Represents the logging category statement."""
    def __init__(self, name: str, channels: List[LogChannel]) -> None:
        self.name = name
        self.channels = [] if not channels else channels

    def __str__(self) -> str:
        return f'category {self.name}'

    def __repr__(self) -> str:
        return f'LogCategory(name={self.name})'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        for channel in self.channels:
            attrs.append(f'{channel.name};')
        attrs_str = " " + " ".join(attrs) + " "
        section_end = '};'
        return f'{return_str}{attrs_str}{section_end}'


class Logging:
    """Represents the logging statement."""
    def __init__(
        self,
        categories: List[LogCategory],
        channels:   List[LogChannel]
    ) -> None:
        self.categories = [] if not categories else categories
        self.channels = [] if not channels else channels

    def __str__(self) -> str:
        return 'logging'

    def __repr__(self) -> str:
        return 'Logging()'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent * 2 if indent > 0 else 4
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        for category in self.categories:
            attrs.append(f'{category.to_isc(indent=child_indent)}')
        for channel in self.channels:
            attrs.append(f'{channel.to_isc(indent=child_indent)}')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '};'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class BaseZoneList:
    """Ancestor to parental-agents, primaries, also-notify and masters
    statements."""
    def __init__(
        self,
        port:           Union[int, None] = None,
        dscp:           Union[int, None] = None,
        servers:        Union[List[str], Tuple[str, int]] = None,
        key:            Union[str, None] = None,
        tls:            Union[str, None] = None
    ) -> None:
        self.port = port
        self.dscp = dscp
        self.servers = servers
        self.key = key
        self.tls = tls

    def __str__(self, parameter=None) -> str:
        optional_attrs = ''
        if self.port:
            optional_attrs += f' port {self.port}'
        if self.dscp:
            optional_attrs += f' dscp {self.dscp}'
        prefix = f'{parameter if parameter else self.__class__.__name__}'
        stmt_name = f'{" " + self.name if hasattr(self, "name") else ""}'
        return f'{prefix}{stmt_name}{optional_attrs}'

    def __repr__(self) -> str:
        optional_attrs = ''
        if self.port:
            optional_attrs += f', port={self.port}'
        if self.dscp:
            optional_attrs += f', dscp={self.dscp}'
        stmt_name = f'{"name=" + self.name if hasattr(self, "name") else ""}'
        return f'{self.__class__.__name__}({stmt_name}{optional_attrs})'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        excluded_attrs = ('name', 'port', 'dscp')
        child_indent = indent * 2 if indent > 0 else 4
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        for key, value in self.__dict__.items():
            key = key.replace('_', '-')
            if any((key in excluded_attrs, not value)):
                continue
            elif all((key == 'servers', isinstance(value, list))):
                attrs.append(f'{" " * child_indent}{", ".join(value)};')
            elif all((key == 'servers', isinstance(value, str))):
                attrs.append(f'{" " * child_indent}{value};')
            elif all((key == 'servers', isinstance(value, tuple))):
                addr, port = value
                attrs.append(f'{" " * child_indent}{addr} port {port};')
            else:
                attrs.append(f'{" " * child_indent}{key} {value};')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '};'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class ParentalAgents(BaseZoneList):
    """Represents the parental-agents statement."""
    def __init__(
        self,
        name:           str,
        port:           Union[int, None] = None,
        dscp:           Union[int, None] = None,
        servers:        Union[List[str], Tuple[str, int]] = None,
        key:            Union[str, None] = None,
        tls:            Union[str, None] = None
    ) -> None:
        self.name = name
        super().__init__(port=port, dscp=dscp, servers=servers, key=key, tls=tls)

    def __str__(self) -> str:
        return super().__str__(parameter='parental-agent')

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        return super().to_isc(indent=indent)


class Primaries(BaseZoneList):
    """Represents the primaries statement."""
    def __init__(
        self,
        name:           str,
        port:           Union[int, None] = None,
        dscp:           Union[int, None] = None,
        servers:        Union[List[str], Tuple[str, int]] = None,
        key:            Union[str, None] = None,
        tls:            Union[str, None] = None
    ) -> None:
        self.name = name
        super().__init__(port=port, dscp=dscp, servers=servers, key=key, tls=tls)

    def __str__(self) -> str:
        return super().__str__(parameter='primaries')

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        return super().to_isc(indent=indent)


class AlsoNotify(BaseZoneList):
    """Represents the also-notify statement."""

    def __str__(self) -> str:
        return super().__str__(parameter='also-notify')

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        return super().to_isc(indent=indent)


class Masters(BaseZoneList):
    """Represents the masters statement."""

    def __str__(self) -> str:
        return super().__str__(parameter='masters')

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        return super().to_isc(indent=indent)


class Options:
    def __init__(
        self,
        allow_new_zones:            Union[bool, None] = None,
        allow_notify:               Union[List, None] = None,
        allow_query:                Union[List, None] = None,
        allow_query_cache:          Union[List, None] = None,
        allow_query_cache_on:       Union[List, None] = None,
        allow_query_on:             Union[List, None] = None,
        allow_recursion:            Union[List, None] = None,
        allow_recursion_on:         Union[List, None] = None,
        allow_transfer:             Union[List, None] = None,
        allow_update:               Union[List, None] = None,
        allow_update_forwarding:    Union[List, None] = None,
        also_notify:                Union[AlsoNotify, None] = None,
        alt_transfer_source:        Union[AltTransferSource, None] = None,
    ) -> None:
        self.allow_new_zones = allow_new_zones
        self.allow_notify = allow_notify
        self.allow_query = allow_query
        self.allow_query_cache = allow_query_cache
        self.allow_query_cache_on = allow_query_cache_on
        self.allow_query_on = allow_query_on
        self.allow_recursion = allow_recursion
        self.allow_recursion_on = allow_recursion_on
        self.allow_transfer = allow_transfer
        self.allow_update = allow_update
        self.allow_update_forwarding = allow_update_forwarding
        self.also_notify = also_notify
        self.alt_transfer_source = alt_transfer_source

    def __str__(self) -> str:
        return 'options'

    def __repr__(self) -> str:
        return 'Options()'

    def to_isc(self, indent: int = 0) -> str:
        """Returns valid ISC configuration as a string.

        Args:
            indent (int): Supply an integer to use as indentation offset.
                Default is 0.

        >>> pass

        Returns:
            str: A string representation of the object tree from this level.

        """
        attrs = []
        child_indent = indent * 2 if indent > 0 else 4
        excluded_attrs = ''
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        for key, value in self.__dict__.items():
            key = key.replace('_', '-')
            if any((key in excluded_attrs, not value)):
                continue
            elif isinstance(value, bool):
                attrs.append(f'{" " * child_indent}{key} {str(value).lower()};')
            elif isinstance(value, list):
                value_list = ('{ ' f'{"; ".join(value)};' ' }')
                attrs.append((f'{" " * child_indent}{key} ' f'{value_list};'))
            elif hasattr(value, 'to_isc'):
                attrs.append(f'{value.to_isc(indent=child_indent)}')
            else:
                attrs.append(f'{" " * child_indent}{key} {value};')
        if len(attrs) > 0:
            return_str += '\n'
        attrs_str = "\n".join(attrs)
        section_end = '};'
        return (f'{return_str}{attrs_str}' '\n' f'{" " * indent}{section_end}')


class Server:
    pass


class StatisticsChannels:
    pass


class Tls:
    pass


class Http:
    pass


class TrustAnchors:
    pass


class DnsSecPolicy:
    pass


class ManagedKeys:
    pass


class TrustedKeys:
    pass


class View:
    pass


class Zone:
    pass

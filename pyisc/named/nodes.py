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

from typing import List, Optional, Tuple, Union


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
        # print("    " + ";\n    ".join(test.elements) + ";")
        excluded_attrs = ('name', 'elements')
        addr_str = ('{ ' f'{"; ".join(self.elements)};' ' }')
        for key, value in self.__dict__.items():
            key = key.replace('_', '-')
            if any((key in excluded_attrs, value is None)):
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


class DenyAnswerAlias(DenyAnswerAddress):
    pass

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


class BaseSource:
    """Ancestor to alt-transfer-source, alt-transfer-source-v6, notify-source
    and notify-source-v6, parental-source, parental-source-v6, transfer-source
    and transfer-source-v6 statements."""
    def __init__(
        self,
        address:    str,
        port:       Union[int, None] = None,
        dscp:       Union[int, None] = None
    ) -> None:
        self.address = address
        self.port = port
        self.dscp = dscp

    def __str__(self, parameter=None) -> str:
        prefix = f'{parameter if parameter else self.__class__.__name__}'
        return f'{prefix}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(address={self.address})'

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
        attrs = []
        return_str = (f'{" " * indent}{self.__str__()} ')
        for key, value in self.__dict__.items():
            key = key.replace('_', '-')
            if not value:
                continue
            elif key == 'address':
                attrs.append(f'{value}')
            else:
                attrs.append(f'{key} {value}')
        attrs_str = " ".join(attrs)
        section_end = ';'
        return (f'{return_str}{attrs_str}{section_end}')


class AltTransferSource(BaseSource):
    """Represents the alt-transfer-source parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='alt-transfer-source')


class AltTransferSourceV6(BaseSource):
    """Represents the alt-transfer-source-v6 parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='alt-transfer-source-v6')


class NotifySource(BaseSource):
    """Represents the notify-source parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='notify-source')


class NotifySourceV6(BaseSource):
    """Represents the notify-source-v6 parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='notify-source-v6')


class ParentalSource(BaseSource):
    """Represents the parental-source parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='parental-source')


class ParentalSourceV6(BaseSource):
    """Represents the parental-source-v6 parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='parental-source-v6')


class TransferSource(BaseSource):
    """Represents the parental-source parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='transfer-source')


class TransferSourceV6(BaseSource):
    """Represents the parental-source-v6 parameter."""
    def __str__(self) -> str:
        return super().__str__(parameter='transfer-source-v6')


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
                attrs.append(f'{value.to_isc(indent=child_indent)}')
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
            if any((key in excluded_attrs, value is None)):
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
        alt_transfer_source_v6:     Union[AltTransferSourceV6, None] = None,
        answer_cookie:              Union[bool, None] = None,
        attach_cache:               Union[str, None] = None,
        auth_nxdomain:              Union[bool, None] = None,
        auto_dnssec:                Union[str, None] = None,
        automatic_interface_scan:   Union[bool, None] = None,
        avoid_v4_udp_ports:         Union[List, None] = None,
        avoid_v6_udp_ports:         Union[List, None] = None,
        bindkeys_file:              Union[str, None] = None,
        blackhole:                  Union[List, None] = None,
        cache_file:                 Union[str, None] = None,
        # Finish below
        catalog_zones:                      Optional[object] = None, # Not done
        check_dup_records:                  Optional[str] = None,
        check_integrity:                    Optional[bool] = None,
        check_mx:                           Optional[str] = None,
        check_mx_cname:                     Optional[str] = None,
        check_names:                        Optional[str] = None,
        check_sibling:                      Optional[bool] = None,
        check_spf:                          Optional[str] = None,
        check_srv_cname:                    Optional[str] = None,
        check_wildcard:                     Optional[bool] = None,
        clients_per_query:                  Optional[int] = None,
        cookie_algorithm:                   Optional[str] = None,
        cookie_secret:                      Optional[str] = None,
        coresize:                           Optional[str] = None,
        datasize:                           Optional[str] = None,
        deny_answer_addresses:              Optional[DenyAnswerAddress] = None,
        deny_answer_aliases:                Optional[DenyAnswerAlias] = None,
        dialup:                             Optional[Union[str, bool]] = None,
        directory:                          Optional[str] = None,
        disable_algorithms:                 Optional[object] = None,
        disable_ds_digests:                 Optional[object] = None,
        disable_empty_zone:                 Optional[object] = None,
        dns64:                              Optional[object] = None,
        dns64_contact:                      Optional[object] = None,
        dns64_server:                       Optional[object] = None,
        dnskey_sig_validity:                Optional[object] = None,
        dnsrps_enable:                      Optional[object] = None,
        dnsrps_options:                     Optional[object] = None,
        dnssec_accept_expired:              Optional[object] = None,
        dnssec_dnskey_kskonly:              Optional[object] = None,
        dnssec_loadkeys_interval:           Optional[object] = None,
        dnssec_must_be_secure:              Optional[object] = None,
        dnssec_policy:                      Optional[object] = None,
        dnssec_secure_to_insecure:          Optional[object] = None,
        dnssec_update_mode:                 Optional[object] = None,
        dnssec_validation:                  Optional[object] = None,
        dnstap:                             Optional[object] = None,
        dnstap_identity:                    Optional[object] = None,
        dnstap_output:                      Optional[object] = None,
        dnstap_version:                     Optional[object] = None,
        dscp:                               Optional[object] = None,
        dual_stack_servers:                 Optional[object] = None,
        dump_file:                          Optional[object] = None,
        edns_udp_size:                      Optional[object] = None,
        empty_contact:                      Optional[object] = None,
        empty_server:                       Optional[object] = None,
        empty_zones_enable:                 Optional[object] = None,
        fetch_quota_params:                 Optional[object] = None,
        fetches_per_server:                 Optional[object] = None,
        fetches_per_zone:                   Optional[object] = None,
        files:                              Optional[object] = None,
        flush_zones_on_shutdown:            Optional[object] = None,
        forward:                            Optional[object] = None,
        forwarders:                         Optional[object] = None,
        fstrm_set_buffer_hint:              Optional[object] = None,
        fstrm_set_flush_timeout:            Optional[object] = None,
        fstrm_set_input_queue_size:         Optional[object] = None,
        fstrm_set_output_notify_threshold:  Optional[object] = None,
        fstrm_set_output_queue_model:       Optional[object] = None,
        fstrm_set_output_queue_size:        Optional[object] = None,
        fstrm_set_reopen_interval:          Optional[object] = None,
        geoip_directory:                    Optional[object] = None,
        glue_cache:                         Optional[object] = None,
        heartbeat_interval:                 Optional[object] = None,
        hostname:                           Optional[object] = None,
        http_listener_clients:              Optional[object] = None,
        http_port:                          Optional[object] = None,
        http_streams_per_connection:        Optional[object] = None,
        https_port:                         Optional[object] = None,
        interface_interval:                 Optional[object] = None,
        ipv4only_contact:                   Optional[object] = None,
        ipv4only_enable:                    Optional[object] = None,
        ipv4only_server:                    Optional[object] = None,
        ixfr_from_differences:              Optional[object] = None,
        keep_response_order:                Optional[object] = None,
        key_directory:                      Optional[object] = None,
        lame_ttl:                           Optional[object] = None,
        listen_on:                          Optional[object] = None,
        listen_on_v6:                       Optional[object] = None,
        lmdb_mapsize:                       Optional[object] = None,
        lock_file:                          Optional[object] = None,
        managed_keys_directory:             Optional[object] = None,
        masterfile_format:                  Optional[object] = None,
        masterfile_style:                   Optional[object] = None,
        match_mapped_addresses:             Optional[object] = None,
        max_cache_size:                     Optional[object] = None,
        max_cache_ttl:                      Optional[object] = None,
        max_clients_per_query:              Optional[object] = None,
        max_ixfr_ratio:                     Optional[object] = None,
        max_journal_size:                   Optional[object] = None,
        max_ncache_ttl:                     Optional[object] = None,
        max_records:                        Optional[object] = None,
        max_recursion_depth:                Optional[object] = None,
        max_recursion_queries:              Optional[object] = None,
        max_refresh_time:                   Optional[object] = None,
        max_retry_time:                     Optional[object] = None,
        max_rsa_exponent_size:              Optional[object] = None,
        max_stale_ttl:                      Optional[object] = None,
        max_transfer_idle_in:               Optional[object] = None,
        max_transfer_idle_out:              Optional[object] = None,
        max_transfer_time_in:               Optional[object] = None,
        max_transfer_time_out:              Optional[object] = None,
        max_udp_size:                       Optional[object] = None,
        max_zone_ttl:                       Optional[object] = None,
        memstatistics:                      Optional[object] = None,
        memstatistics_file:                 Optional[object] = None,
        message_compression:                Optional[object] = None,
        min_cache_ttl:                      Optional[object] = None,
        min_ncache_ttl:                     Optional[object] = None,
        min_refresh_time:                   Optional[object] = None,
        min_retry_time:                     Optional[object] = None,
        minimal_any:                        Optional[object] = None,
        minimal_responses:                  Optional[object] = None,
        multi_master:                       Optional[object] = None,
        new_zones_directory:                Optional[object] = None,
        no_case_compress:                   Optional[object] = None,
        nocookie_udp_size:                  Optional[object] = None,
        notify:                             Optional[object] = None,
        notify_delay:                       Optional[object] = None,
        notify_rate:                        Optional[object] = None,
        notify_source:                      Optional[object] = None,
        notify_source_v6:                   Optional[object] = None,
        notify_to_soa:                      Optional[object] = None,
        nta_lifetime:                       Optional[object] = None,
        nta_recheck:                        Optional[object] = None,
        nxdomain_redirect:                  Optional[object] = None,
        parental_source:                    Optional[object] = None,
        parental_source_v6:                 Optional[object] = None,
        pid_file:                           Optional[object] = None,
        port:                               Optional[object] = None,
        preferred_glue:                     Optional[object] = None,
        prefetch:                           Optional[object] = None,
        provide_ixfr:                       Optional[object] = None,
        qname_minimization:                 Optional[object] = None,
        query_source:                       Optional[object] = None,
        query_source_v6:                    Optional[object] = None,
        querylog:                           Optional[object] = None,
        random_device:                      Optional[object] = None,
        rate_limit:                         Optional[object] = None,
        recursing_file:                     Optional[object] = None,
        recursion:                          Optional[object] = None,
        recursive_clients:                  Optional[object] = None,
        request_expire:                     Optional[object] = None,
        request_ixfr:                       Optional[object] = None,
        request_nsid:                       Optional[object] = None,
        require_server_cookie:              Optional[object] = None,
        reserved_sockets:                   Optional[object] = None,
        resolver_nonbackoff_tries:          Optional[object] = None,
        resolver_query_timeout:             Optional[object] = None,
        resolver_retry_interval:            Optional[object] = None,
        response_padding:                   Optional[object] = None,
        response_policy:                    Optional[object] = None,
        root_delegation_only:               Optional[object] = None,
        root_key_sentinel:                  Optional[object] = None,
        rrset_order:                        Optional[object] = None,
        secroots_file:                      Optional[object] = None,
        send_cookie:                        Optional[object] = None,
        serial_query_rate:                  Optional[object] = None,
        serial_update_method:               Optional[object] = None,
        server_id:                          Optional[object] = None,
        servfail_ttl:                       Optional[object] = None,
        session_keyalg:                     Optional[object] = None,
        session_keyfile:                    Optional[object] = None,
        session_keyname:                    Optional[object] = None,
        sig_signing_nodes:                  Optional[object] = None,
        sig_signing_signatures:             Optional[object] = None,
        sig_signing_type:                   Optional[object] = None,
        sig_validity_interval:              Optional[object] = None,
        sortlist:                           Optional[object] = None,
        stacksize:                          Optional[object] = None,
        stale_answer_client_timeout:        Optional[object] = None,
        stale_answer_enable:                Optional[object] = None,
        stale_answer_ttl:                   Optional[object] = None,
        stale_cache_enable:                 Optional[object] = None,
        stale_refresh_time:                 Optional[object] = None,
        startup_notify_rate:                Optional[object] = None,
        statistics_file:                    Optional[object] = None,
        synth_from_dnssec:                  Optional[object] = None,
        tcp_advertised_timeout:             Optional[object] = None,
        tcp_clients:                        Optional[object] = None,
        tcp_idle_timeout:                   Optional[object] = None,
        tcp_initial_timeout:                Optional[object] = None,
        tcp_keepalive_timeout:              Optional[object] = None,
        tcp_listen_queue:                   Optional[object] = None,
        tcp_receive_buffer:                 Optional[object] = None,
        tcp_send_buffer:                    Optional[object] = None,
        tkey_dhkey:                         Optional[object] = None,
        tkey_domain:                        Optional[object] = None,
        tkey_gssapi_credential:             Optional[object] = None,
        tkey_gssapi_keytab:                 Optional[object] = None,
        tls_port:                           Optional[object] = None,
        transfer_format:                    Optional[object] = None,
        transfer_message_size:              Optional[object] = None,
        transfer_source:                    Optional[object] = None,
        transfer_source_v6:                 Optional[object] = None,
        transfers_in:                       Optional[object] = None,
        transfers_out:                      Optional[object] = None,
        transfers_per_ns:                   Optional[object] = None,
        trust_anchor_telemetry:             Optional[object] = None,
        try_tcp_refresh:                    Optional[object] = None,
        udp_receive_buffer:                 Optional[object] = None,
        udp_send_buffer:                    Optional[object] = None,
        update_check_ksk:                   Optional[object] = None,
        use_alt_transfer_source:            Optional[object] = None,
        use_v4_udp_ports:                   Optional[object] = None,
        use_v6_udp_ports:                   Optional[object] = None,
        v6_bias:                            Optional[object] = None,
        validate_except:                    Optional[object] = None,
        version:                            Optional[object] = None,
        zero_no_soa_ttl:                    Optional[object] = None,
        zero_no_soa_ttl_cache:              Optional[object] = None,
        zone_statistics:                    Optional[object] = None,
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
        self.alt_transfer_source_v6 = alt_transfer_source_v6
        self.answer_cookie = answer_cookie
        self.attach_cache = attach_cache
        self.auth_nxdomain = auth_nxdomain
        self.auto_dnssec = auto_dnssec
        self.automatic_interface_scan = automatic_interface_scan
        self.avoid_v4_udp_ports = avoid_v4_udp_ports
        self.avoid_v6_udp_ports = avoid_v6_udp_ports
        self.bindkeys_file = bindkeys_file
        self.blackhole = blackhole
        self.cache_file = cache_file
        self.catalog_zones = catalog_zones
        self.check_dup_records = check_dup_records
        self.check_integrity = check_integrity
        self.check_mx = check_mx
        self.check_mx_cname = check_mx_cname
        self.check_names = check_names
        self.check_sibling = check_sibling
        self.check_spf = check_spf
        self.check_srv_cname = check_srv_cname
        self.check_wildcard = check_wildcard
        self.clients_per_query = clients_per_query
        self.cookie_algorithm = cookie_algorithm
        self.cookie_secret = cookie_secret
        self.coresize = coresize
        self.datasize = datasize
        self.deny_answer_addresses = deny_answer_addresses
        self.deny_answer_aliases = deny_answer_aliases
        self.dialup = dialup
        self.directory = directory
        self.disable_algorithms = disable_algorithms
        self.disable_ds_digests = disable_ds_digests
        self.disable_empty_zone = disable_empty_zone
        self.dns64 = dns64
        self.dns64_contact = dns64_contact
        self.dns64_server = dns64_server
        self.dnskey_sig_validity = dnskey_sig_validity
        self.dnsrps_enable = dnsrps_enable
        self.dnsrps_options = dnsrps_options
        self.dnssec_accept_expired = dnssec_accept_expired
        self.dnssec_dnskey_kskonly = dnssec_dnskey_kskonly
        self.dnssec_loadkeys_interval = dnssec_loadkeys_interval
        self.dnssec_must_be_secure = dnssec_must_be_secure
        self.dnssec_policy = dnssec_policy
        self.dnssec_secure_to_insecure = dnssec_secure_to_insecure
        self.dnssec_update_mode = dnssec_update_mode
        self.dnssec_validation = dnssec_validation
        self.dnstap = dnstap
        self.dnstap_identity = dnstap_identity
        self.dnstap_output = dnstap_output
        self.dnstap_version = dnstap_version
        self.dscp = dscp
        self.dual_stack_servers = dual_stack_servers
        self.dump_file = dump_file
        self.edns_udp_size = edns_udp_size
        self.empty_contact = empty_contact
        self.empty_server = empty_server
        self.empty_zones_enable = empty_zones_enable
        self.fetch_quota_params = fetch_quota_params
        self.fetches_per_server = fetches_per_server
        self.fetches_per_zone = fetches_per_zone
        self.files = files
        self.flush_zones_on_shutdown = flush_zones_on_shutdown
        self.forward = forward
        self.forwarders = forwarders
        self.fstrm_set_buffer_hint = fstrm_set_buffer_hint
        self.fstrm_set_flush_timeout = fstrm_set_flush_timeout
        self.fstrm_set_input_queue_size = fstrm_set_input_queue_size
        self.fstrm_set_output_notify_threshold = fstrm_set_output_notify_threshold
        self.fstrm_set_output_queue_model = fstrm_set_output_queue_model
        self.fstrm_set_output_queue_size = fstrm_set_output_queue_size
        self.fstrm_set_reopen_interval = fstrm_set_reopen_interval
        self.geoip_directory = geoip_directory
        self.glue_cache = glue_cache
        self.heartbeat_interval = heartbeat_interval
        self.hostname = hostname
        self.http_listener_clients = http_listener_clients
        self.http_port = http_port
        self.http_streams_per_connection = http_streams_per_connection
        self.https_port = https_port
        self.interface_interval = interface_interval
        self.ipv4only_contact = ipv4only_contact
        self.ipv4only_enable = ipv4only_enable
        self.ipv4only_server = ipv4only_server
        self.ixfr_from_differences = ixfr_from_differences
        self.keep_response_order = keep_response_order
        self.key_directory = key_directory
        self.lame_ttl = lame_ttl
        self.listen_on = listen_on
        self.listen_on_v6 = listen_on_v6
        self.lmdb_mapsize = lmdb_mapsize
        self.lock_file = lock_file
        self.managed_keys_directory = managed_keys_directory
        self.masterfile_format = masterfile_format
        self.masterfile_style = masterfile_style
        self.match_mapped_addresses = match_mapped_addresses
        self.max_cache_size = max_cache_size
        self.max_cache_ttl = max_cache_ttl
        self.max_clients_per_query = max_clients_per_query
        self.max_ixfr_ratio = max_ixfr_ratio
        self.max_journal_size = max_journal_size
        self.max_ncache_ttl = max_ncache_ttl
        self.max_records = max_records
        self.max_recursion_depth = max_recursion_depth
        self.max_recursion_queries = max_recursion_queries
        self.max_refresh_time = max_refresh_time
        self.max_retry_time = max_retry_time
        self.max_rsa_exponent_size = max_rsa_exponent_size
        self.max_stale_ttl = max_stale_ttl
        self.max_transfer_idle_in = max_transfer_idle_in
        self.max_transfer_idle_out = max_transfer_idle_out
        self.max_transfer_time_in = max_transfer_time_in
        self.max_transfer_time_out = max_transfer_time_out
        self.max_udp_size = max_udp_size
        self.max_zone_ttl = max_zone_ttl
        self.memstatistics = memstatistics
        self.memstatistics_file = memstatistics_file
        self.message_compression = message_compression
        self.min_cache_ttl = min_cache_ttl
        self.min_ncache_ttl = min_ncache_ttl
        self.min_refresh_time = min_refresh_time
        self.min_retry_time = min_retry_time
        self.minimal_any = minimal_any
        self.minimal_responses = minimal_responses
        self.multi_master = multi_master
        self.new_zones_directory = new_zones_directory
        self.no_case_compress = no_case_compress
        self.nocookie_udp_size = nocookie_udp_size
        self.notify = notify
        self.notify_delay = notify_delay
        self.notify_rate = notify_rate
        self.notify_source = notify_source
        self.notify_source_v6 = notify_source_v6
        self.notify_to_soa = notify_to_soa
        self.nta_lifetime = nta_lifetime
        self.nta_recheck = nta_recheck
        self.nxdomain_redirect = nxdomain_redirect
        self.parental_source = parental_source
        self.parental_source_v6 = parental_source_v6
        self.pid_file = pid_file
        self.port = port
        self.preferred_glue = preferred_glue
        self.prefetch = prefetch
        self.provide_ixfr = provide_ixfr
        self.qname_minimization = qname_minimization
        self.query_source = query_source
        self.query_source_v6 = query_source_v6
        self.querylog = querylog
        self.random_device = random_device
        self.rate_limit = rate_limit
        self.recursing_file = recursing_file
        self.recursion = recursion
        self.recursive_clients = recursive_clients
        self.request_expire = request_expire
        self.request_ixfr = request_ixfr
        self.request_nsid = request_nsid
        self.require_server_cookie = require_server_cookie
        self.reserved_sockets = reserved_sockets
        self.resolver_nonbackoff_tries = resolver_nonbackoff_tries
        self.resolver_query_timeout = resolver_query_timeout
        self.resolver_retry_interval = resolver_retry_interval
        self.response_padding = response_padding
        self.response_policy = response_policy
        self.root_delegation_only = root_delegation_only
        self.root_key_sentinel = root_key_sentinel
        self.rrset_order = rrset_order
        self.secroots_file = secroots_file
        self.send_cookie = send_cookie
        self.serial_query_rate = serial_query_rate
        self.serial_update_method = serial_update_method
        self.server_id = server_id
        self.servfail_ttl = servfail_ttl
        self.session_keyalg = session_keyalg
        self.session_keyfile = session_keyfile
        self.session_keyname = session_keyname
        self.sig_signing_nodes = sig_signing_nodes
        self.sig_signing_signatures = sig_signing_signatures
        self.sig_signing_type = sig_signing_type
        self.sig_validity_interval = sig_validity_interval
        self.sortlist = sortlist
        self.stacksize = stacksize
        self.stale_answer_client_timeout = stale_answer_client_timeout
        self.stale_answer_enable = stale_answer_enable
        self.stale_answer_ttl = stale_answer_ttl
        self.stale_cache_enable = stale_cache_enable
        self.stale_refresh_time = stale_refresh_time
        self.startup_notify_rate = startup_notify_rate
        self.statistics_file = statistics_file
        self.synth_from_dnssec = synth_from_dnssec
        self.tcp_advertised_timeout = tcp_advertised_timeout
        self.tcp_clients = tcp_clients
        self.tcp_idle_timeout = tcp_idle_timeout
        self.tcp_initial_timeout = tcp_initial_timeout
        self.tcp_keepalive_timeout = tcp_keepalive_timeout
        self.tcp_listen_queue = tcp_listen_queue
        self.tcp_receive_buffer = tcp_receive_buffer
        self.tcp_send_buffer = tcp_send_buffer
        self.tkey_dhkey = tkey_dhkey
        self.tkey_domain = tkey_domain
        self.tkey_gssapi_credential = tkey_gssapi_credential
        self.tkey_gssapi_keytab = tkey_gssapi_keytab
        self.tls_port = tls_port
        self.transfer_format = transfer_format
        self.transfer_message_size = transfer_message_size
        self.transfer_source = transfer_source
        self.transfer_source_v6 = transfer_source_v6
        self.transfers_in = transfers_in
        self.transfers_out = transfers_out
        self.transfers_per_ns = transfers_per_ns
        self.trust_anchor_telemetry = trust_anchor_telemetry
        self.try_tcp_refresh = try_tcp_refresh
        self.udp_receive_buffer = udp_receive_buffer
        self.udp_send_buffer = udp_send_buffer
        self.update_check_ksk = update_check_ksk
        self.use_alt_transfer_source = use_alt_transfer_source
        self.use_v4_udp_ports = use_v4_udp_ports
        self.use_v6_udp_ports = use_v6_udp_ports
        self.v6_bias = v6_bias
        self.validate_except = validate_except
        self.version = version
        self.zero_no_soa_ttl = zero_no_soa_ttl
        self.zero_no_soa_ttl_cache = zero_no_soa_ttl_cache
        self.zone_statistics = zone_statistics

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
            if any((key in excluded_attrs, value is None)):
                continue
            elif isinstance(value, bool):
                attrs.append(f'{" " * child_indent}{key} {str(value).lower()};')
            elif isinstance(value, list):
                string_list = [str(item) for item in value]
                value_list = ('{ ' f'{"; ".join(string_list)};' ' }')
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

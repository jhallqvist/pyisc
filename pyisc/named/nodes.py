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


class Acl:
    """Represents an ACL statment."""
    def __init__(self, name: str, acl_elements: List[str] = None) -> None:
        self.name = name
        self.acl_elements = [] if not acl_elements else acl_elements

    def __str__(self) -> str:
        return f'acl {self.name}'

    def __repr__(self) -> str:
        return f'Acl(name={self.name})'

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
        addr_list = []
        for addr in self.acl_elements:
            addr_list.append(f'{" " * child_indent}{addr};')
        return_str = (f'{" " * indent}{self.__str__()}' ' {')
        if len(addr_list) > 0:
            return_str += '\n'
        addr_str = "\n".join(addr_list)
        section_end = '};'
        return (f'{return_str}{addr_str}' '\n' f'{" " * indent}{section_end}')


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
        self.keys = keys
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
    """Represents an INET controls statment."""
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
        self.keys = keys
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
            if all((value, key in ('null', 'stderr'))):
                attrs.append(f'{" " * child_indent}{key};')
            elif all((isinstance(value, bool), key not in ('null', 'stderr'))):
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
    def __init__(self, name: str, channels: List[LogChannel]) -> None:
        self.name = name
        self.channels = channels

    def __str__(self) -> str:
        return f'category {self.name}'

    def __repr__(self) -> str:
        return f'LogCategory(name={self.name}, channels={self.channels})'

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
    def __init__(
        self,
        categories: List[LogCategory],
        channels: List[LogChannel]
    ) -> None:
        self.categories = categories
        self.channels = channels

    def __str__(self) -> str:
        return 'logging'

    def __repr__(self) -> str:
        return f'Logging(categories={self.categories}, channels={self.channels})'

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


class ParentalAgents:
    pass


class Primaries:
    pass


class Options:
    pass


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

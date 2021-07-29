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

from typing import Tuple
from pyisc.dhcpd.nodes import (DhcpClass, Event, EventSet, Group, Hardware,
                               Host, Include, Key, Failover, Option, Pool4,
                               Range4, SubClass, Subnet4, SharedNetwork, Zone)


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
            token (pyisc.dhcpd.parsing.Token): A supplied token instance.

        Returns:
            tuple: Tuple containing value or object in first position
                and method in second position.

        Examples:
            >>> token = Token(type='OPTION',
            ...               value='option domain-name "example.org";',
            ...               line=8, column=0)
            >>> processor = TokenProcessor()
            >>> declaration, method = processor.switch(token)
            >>> declaration
            Option(name="domain_name", value=""example.org"")
            >>> method
            'add_option'

        """
        self.token = token
        default = (None, 'Unknown operation')
        return getattr(self, str(token.type).lower(), lambda: default)()

    def authoritative(self) -> Tuple:
        """Returns tuple for the authoritative command."""
        if 'not' in self.token.value:
            return (False, 'authoritative')
        return (True, 'authoritative')

    def hardware(self) -> Tuple:
        """Returns tuple for the hardware command."""
        _, hardware_type, hardware_address = self.token.value[:-1].split()
        node_hardware = Hardware(type=hardware_type, address=hardware_address)
        return (node_hardware, 'hardware')

    def primary(self) -> Tuple:
        """Returns tuple for the zone primary command."""
        _, primary = self.token.value[:-1].split()
        return (primary, 'primary')

    def failover_role(self) -> Tuple:
        """Returns tuple for the failover role."""
        role = self.token.value[:-1]
        return (role, 'role')

    def include(self) -> Tuple:
        """Returns tuple for the include declaration."""
        _, file_name = self.token.value[:-1].split()
        declaration = Include(filename=file_name)
        return (declaration, 'add_include')

    def general_parameter(self) -> Tuple:
        """Returns tuple for the all other parameters."""
        key, value = self.token.value[:-1].rsplit(' ', 1)
        if value.isdigit():
            value = int(value)
        attr_key = key.replace('-', '_').replace(' ', '_')
        return (value, attr_key)

    def allow_member(self) -> Tuple:
        """Returns tuple for the allow member of statement."""
        _, value = self.token.value[:-1].rsplit(' ', 1)
        return (value, 'add_allowed_member')

    def deny_member(self) -> Tuple:
        """Returns tuple for the deny member of statement."""
        _, value = self.token.value[:-1].rsplit(' ', 1)
        return (value, 'add_denied_member')

    def class_statement(self) -> Tuple:
        """Returns tuple for the match statement of the class declaration."""
        _, statement = self.token.value[:-1].split(' ', 1)
        return (statement, 'match')

    def spawn_class(self) -> Tuple:
        """Returns tuple for the spawn statement of the class declaration."""
        _, statement = self.token.value[:-1].split(' ', 1)
        return (statement, 'spawn')

    # def range4(self) -> Tuple:
    #     """Returns tuple for the range statement for ipv4 configuration."""
    #     if self.token.value.count(' ') == 1:
    #         _, range_start = self.token.value[:-1].split()
    #         range_end = flag = None
    #     elif self.token.value.count(' ') == 2:
    #         _, range_start, range_end = self.token.value[:-1].split()
    #         flag = None
    #     else:
    #         _, flag, range_start, range_end = self.token.value[:-1].split()
    #     subnet_range = Range4(start=range_start, end=range_end, flag=flag)
    #     return (subnet_range, 'add_range')

    def range4(self) -> Tuple:
        """Returns tuple for the range statement for ipv4 configuration."""
        cleaned_token = self.token.value[:-1].strip()
        range_list = [data.strip() for data in cleaned_token.split()]
        if 'dynamic-bootp' in cleaned_token:
            dynamic_bootp = True
            range_list.remove('dynamic-bootp')
        else:
            dynamic_bootp = False
        while len(range_list) < 3:
            range_list += [None]
        _, range_start, range_end = range_list
        subnet_range = Range4(
            start=range_start, end=range_end, dynamic_bootp=dynamic_bootp)
        return (subnet_range, 'add_range')

    def option(self) -> Tuple:
        """Returns tuple for the option command."""
        _, option, value = self.token.value[:-1].split(' ', 2)
        if option.isdigit():
            node_option = Option(number=option, value=value)
        else:
            option = option.replace('-', '_')
            node_option = Option(name=option, value=value)
        return (node_option, 'add_option')

    def key(self) -> Tuple:
        """Returns tuple for the key declaration."""
        _, name = self.token.value[:-1].split()
        if self.token.value[-1] == '{':
            method = 'add_key'
        else:
            method = 'key'
        return (Key(name=name), method)

    def failover(self) -> Tuple:
        """Returns tuple for the failover declaration and parameter."""
        *_, peer = self.token.value[:-1].split()
        return (Failover(name=peer), 'failover')

    def subnet4(self) -> Tuple:
        """Returns tuple for the ipv4 subnet declaration."""
        _, subnet, _, netmask = self.token.value[:-1].split()
        return (Subnet4(network=f'{subnet}/{netmask}'), 'add_subnet')

    def shared_network(self) -> Tuple:
        """Returns tuple for the shared network declaration."""
        _, name = self.token.value[:-1].split()
        return (SharedNetwork(name=name), 'add_shared_network')

    def pool(self) -> Tuple:
        """Returns tuple for the ipv4 pool declaration."""
        return (Pool4(), 'add_pool')

    def group(self) -> Tuple:
        """Returns tuple for the group declaration."""
        return (Group(), 'add_group')

    def host(self) -> Tuple:
        """Returns tuple for the host declaration."""
        _, name = self.token.value[:-1].split()
        return (Host(name=name), 'add_host')

    def dhcp_class(self) -> Tuple:
        """Returns tuple for the class declaration."""
        _, name = self.token.value[:-1].split()
        return (DhcpClass(name=name), 'add_class')

    def subclass(self) -> Tuple:
        """Returns tuple for the class declaration and parameter."""
        cleaned_token = self.token.value[:-1].strip()
        _, name, match_value = cleaned_token.split(' ', 2)
        return (SubClass(name=name, match_value=match_value), 'add_subclass')

    def zone(self) -> Tuple:
        """Returns tuple for the zone declaration."""
        _, name = self.token.value[:-1].split()
        return (Zone(name=name), 'add_zone')

    def event(self) -> Tuple:
        """Returns tuple for the event declaration."""
        _, event_type = self.token.value[:-1].split()
        return (Event(event_type=event_type), 'add_event')

    def event_set(self) -> Tuple:
        """Returns tuple for the event set expression."""
        key, value = [
            data.strip() for data in self.token.value[:-1].split('=')]
        _, attr_key = key.split()
        return (EventSet(key=attr_key, value=value), 'add_event_set')

    def event_log(self) -> Tuple:
        """Returns tuple for the event log directive."""
        value = self.token.value[:-1].replace('log', '')
        return (value, 'log')

    def event_execute(self) -> Tuple:
        """Returns tuple for the event execute directive."""
        value = self.token.value[:-1].replace('execute', '')
        return (value, 'execute')

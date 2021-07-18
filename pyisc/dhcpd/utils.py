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

from pyisc.dhcpd.nodes import Class, Group, Hardware, Host, Include, Key, Failover, Option, Pool4, Range4, SubClass, Subnet4, SharedNetwork, Zone

class TokenProcessor:
    """A processor class for tokens.

    Description here.

    """

    def switch(self, token):
        self.token = token
        default = 'Unknown operation'
        return getattr(self, str(token.type).lower(), lambda: default)()
    def authoritative(self):
        if 'not' in self.token.value:
            return (False, 'authoritative')
        return (True, 'authoritative')
    def failover_parameter(self):
        *_, peer = self.token.value[:-1].split()
        return (Failover(name=peer), 'failover_peer')
    def hardware(self):
        _, hardware_type, hardware_address = self.token.value[:-1].split()
        node_hardware = Hardware(type=hardware_type, address=hardware_address)
        return (node_hardware, 'hardware')
    def primary(self):
        _, primary = self.token.value[:-1].split()
        return (primary, 'primary')
    def key_parameter(self):
        _, key = self.token.value[:-1].split()
        return (Key(name=key), 'key')
    def failover_role(self):
        role = self.token.value[:-1]
        return (role, 'role')
    def include(self):
        _, file_name = self.token.value[:-1].split()
        declaration = Include(filename=file_name)
        return (declaration, 'add_include')
    def general_parameter(self):
        key, value = self.token.value[:-1].rsplit(' ', 1)
        attr_key = key.replace('-', '_').replace(' ', '_')
        return (value, attr_key)
    def allow_member(self):
        _, value = self.token.value[:-1].rsplit(' ', 1)
        return (value, 'add_allowed_member')
    def deny_member(self):
        _, value = self.token.value[:-1].rsplit(' ', 1)
        return (value, 'add_denied_member')
    def class_statement(self):
        _, statement = self.token.value[:-1].split(' ', 1)
        return (statement, 'match')
    def spawn_class(self):
        _, statement =  self.token.value[:-1].split(' ', 1)
        return (statement, 'spawn')
    def range4(self):
        if self.token.value.count(' ') == 1:
            _, range_start = self.token.value[:-1].split()
            subnet_range = Range4(start=range_start)
        elif self.token.value.count(' ') == 2:
            _, range_start, range_end = self.token.value[:-1].split()
            subnet_range = Range4(start=range_start, end=range_end)
        else:
            _, flag, range_start, range_end = self.token.value[:-1].split()
            subnet_range = Range4(start=range_start, end=range_end, flag=flag)
        return (subnet_range, 'add_range')
    def option(self):
        _, option, value = self.token.value[:-1].split(' ', 2)
        if option.isdigit():
            node_option = Option(number=option, value=value)
        else:
            option = option.replace('-', '_')
            node_option = Option(name=option, value=value)
        return (node_option, 'add_option')
    def key(self):
        _, name = self.token.value[:-1].split()
        return (Key(name=name), 'add_key')
    def failover(self):
        *_, peer = self.token.value[:-1].split()
        return (Failover(name=peer), 'failover')
    def subnet4(self):
        _, subnet, _, netmask = self.token.value[:-1].split()
        return (Subnet4(network=f'{subnet}/{netmask}'), 'add_subnet')
    def shared_network(self):
        _, name = self.token.value[:-1].split()
        return (SharedNetwork(name=name), 'add_shared_network')
    def pool(self):
        return (Pool4(), 'add_pool')
    def group(self):
        return (Group(), 'add_group')
    def host(self):
        _, name = self.token.value[:-1].split()
        return (Host(name=name), 'add_host')
    def dhcp_class(self):
        _, name = self.token.value[:-1].split()
        return (Class(name=name), 'add_class')
    def subclass(self):
        _, name, match_value = self.token.value[:-1].split()
        return (SubClass(name=name, match_value=match_value), 'add_subclass')
    def subclass_parameter(self):
        _, name, match_value = self.token.value[:-1].split()
        return (SubClass(name=name, match_value=match_value), 'add_subclass')
    def zone(self):
        _, name = self.token.value[:-1].split()
        return (Zone(name=name), 'add_zone')

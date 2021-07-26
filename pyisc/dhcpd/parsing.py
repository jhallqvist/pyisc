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

from typing import NamedTuple
import re
from pyisc.dhcpd.nodes import Global
from pyisc.dhcpd.utils import TokenProcessor

class Token(NamedTuple):
    """A class to implement tokens for text classification.

    Description here.

    """

    type: str
    value: str
    line: int
    column: int

class DhcpdParser:
    """A parser for ISC DHCPD configs.

    Description here.

    """

    def tokenize(self, content):
        token_specification = [
            ('SHARED_NETWORK',      r'shared-network\s+[^\n]*?{'),          # SCOPE
            ('SUBNET4',             r'subnet\s+[^\n]*?{'),                  # SCOPE
            ('POOL',                r'pool\s+[^\n]*?{'),                    # SCOPE
            ('GROUP',               r'group\s+[^\n]*?{'),                   # SCOPE
            ('HOST',                r'host\s+[^\n]*?{'),                    # SCOPE
            ('SUBCLASS',            r'subclass\s+[^\n]*?{'),                # SCOPE
            ('SUBCLASS_PARAMETER',  r'subclass\s+[^\n]*?;'),                # PARAMETER
            ('FAILOVER',            r'failover\s+[^\n]*?({|;)'),                # SCOPE
            # ('FAILOVER_PARAMETER',  r'failover\s+[^\n]*?;'),                # PARAMETER
            ('DHCP_CLASS',          r'class\s+[^\n]*?{'),                   # SCOPE
            ('SERVER_DUID',         r'server-duid\s+[^\n]*?;'),             # PARAMETER - Not implemented
            ('HARDWARE',            r'hardware\s+[^\n]*?;'),                # PARAMETER
            ('KEY',                 r'key\s+[^\n]*?{'),                     # SCOPE
            ('ZONE',                r'zone\s+[^\n]*?{'),                    # SCOPE
            ('PRIMARY',             r'primary\s+[^\n]*?;'),                 # SCOPE
            ('KEY_PARAMETER',       r'key\s+[^\n]*?;'),                     # PARAMETER
            ('EVENT',               r'on\s+[^\n]*?{'),                      # SCOPE - Not implemented
            ('OPTION',              r'option\s+[^\n=]*?;'),                 # PARAMETER
            ('RANGE4',              r'range\s+[^\n]*?;'),                   # PARAMETER
            ('INCLUDE',             r'include\s+[^\n]*?;'),                 # PARAMETER
            ('FAILOVER_ROLE',       r'(primary|secondary);'),               # PARAMETER
            ('AUTHORITATIVE',       r'(?:not\s+)?authoritative;'),          # PARAMETER
            ('ALLOW_MEMBER',        r'allow\s+member[^\n]*?;'),
            ('DENY_MEMBER',         r'deny\s+member[^\n]*?;'),
            ('CLASS_STATEMENT',     r'match\s+(?:if\s+)?[^\n]*?;'),
            ('SPAWN_CLASS',         r'spawn\s+[^\n]*?;'),
            ('GENERAL_PARAMETER',   r'[\w]+\s*?[^\n]*?;'),                  # GENERAL PARAMETERS
            ('SCOPE_END',           r'}'),
            ('COMMENT_UNIX',        r'\#.*'),                               # COMMENT - Not implemented
            ('NEWLINE',             r'\n'),
            ('SKIP',                r'[ \t]+'),
            ('MISMATCH',            r'.'),                                  # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        line_num = 1
        line_start = 0
        for mo in re.finditer(tok_regex, content):
            kind = mo.lastgroup     # maybe add .lower() here and remove in Processor switch method.
            value = re.sub(r'\s+', ' ', mo.group())
            column = mo.start() - line_start
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
                continue
            # elif kind == 'SKIP':
            #     continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            yield Token(kind, value, line_num, column)

    def construct_tree(self, content):
        isc_declarations = ('KEY', 'SUBNET4', 'SHARED_NETWORK', 'FAILOVER',
                            'POOL', 'GROUP', 'HOST', 'DHCP_CLASS', 'SUBCLASS',
                            'ZONE')
        # parameters = ('AUTHORITATIVE', 'FAILOVER_PARAMETER', 'RANGE4', 'OPTION', 'SUBCLASS_PARAMETER', 'HARDWARE', 'KEY_PARAMETER', 'PRIMARY', 'FAILOVER_ROLE', 'INCLUDE', 'GENERAL_PARAMETER', 'ALLOW_MEMBER', 'DENY_MEMBER', 'CLASS_STATEMENT', 'SPAWN_CLASS')
        node = Global()
        node_stack = []
        processor = TokenProcessor()
        for token in self.tokenize(content):
            if token.type in ('NEWLINE', 'SKIP', 'COMMENT_UNIX'):
                continue
            elif token.type == 'SCOPE_END':
                node = node_stack.pop()
            else:
                # maybe value, attribute instead of declaration, method?
                declaration, method = processor.switch(token)
                if not hasattr(node, method):
                    raise AttributeError(f'{node} attribute {method} does not exist')
                node_method = getattr(node, method)
                if callable(node_method):
                    node_method(declaration)
                else:
                    setattr(node, method, declaration)
                # if token.type in isc_declarations:
                if token.value[-1] == '{':
                    node_stack.append(node)
                    node = declaration
            # elif token.type == 'CLASS_STATEMENT':
            #     _, statement = token.value[:-1].split(' ', 1)
            #     node.match = statement
            # elif token.type == 'SPAWN_CLASS':
            #     _, statement =  token.value[:-1].split(' ', 1)
            #     node.spawn = statement
            # elif token.type == 'ALLOW_MEMBER':
            #     _, value = token.value[:-1].rsplit(' ', 1)
            #     node.add_allowed_member(value)
            # elif token.type == 'DENY_MEMBER':
            #     _, value = token.value[:-1].rsplit(' ', 1)
            #     node.add_denied_member(value)
            # elif token.type == 'OPTION':
            #     _, option, value = token.value[:-1].split(' ', 2)
            #     if option.isdigit():
            #         node_option = Option(number=option, value=value)
            #     else:
            #         option = option.replace('-', '_')
            #         node_option = Option(name=option, value=value)
            #     node.add_option(node_option)
            # elif token.type == 'AUTHORITATIVE':
                # node.authoritative = processor.switch(token)
                # if 'not' in token.value:
                #     node.authoritative = False
                # else:
                #     node.authoritative = True
            # elif token.type == 'PRIMARY':
            #     _, primary = token.value[:-1].split()
            #     node.primary = primary
            # elif token.type == 'KEY_PARAMETER':
            #     _, key = token.value[:-1].split()
            #     node.key = Key(name=key)
            # elif token.type == 'FAILOVER_ROLE':
            #     node.role = token.value[:-1]
            # elif token.type == 'INCLUDE':
            #     _, file_name = token.value[:-1].split()
            #     declaration = Include(filename=file_name)
            #     node.add_include(declaration)
            # elif token.type == 'GENERAL_PARAMETER':
            #     key, value = token.value[:-1].rsplit(' ', 1)
            #     attr_key = key.replace('-', '_').replace(' ', '_')
            #     if hasattr(node, attr_key):
            #         setattr(node, attr_key, value)
            # elif token.type == 'SUBCLASS_PARAMETER':
            #     _, name, match_value = token.value[:-1].split()
            #     subclass = SubClass(name=name, match_value=match_value)
            #     node.add_subclass(subclass)
            # elif token.type == 'HARDWARE':
            #     _, hardware_type, hardware_address = token.value[:-1].split()
            #     node_hardware = Hardware(type=hardware_type, address=hardware_address)
            #     node.hardware = node_hardware
            # elif token.type == 'RANGE4':
            #     if token.value.count(' ') == 1:
            #         _, range_start = token.value[:-1].split()
            #         subnet_range = Range4(start=range_start)
            #     elif token.value.count(' ') == 2:
            #         _, range_start, range_end = token.value[:-1].split()
            #         subnet_range = Range4(start=range_start, end=range_end)
            #     else:
            #         _, flag, range_start, range_end = token.value[:-1].split()
            #         subnet_range = Range4(start=range_start, end=range_end, flag=flag)
            #     node.add_range(subnet_range)
            # -
            # elif token.type in parameters:
            #     # needs to be expanded to allow for methods as well (i.e. add_option)
            #     attribute, value = processor.switch(token)
            #     if hasattr(node, attribute):
            #         setattr(node, attribute, value)
            #     else:
            #         raise AttributeError(f'{node} attribute {method} does not exist')
            # elif token.type in isc_declarations:
            #     declaration, method = processor.switch(token)
            #     if not hasattr(node, method):
            #         raise AttributeError(f'{node} attribute {method} does not exist')
            #     node_method = getattr(node, method)
            #     if callable(node_method):
            #         node_method(declaration)
            #     else:
            #         setattr(node, method, declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'KEY':
            #     _, name = token.value[:-1].split()
            #     declaration = Key(name=name)
            #     node.add_key(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'FAILOVER':
            #     *_, peer = token.value[:-1].split()
            #     declaration = Failover(name=peer)
            #     node.failover = declaration
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'SHARED_NETWORK':
            #     _, name = token.value[:-1].split()
            #     declaration = SharedNetwork(name=name)
            #     node.add_shared_network(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'FAILOVER_PARAMETER':
            #     *_, peer = token.value[:-1].split()
            #     node_failover = Failover(name=peer)
            #     node.failover_peer = node_failover
            # elif token.type == 'POOL':
            #     declaration = Pool4()
            #     node.add_pool(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'GROUP':
            #     declaration = Group()
            #     node.add_group(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'HOST':
            #     _, name = token.value[:-1].split()
            #     declaration = Host(name=name)
            #     node.add_host(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'CLASS':
            #     _, name = token.value[:-1].split()
            #     declaration = Class(name=name)
            #     node.add_class(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'SUBCLASS':
            #     _, name, match_value = token.value[:-1].split()
            #     declaration = SubClass(name=name, match_value=match_value)
            #     node.add_subclass(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # elif token.type == 'ZONE':
            #     _, name = token.value[:-1].split()
            #     declaration = Zone(name=name)
            #     node.add_zone(declaration)
            #     node_stack.append(node)
            #     node = declaration
            # else:
            #     continue
        return node
from typing import NamedTuple
import re
from pyisc.dhcpd.nodes import (Class, Failover, Global, Group, Hardware, Host, Key, Option, Pool4, Range4, SharedNetwork, Subnet4)

class Token(NamedTuple):
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
            ('FAILOVER',            r'failover\s+[^\n]*?{'),                # SCOPE
            ('FAILOVER_PARAMETER',  r'failover\s+[^\n]*?;'),                # PARAMETER
            ('CLASS',               r'class\s+[^\n]*?{'),                   # SCOPE
            ('SERVER_DUID',         r'server-duid\s+[^\n]*?;'),             # PARAMETER
            ('HARDWARE',            r'hardware\s+[^\n]*?;'),                # PARAMETER
            ('ZONE',                r'zone\s+[^\n]*?{'),                    # SCOPE
            ('KEY',                 r'key\s+[^\n]*?{'),                     # SCOPE
            ('EVENT',               r'on\s+[^\n]*?{'),                      # SCOPE
            ('OPTION',              r'option\s+[^\n=]*?;'),                 # PARAMETER
            ('RANGE4',              r'range\s+[^\n]*?;'),                   # PARAMETER
            ('INCLUDE',             r'include\s+[^\n]*?;'),                 # PARAMETER
            ('FAILOVER_ROLE',       r'(primary|secondary);'),               # PARAMETER
            ('BOOLEAN',             r'\w+;'),                               # PARAMETER
            ('ALLOW_MEMBER',        r'allow\s+member[^\n]*?;'),
            ('DENY_MEMBER',         r'deny\s+member[^\n]*?;'),
            ('CLASS_STATEMENT',     r'match\s+(?:if\s+)?[^\n]*?;'),
            ('SPAWN_CLASS',         r'spawn\s+[^\n]*?;'),
            ('GENERAL_PARAMETER',   r'[\w]+\s*?[^\n]*?;'),                  # GENERAL PARAMETERS
            ('SCOPE_END',           r'}'),
            ('COMMENT_UNIX',        r'\#.*'),                               # COMMENT
            ('NEWLINE',             r'\n'),
            ('SKIP',                r'[ \t]+'),
            ('MISMATCH',            r'.'),            # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        line_num = 1
        line_start = 0
        for mo in re.finditer(tok_regex, content):
            kind = mo.lastgroup
            value = re.sub(r'\s+', ' ', mo.group())
            column = mo.start() - line_start
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
                continue
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            yield Token(kind, value, line_num, column)

    def build_tree(self, content):
        node = Global()
        node_stack = []
        for token in self.tokenize(content):
            if token.type in ('NEWLINE', 'SKIP'):
                continue
            elif token.type == 'SCOPE_END':
                node = node_stack.pop()
            elif token.type == 'OPTION':
                _, option, value = token.value[:-1].split(' ', 2)
                if option.isdigit():
                    node_option = Option(number=option, value=value)
                else:
                    node_option = Option(name=option, value=value)
                node.add_option(node_option)
            elif token.type == 'FAILOVER_ROLE':
                node.role = token.value[:-1]
            elif token.type == 'GENERAL_PARAMETER':
                key, value = token.value[:-1].rsplit(' ', 1)
                attr_key = key.replace('-', '_').replace(' ', '_')
                if hasattr(node, attr_key):
                    setattr(node, attr_key, value)
            elif token.type == 'ALLOW_MEMBER':
                _, value = token.value[:-1].rsplit(' ', 1)
                node.add_allowed_member(value)
            elif token.type == 'DENY_MEMBER':
                _, value = token.value[:-1].rsplit(' ', 1)
                node.add_denied_member(value)
            elif token.type == 'HARDWARE':
                _, hardware_type, hardware_address = token.value[:-1].split()
                node_hardware = Hardware(type=hardware_type, address=hardware_address)
                node.hardware = node_hardware
            elif token.type == 'CLASS_STATEMENT':
                _, statement = token.value[:-1].split(' ', 1)
                node.match = statement
            elif token.type == 'SPAWN_CLASS':
                _, statement =  token.value[:-1].split(' ', 1)
                node.spawn = statement
            elif token.type == 'RANGE4':
                if token.value.count(' ') == 1:
                    _, range_start = token.value[:-1].split()
                    subnet_range = Range4(start=range_start)
                elif token.value.count(' ') == 2:
                    _, range_start, range_end = token.value[:-1].split()
                    subnet_range = Range4(start=range_start, end=range_end)
                else:
                    _, flag, range_start, range_end = token.value[:-1].split()
                    subnet_range = Range4(start=range_start, end=range_end, flag=flag)
                node.add_range(subnet_range)
            elif token.type == 'KEY':
                _, name = token.value[:-1].split()
                declaration = Key(name=name)
                node.add_key(declaration)
                node_stack.append(node)
                node = declaration
            elif token.type == 'FAILOVER':
                *_, peer = token.value[:-1].split()
                declaration = Failover(name=peer)
                node.failover = declaration
                node_stack.append(node)
                node = declaration
            elif token.type == 'SUBNET4':
                _, subnet, _, netmask = token.value[:-1].split()
                declaration = Subnet4(network=f'{subnet}/{netmask}')
                node.add_subnet(declaration)
                node_stack.append(node)
                node = declaration
            elif token.type == 'SHARED_NETWORK':
                _, name = token.value[:-1].split()
                declaration = SharedNetwork(name=name)
                node.add_shared_network(declaration)
                node_stack.append(node)
                node = declaration
            elif token.type == 'FAILOVER_PARAMETER':
                *_, peer = token.value[:-1].split()
                node_failover = Failover(name=peer)
                node.failover_peer = node_failover
            elif token.type == 'POOL':
                declaration = Pool4()
                node.add_pool(declaration)
                node_stack.append(node)
                node = declaration
            elif token.type == 'GROUP':
                declaration = Group()
                node.add_group(declaration)
                node_stack.append(node)
                node = declaration
            elif token.type == 'HOST':
                _, name = token.value[:-1].split()
                declaration = Host(name=name)
                node.add_host(declaration)
                node_stack.append(node)
                node = declaration
            elif token.type == 'CLASS':
                _, name = token.value[:-1].split()
                declaration = Class(name=name)
                node.add_class(declaration)
                node_stack.append(node)
                node = declaration
            else:
                continue
        return node
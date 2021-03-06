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

from typing import Generator, NamedTuple
import re
from pyisc.dhcpd.nodes import Global
from pyisc.dhcpd.utils import TokenProcessor


class Token(NamedTuple):
    """A class to implement tokens for text classification."""

    type: str
    value: str
    line: int
    column: int


class DhcpdParser:
    """A parser for ISC DHCPD configs.

    This class contains methods for making tokens out of text as
    well as building a object tree of the generated tokens.
    Instantiate the class and use of of the methods with a string from
    a valid ISC DHCPD configuration file.

    """

    def tokenize(self, content: str) -> Generator:
        """
        Return a generator of token objects.

        Args:
            content (str): A supplied string to turn into tokens.

        Returns:
            generator: A generator containing the tokens.

        Examples:
            >>> isc_string = 'option domain-name "example.org";'
            <generator object DhcpdParser.tokenize at ...>
            >>> for token in parser.tokenize(isc_string):
            ...     token
            Token(type='OPTION', value='option domain-name "example.org";',
            line=1, column=0)

        """
        token_specification = [
            ('SHARED_NETWORK',      r'shared-network\s+[^\n]*?{'),
            ('SUBNET4',             r'subnet\s+[^\n]*?{'),
            ('SUBNET6',             r'subnet6\s+[^\n]*?{'),
            ('POOL',                r'pool\s+[^\n]*?{'),
            ('GROUP',               r'group\s+[^\n]*?{'),
            ('HOST',                r'host\s+[^\n]*?{'),
            ('SUBCLASS',            r'subclass\s+[^\n]*?({|;)'),
            ('FAILOVER',            r'failover\s+[^\n]*?({|;)'),
            ('DHCP_CLASS',          r'class\s+[^\n]*?{'),
            ('SERVER_DUID_LL',      r'server-duid\s+LL[^\n]*?;'),
            ('SERVER_DUID_EN',      r'server-duid\s+[^\n]*?;'),
            ('HARDWARE',            r'hardware\s+[^\n]*?;'),
            ('KEY',                 r'key\s+[^\n]*?({|;)'),
            ('ZONE',                r'zone\s+[^\n]*?{'),
            ('PRIMARY',             r'primary\s+[^\n]*?;'),
            ('EVENT',               r'on\s+[^\n]*?{'),
            ('EVENT_SET',           r'set\s+[^\n]*?=[^\n]*?;'),
            ('EVENT_LOG',           r'log\([^\n]*?[^\n]*?;'),
            ('EVENT_EXECUTE',       r'execute\([^\n]*?[^\n]*?;'),
            ('OPTION',              r'option\s+[^\n=]*?;'),
            ('RANGE4',              r'range\s+[^\n]*?;'),
            ('RANGE6',              r'range6\s+[^\n]*?;'),
            ('PREFIX6',             r'prefix6\s+[^\n]*?;'),
            ('INCLUDE',             r'include\s+[^\n]*?;'),
            ('FAILOVER_ROLE',       r'(primary|secondary);'),
            ('AUTHORITATIVE',       r'(?:not\s+)?authoritative;'),
            ('ALLOW_MEMBER',        r'allow\s+member[^\n]*?;'),
            ('DENY_MEMBER',         r'deny\s+member[^\n]*?;'),
            ('IGNORE_GENERAL',      r'ignore[^\n]*?;'),
            ('ALLOW_GENERAL',       r'allow[^\n]*?;'),
            ('DENY_GENERAL',        r'deny[^\n]*?;'),
            ('CLASS_STATEMENT',     r'match\s+(?:if\s+)?[^\n]*?;'),
            ('SPAWN_CLASS',         r'spawn\s+[^\n]*?;'),
            ('CUSTOM_OPTION',       r'option\s+[^\n]*?code\s+\d+\s+=[^\n]*?;'),
            ('OPTION_EXPRESSION',   r'option\s+[^\n]*?=[^\n]*?;'),
            ('GENERAL_PARAMETER',   r'[\w]+\s*?[^\n]*?;'),
            ('SCOPE_END',           r'}'),
            ('COMMENT_UNIX',        r'\#.*'),
            ('NEWLINE',             r'\n'),
            ('WHITESPACE',          r'[ \t]+'),
            ('MISMATCH',            r'.'),
        ]
        tok_regex = '|'.join(
            '(?P<%s>%s)' % pair for pair in token_specification)
        line_num = 1
        line_start = 0
        for mo in re.finditer(tok_regex, content):
            kind = mo.lastgroup
            value = re.sub(r'\s+', ' ', mo.group())
            column = mo.start() - line_start
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            yield Token(kind, value, line_num, column)

    def construct_tree(self, content: str) -> Global:
        """
        Return an object tree of supplied string.

        Args:
            content (str): A supplied string to turn into tokens.

        Returns:
            Global: An object tree with the root of Global.

        Examples:
            >>> parser = DhcpdParser()
            >>> with open('dhcpd1.conf','r') as infile:
            ...     conf = infile.read()
            >>> object_tree = parser.construct_tree(conf)

        """
        node = Global()
        node_stack = []
        processor = TokenProcessor()
        for token in self.tokenize(content):
            if token.type in ('NEWLINE', 'WHITESPACE', 'COMMENT_UNIX'):
                continue
            elif token.type == 'SCOPE_END':
                node = node_stack.pop()
            else:
                # maybe value, attribute instead of declaration, method?
                declaration, method = processor.switch(token)
                if not hasattr(node, method):
                    raise AttributeError(
                        f'{node} attribute {method} does not exist')
                node_method = getattr(node, method)
                if callable(node_method):
                    node_method(declaration)
                else:
                    setattr(node, method, declaration)
                if token.value[-1] == '{':
                    node_stack.append(node)
                    node = declaration
        return node

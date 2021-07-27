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

    This class parses contains methods for making tokens out of text as
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
            Token(type='OPTION', value='option domain-name "example.org";', line=1, column=0)

        """
        token_specification = [
            ('SHARED_NETWORK',      r'shared-network\s+[^\n]*?{'),          # SCOPE
            ('SUBNET4',             r'subnet\s+[^\n]*?{'),                  # SCOPE
            ('POOL',                r'pool\s+[^\n]*?{'),                    # SCOPE
            ('GROUP',               r'group\s+[^\n]*?{'),                   # SCOPE
            ('HOST',                r'host\s+[^\n]*?{'),                    # SCOPE
            ('SUBCLASS',            r'subclass\s+[^\n]*?({|;)'),                # SCOPE
            ('FAILOVER',            r'failover\s+[^\n]*?({|;)'),                # SCOPE
            ('DHCP_CLASS',          r'class\s+[^\n]*?{'),                   # SCOPE
            ('SERVER_DUID',         r'server-duid\s+[^\n]*?;'),             # PARAMETER - Not implemented
            ('HARDWARE',            r'hardware\s+[^\n]*?;'),                # PARAMETER
            ('KEY',                 r'key\s+[^\n]*?({|;)'),                     # SCOPE
            ('ZONE',                r'zone\s+[^\n]*?{'),                    # SCOPE
            ('PRIMARY',             r'primary\s+[^\n]*?;'),                 # SCOPE
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
            ('WHITESPACE',          r'[ \t]+'),
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
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            yield Token(kind, value, line_num, column)

    def construct_tree(self, content:str) -> Global:
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
                    raise AttributeError(f'{node} attribute {method} does not exist')
                node_method = getattr(node, method)
                if callable(node_method):
                    node_method(declaration)
                else:
                    setattr(node, method, declaration)
                if token.value[-1] == '{':
                    node_stack.append(node)
                    node = declaration
        return node
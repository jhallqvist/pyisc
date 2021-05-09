"""Contains the parser for DHCPd configuration files/strings."""

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

import re
from pyisc.dhcpd.nodes import Token, Node, PropertyNode, RootNode
from pyisc.dhcpd.utils import TokenSplitter


class DhcpdParser:
    """A parser for ISC DHCPD configs.

    The constants are the various RegEx patterns that is used in the tokens
    variable. Token variable is a list of tuples that conains previously
    mentioned RegEx patterns as well as lambda functions that are meant to be
    used by the re.Scanner in tokenize function.

    """

    DECLARATION_FAILOVER = r"(?:failover\s)[\w]+\s*?[^\n]*?{"
    DECLARATION_GENERAL = r"[\w]+\s*?[^\n]*?{"
    PARAMETER_SINGLE_KEY = r"""(?:(?:allow|deny|ignore|match|spawn|range|
                            fixed-address|fixed-prefix6)\s)[\w]+\s*?[^\n]*?;"""
    PARAMETER_MULTI_VALUE = r"(?:server-duid\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_SINGLE_VALUE = r"""(?:(?:hardware|host-identifier|load|lease|
                               peer|my state|peer state)\s)[\w]+\s*?[^\n]*?;"""
    PARAMETER_OPTION = r"(?:option\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_FAILOVER = r"(?:failover\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_GENERAL = r"[\w]+\s*?[^\n]*?;"
    NEWLINE = r"\n"
    WHITESPACE = r"\s"
    COMMENT = r"\#.*?\n"
    SECTION_END = r"\}"

    tokens = [
        (DECLARATION_FAILOVER, lambda scanner, token: Token(
            type='declaration_failover', value=token)),
        (DECLARATION_GENERAL, lambda scanner, token: Token(
            type='declaration_general', value=token)),
        (PARAMETER_SINGLE_KEY, lambda scanner, token: Token(
            type='parameter_single_key', value=token)),
        (PARAMETER_MULTI_VALUE, lambda scanner, token: Token(
            type='parameter_multiple_values', value=token)),
        (PARAMETER_SINGLE_VALUE, lambda scanner, token: Token(
            type='parameter_single_value', value=token)),
        (PARAMETER_OPTION, lambda scanner, token: Token(
            type='parameter_option', value=token)),
        (PARAMETER_FAILOVER, lambda scanner, token: Token(
            type='parameter_failover', value=token)),
        (PARAMETER_GENERAL, lambda scanner, token: Token(
            type='parameter_general', value=token)),
        (NEWLINE, lambda scanner, token: Token(
            type='newline', value=token)),
        (WHITESPACE, lambda scanner, token: Token(
            type='whitespace', value=token)),
        (COMMENT, lambda scanner, token: Token(
            type='comment', value=token)),
        (SECTION_END, lambda scanner, token: Token(
            type='section_end', value=token)),
    ]

    def tokenize(self, content):
        """
        Return list of token objects.

        Args:
            content (str): A supplied string to turn into tokens.

        Returns:
            list[Token]: A list of Token instances

        Examples: 
            >>> isc_string = 'option domain-name "example.org";'
            >>> parser = dhcpd.DhcpdParser()
            >>> parser.tokenize(isc_string)
            [Token(type='parameter_option', value='option domain-name "example.org";')]

        """ # noqa
        scanner = re.Scanner(self.tokens, flags=re.DOTALL | re.VERBOSE)
        tokens, remainder = scanner.scan(content)
        if remainder:
            raise Exception(f'Invalid tokens: {remainder}, Tokens: {tokens}')
        return tokens

    def build_tree(self, content):
        """
        Return a tree like structure of token objects.

        Args:
            content (str): A supplied string to supply to the tokenize method.

        Returns:
            pyisc.dhcpd.RootNode: A tree like representation of the supplied string.

        Examples:
            >>> isc_string = 'option domain-name "example.org";'
            >>> parser = dhcpd.DhcpdParser()
            >>> parser.build_tree(isc_string)
            RootNode(Root)

        """ # noqa
        node = RootNode()
        node_stack = []
        splitter = TokenSplitter()
        next_comment = None
        for token in self.tokenize(content):
            if token.type in ['whitespace', 'newline']:
                continue
            if token.type == 'section_end':
                node = node_stack.pop()
            if token.type == 'comment':
                continue
            if token.type.startswith('parameter'):
                key, value, parameters, *_ = splitter.switch(token)
                prop = PropertyNode(
                    type=key, value=value, parameters=parameters)
                node.children.append(prop)
            if token.type.startswith('declaration'):
                key, value, parameters, *_ = splitter.switch(token)
                section = Node(type=key, value=value, parameters=parameters)
                node.children.append(section)
                node_stack += [node]
                node = section
        return node

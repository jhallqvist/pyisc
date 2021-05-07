"""Contains the parser for DHCPd configuration files/strings."""

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

    FAILOVER_START = r"(?:failover\s)[\w]+\s*?[^\n]*?{"
    BLOCK_START = r"[\w]+\s*?[^\n]*?{"
    PARAMETER_SINGLE_KEY = r"""(?:(?:allow|deny|ignore|match|spawn|range|
                            fixed-address|fixed-prefix6)\s)[\w]+\s*?[^\n]*?;"""
    PARAMETER_MULTI_VALUE = r"(?:server-duid\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_SINGLE_VALUE = r"""(?:(?:hardware|host-identifier|load|lease|
                               peer|my state|peer state)\s)[\w]+\s*?[^\n]*?;"""
    PARAMETER_OPTION = r"(?:option\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_GENERAL = r"[\w]+\s*?[^\n]*?;"
    NEWLINE = r"\n"
    WHITESPACE = r"\s"
    COMMENT = r"\#.*?\n"
    SECTION_END = r"\}"

    tokens = [
        (FAILOVER_START, lambda scanner, token: Token(
            type='failover_start', value=token)),
        (BLOCK_START, lambda scanner, token: Token(
            type='section_start', value=token)),
        (PARAMETER_SINGLE_KEY, lambda scanner, token: Token(
            type='parameter_single_key', value=token)),
        (PARAMETER_MULTI_VALUE, lambda scanner, token: Token(
            type='parameter_multiple_values', value=token)),
        (PARAMETER_SINGLE_VALUE, lambda scanner, token: Token(
            type='parameter_single_value', value=token)),
        (PARAMETER_OPTION, lambda scanner, token: Token(
            type='parameter_option', value=token)),
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

        """
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

        """
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
            if token.type == 'section_start' or token.type == 'failover_start':
                # Need to break out failover and split in correct way.
                # Also need to alter TokenSplitter for failover as a parameter.
                token, name, parameters, *_ = token.value[:-1].strip().split(
                    None, 2) + [None, None]
                section = Node(type=token, value=name, parameters=parameters)
                node.children.append(section)
                node_stack += [node]
                node = section
        return node

"""TEMP."""

import re
from .nodes import Token, Node, PropertyNode, RootNode
from .utils import TokenSplitter


class DhcpParser:
    """A parser for ISC configs."""

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
        (FAILOVER_START, lambda scanner, token: Token(type='failover_start', value=token)),
        (BLOCK_START, lambda scanner, token: Token(type='section_start', value=token)),
        (PARAMETER_SINGLE_KEY, lambda scanner, token: Token(type='parameter_single_key', value=token)),
        (PARAMETER_MULTI_VALUE, lambda scanner, token: Token(type='parameter_multiple_values', value=token)),
        (PARAMETER_SINGLE_VALUE, lambda scanner, token: Token(type='parameter_single_value', value=token)),
        (PARAMETER_OPTION, lambda scanner, token: Token(type='parameter_option', value=token)),
        (PARAMETER_GENERAL, lambda scanner, token: Token(type='parameter_general', value=token)),
        (NEWLINE, lambda scanner, token: Token(type='newline', value=token)),
        (WHITESPACE, lambda scanner, token: Token(type='whitespace', value=token)),
        (COMMENT, lambda scanner, token: Token(type='comment', value=token)),
        (SECTION_END, lambda scanner, token: Token(type='section_end', value=token)),
    ]

    def tokenize(self, content):
        """
        Return list of token objects.

        :param content: A supplied string.
        :type token: str
        :return: Returns a list of Token objects parsed from submitted string.
        :rtype: list
        """
        scanner = re.Scanner(self.tokens, flags=re.DOTALL | re.VERBOSE)
        tokens, remainder = scanner.scan(content)
        if remainder:
            raise Exception(f'Invalid tokens: {remainder}, Tokens: {tokens}')
        return tokens

    def build_tree(self, content):
        """
        Return a tree like structure of token objects.

        :param content: A supplied string.
        :type token: str
        :return: Returns a tree representation of pyisc.RootNode, pyisc.Node
            and pyisc PropertyNode objects.
        :rtype: list
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
                    name=key, value=value, parameters=parameters)
                node.children.append(prop)
            if token.type == 'section_start' or token.type == 'failover_start':
                # Need to break out failover and split in correct way.
                # Also need to alter TokenSplitter for failover as a parameter.
                token, name, parameters, *_ = token.value[:-1].strip().split(None, 2) + [None, None]
                section = Node(type=token, name=name, parameters=parameters)
                node.children.append(section)
                node_stack += [node]
                node = section
        return node

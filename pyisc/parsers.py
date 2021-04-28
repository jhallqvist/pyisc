"""TEMP."""

import re
from .nodes import Token, Node, PropertyNode, RootNode
from .utils import nth_split


class IscParser():
    """A parser for ISC configs."""

    tokens = [
        (r"[\w_]+\s*?[^\n]*?{", lambda scanner, token: Token(type='section_start', value=token)),
        (r"[\w_]+?(?:[^\"]+?(?:\".*?\")?)+?;", lambda scanner, token: Token(type='option', value=token)),
        (r"\n", lambda scanner, token: Token(type='newline', value=token)),
        (r"\s", lambda scanner, token: Token(type='whitespace', value=token)),
        (r"\#.*?\n", lambda scanner, token: Token(type='comment', value=token)),
        (r"\}", lambda scanner, token: Token(type='section_end', value=token)),
    ]

    def tokenize(self, content):
        """TEMP."""
        scanner = re.Scanner(self.tokens, re.DOTALL)
        tokens, remainder = scanner.scan(content)
        if remainder:
            raise Exception(f'Invalid tokens: {remainder}, Tokens: {tokens}')
        return tokens

    def build_tree(self, content):
        """TEMP."""
        node = RootNode()
        node_stack = []
        next_comment = None
        for token in self.tokenize(content):
            if token.type in ['whitespace', 'newline']:
                continue
            if token.type == 'section_end':
                node = node_stack.pop()
            if token.type == 'comment':
                continue
            if token.type == 'option':
                if token.value.startswith('option'):
                    key, value = nth_split(token.value[:-1], ' ', 2)
                else:
                    key, value, *_ = token.value[:-1].split(None, 1) + [None]
                prop = PropertyNode(name=key, value=value)
                node.children.append(prop)
            if token.type == 'section_start':
                token, name, parameters, *_ = token.value[:-1].strip().split(None, 2) + [None, None]
                section = Node(type=token, name=name, parameters=parameters)
                node.children.append(section)
                node_stack += [node]
                node = section
        return node

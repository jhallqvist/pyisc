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

"""Contains the base parsing components for use in the various submodules."""

from pyisc.shared.parsing import BaseParser, Token
from pyisc.shared.nodes import RootNode, Node, PropertyNode
from pyisc.dhcpd.utils import DhcpdSplitter


class DhcpdParser(BaseParser):
    """A parser for ISC DHCPD configs.

    The constants are the various RegEx patterns that is used in the
    tokens variable. Token variable is a list of tuples that contains
    previously mentioned RegEx patterns as well as lambda functions
    that are meant to be used by the re.Scanner in tokenize function.

    """
    DECLARATION_FAILOVER = r"(?:failover\s)[\w]+\s*?[^\n]*?{"
    DECLARATION_GENERAL = r"[\w]+\s*?[^\n=]*?{"
    EVENTS_GENERAL = r"(?:set|execute|log)[\w\s(]+\s*?[^\n]*?;"
    PARAMETER_BOOLEAN = r"(?:not\s)?(?:authoritative);"
    PARAMETER_SINGLE_KEY = r"""(?:(?:allow|deny|ignore|match|spawn|
                            range6?(?!.*temporary)|fixed-address6?|
                            fixed-prefix6|prefix6|dynamic-bootp
                            -lease-cutoff)\s)[\w]+\s*?[^\n]*?;"""
    FORMULA_GENERAL = r"(?:option|v6relay)[^\n=]*?=[^\n]*?;"
    # PARAMETER_MULTI_VALUE = r"(?:server-duid\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_SINGLE_VALUE = r"""(?:(?:hardware|host-identifier|load|lease|
                              peer|my\sstate)\s)[\w]+\s*?[^\n]*?;"""
    PARAMETER_OPTION = r"(?:(?:option|server-duid)\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_FAILOVER = r"(?:failover\s)[\w]+\s*?[^\n]*?;"
    PARAMETER_GENERAL = r"[\w]+\s*?[^\n]*?;"
    SECTION_END = r"\}"

    tokens = [
        (DECLARATION_FAILOVER, lambda scanner, token: Token(
            type='declaration_failover', value=token)),
        (DECLARATION_GENERAL, lambda scanner, token: Token(
            type='declaration_general', value=token)),
        (EVENTS_GENERAL, lambda scanner, token: Token(
            type='event_general', value=token)),
        (FORMULA_GENERAL, lambda scanner, token: Token(
            type='formula_general', value=token)),
        (PARAMETER_BOOLEAN, lambda scanner, token: Token(
            type='parameter_boolean', value=token)),
        (PARAMETER_SINGLE_KEY, lambda scanner, token: Token(
            type='parameter_single_key', value=token)),
        # (PARAMETER_MULTI_VALUE, lambda scanner, token: Token(
        #     type='parameter_multiple_values', value=token)),
        (PARAMETER_SINGLE_VALUE, lambda scanner, token: Token(
            type='parameter_single_value', value=token)),
        (PARAMETER_OPTION, lambda scanner, token: Token(
            type='parameter_option', value=token)),
        (PARAMETER_FAILOVER, lambda scanner, token: Token(
            type='parameter_failover', value=token)),
        (PARAMETER_GENERAL, lambda scanner, token: Token(
            type='parameter_general', value=token)),
        (SECTION_END, lambda scanner, token: Token(
            type='section_end', value=token)),
    ] + BaseParser.tokens

    def build_tree(self, content):
        """
        Return a tree like structure of token objects.

        Args:
            content (str): A supplied string to supply to the tokenize
                method.

        Returns:
            pyisc.shared.nodes.RootNode: A tree like representation of the
                supplied string.

        Examples:
            >>> isc_string = 'option domain-name "example.org";'
            >>> parser = dhcpd.DhcpdParser()
            >>> parser.build_tree(isc_string)
            RootNode(Root)

        """
        node = RootNode()
        node_stack = []
        splitter = DhcpdSplitter()
        next_comment = None
        for token in self.tokenize(content):
            if token.type in ['whitespace', 'newline']:
                continue
            if token.type == 'section_end':
                node = node_stack.pop()
            if token.type.startswith('comment'):
                if not next_comment:
                    next_comment = ''
                else:
                    next_comment += '\n'
                next_comment += token.value.strip()
            if token.type.startswith('event'):
                key, value, parameters, *_ = splitter.switch(token)
                prop = PropertyNode(
                    type=key, value=value, parameters=parameters)
                node.children.append(prop)
            if token.type.startswith('formula'):
                key, value, parameters, *_ = splitter.switch(token)
                prop = PropertyNode(
                    type=key, value=value, parameters=parameters)
                node.children.append(prop)
            if token.type.startswith('parameter'):
                key, value, parameters, *_ = splitter.switch(token)
                prop = PropertyNode(
                    type=key, value=value, parameters=parameters)
                prop.comment = next_comment
                next_comment = None
                node.children.append(prop)
            if token.type.startswith('declaration'):
                key, value, parameters, *_ = splitter.switch(token)
                section = Node(type=key, value=value, parameters=parameters)
                section.comment = next_comment
                next_comment = None
                node.children.append(section)
                node_stack += [node]
                node = section
        return node

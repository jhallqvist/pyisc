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

import re
from collections import namedtuple


class BaseParser:
    """A base parser for ISC parsers.

    The constants are the various RegEx patterns that is used in the
    tokens variable. Token variable is a list of tuples that conains
    previously mentioned RegEx patterns as well as lambda functions
    that are meant to be used by the re.Scanner in tokenize function.

    """
    NEWLINE = r"\n"
    WHITESPACE = r"\s"
    COMMENT_UNIX = r"\#.*?\n"

    tokens = [
        (NEWLINE, lambda scanner, token: Token(
            type='newline', value=token)),
        (WHITESPACE, lambda scanner, token: Token(
            type='whitespace', value=token)),
        (COMMENT_UNIX, lambda scanner, token: Token(
            type='comment', value=token))
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
            [Token(type='parameter_option', value='option domain-name "example.org";')]

        """
        scanner = re.Scanner(self.tokens, flags=re.DOTALL | re.VERBOSE)
        tokens, remainder = scanner.scan(content)
        if remainder:
            raise Exception(f'Invalid tokens: {remainder}, Tokens: {tokens}')
        return tokens


Token = namedtuple('Token', ['type', 'value'])

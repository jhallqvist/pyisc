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
from pyisc.zone.nodes import Zone
from pyisc.zone.utils import (TokenProcessor, partition_string, rr_split,
                              standardize_rr)


class Token(NamedTuple):
    """A class to implement tokens for text classification."""

    type: str
    value: str
    line: int
    column: int


class ZoneParser:
    """A parser for ISC Zone files.

    This class contains methods for making tokens out of text as
    well as building a object tree of the generated tokens.
    Instantiate the class and use of of the methods with a string from
    a valid ISC Zone file.

    """

    def tokenize(self, content: str) -> Generator:
        """
        Return a generator of token objects.

        Args:
            content (str): A supplied string to turn into tokens.

        Returns:
            generator: A generator containing the tokens.

        Examples:
            >>> pass

        """
        content_list = partition_string(content)
        directives = ('$ORIGIN', '$INCLUDE', '$TTL', '$GENERATE')

        for row in content_list:
            line_no, line, char_pos = row

            if line.startswith(directives):
                token_type = line.split()[0][1:].upper()
            elif line.startswith(';'):
                token_type = 'COMMENT'
            else:
                rr_list = rr_split(line)
                sanitized_record = standardize_rr(rr_list)
                token_type = sanitized_record[3].upper()
            token = Token(token_type, line, line_no, char_pos)
            yield token

    def construct_tree(self, content: str) -> Zone:
        """
        Return an object tree of supplied string.

        Args:
            content (str): A supplied string to turn into tokens.

        Returns:
            Zone: An object tree with the root of Zone.

        Examples:
            >>> pass

        """
        node = Zone()
        processor = TokenProcessor()
        for token in self.tokenize(content):
            if token.type in ('COMMENT'):
                continue
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
        return node

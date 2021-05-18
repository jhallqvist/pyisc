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

"""General helper functions and classes for the module."""

from pyisc.shared.utils import TokenSplitter, split_at, split_from


class DhcpdSplitter(TokenSplitter):
    def parameter_option(self):
        """Return a list of an option string.

        Expects a string where the the first two words are to be
        considered the key and everything after that is the value,
        whether that is a single word or multiple words (usually
        separated by a comma)

        """
        return split_at(self.token.value[:-1], ' ', 2)

    def parameter_single_value(self):
        """Return a list where the last word in the string is the value.

        Expects a string where the last word or number is the value and
        everything up until that is to be considered the key.

        """
        return self.token.value[:-1].rsplit(None, 1)

    def parameter_multiple_values(self):
        """Return a list where the parameter contains space.

        Expects a string where the the first two words make up the key
        and value and everything after that is considered the parameter
        of the future Token instance.

        """
        return self.token.value[:-1].split(None, 2)

    def parameter_single_key(self):
        """Return a list where the first word in the string is the key.

        Expects a string where the first word in the string is the key
        and everything after that is the value.

        """
        return self.token.value[:-1].split(None, 1)

    def parameter_failover(self):
        """Return a list from a failover parameter string.

        Expects a string that starts with failover and ends with a
        semicolon.

        """
        return split_from(self.token.value[:-1], ' ', 2)

    def parameter_general(self):
        """Return a list from a general parameter string.

        Splits any parameter string that is not processesed by a more
        specific match from the parser.

        """
        return self.token.value[:-1].split()

    def declaration_failover(self):
        """Return a list from a failover declaration string.

        Expects a string that starts with failover and ends with a
        left curly bracket.

        """
        return split_from(self.token.value[:-2], ' ', 2)

    def declaration_general(self):
        """Return a list from a general declaration string.

        Splits any declaration string that is not processesed by a more
        specific match from the parser.

        """
        return self.token.value[:-1].strip().split(None, 2)

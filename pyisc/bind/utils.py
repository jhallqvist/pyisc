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

from pyisc.shared.utils import TokenSplitter


class BindSplitter(TokenSplitter):
    def parameter_general(self):
        """Return a list from a general parameter string.

        Splits any parameter string that is not processesed by a more
        specific match from the parser.

        """
        return self.token.value[:-1].split()

    def declaration_general(self):
        """Return a list from a general declaration string.

        Splits any declaration string that is not processesed by a more
        specific match from the parser.

        """
        return self.token.value[:-1].strip().split(None, 2)

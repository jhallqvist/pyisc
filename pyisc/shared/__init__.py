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

"""Shared components for both DHCPd and Bind.

All components found in this sub-module, although maybe possible, are not meant
to utilize directly. They are to serve as a common base for the other
sub-modules to reduce duplication in the code.

"""

__version__ = '1.0'
__author__ = 'Jonas Hallqvist'

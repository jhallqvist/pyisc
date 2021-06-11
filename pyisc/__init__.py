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

"""PyISC enables the manipulation of ISC configuration files.

The library is divided into submodules where each submodule is
responsible for the parsing and editing of that specific type of file.
So for ISC DHCPds configuration file the submodule dhcpd is used and
for Bind9s named.conf file the bind subpackage is used.

"""

__all__ = ['dhcpd', 'bind']
__version__ = '0.3.1'
__author__ = 'Jonas Hallqvist'

from pyisc import dhcpd, bind

"""PyISC enables the manipulation of ISC configuration files.

The library is divided into submodules where each submodule is responsible for
the parsing and editing of that specific type of file.
So for ISC DHCPds configuration file the submodule dhcpd is used and for Bind9s
named.conf file the bind subpackage is used.

"""

__all__ = ['dhcpd']

from pyisc import dhcpd

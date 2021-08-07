# PyISC

A python library with the purpose of parsing and manipulating ISC configuration files. Currently only focused on the dhcpd.conf file but will be expanded in the future.

## Scope of project

The aim of this project it to provide a working ORM for ISC configuration files so that one may use existing, as well as new, files and transform them to a easy to use python data structure.

It is not in scope to provide validation of provided data when supplying new data to a parsed configuration file.

## Installation

Currently a git clone is necessary as the package on PyPi is not yet updated.

## Usage

```python
>>> from pyisc import dhcpd

>>> test = '''shared-network 224-29 {
    subnet 10.0.29.0 netmask 255.255.255.0 {
        option routers rtr-29.example.org;
    }
    subnet 10.17.224.0 netmask 255.255.255.0 {
        option routers rtr-224.example.org;
    }
    pool {
        allow members of "foo";
        range 10.17.224.10 10.17.224.250;
    }
    pool {
        deny members of "foo";
        range 10.0.29.10 10.0.29.230;
    }
}'''

>>> tree = dhcpd.loads(test)

>>> dhcpd.dumps(tree) == test
True

>>> print(dhcpd.dumps(tree))
shared-network 224-29 {
    subnet 10.0.29.0 netmask 255.255.255.0 {
        option routers rtr-29.example.org;
    }
    subnet 10.17.224.0 netmask 255.255.255.0 {
        option routers rtr-224.example.org;
    }
    pool {
        allow members of "foo";
        range 10.17.224.10 10.17.224.250;
    }
    pool {
        deny members of "foo";
        range 10.0.29.10 10.0.29.230;
    }
}

>>> new_subnet = dhcpd.nodes.Subnet4(network='192.168.0.0/24')

>>> tree.shared_networks[0].subnets
[Subnet4(network="10.0.29.0/24"), Subnet4(network="10.17.224.0/24")]

>>> tree.shared_networks[0].add_subnet(new_subnet)

>>> tree.shared_networks[0].subnets
[Subnet4(network="10.0.29.0/24"), Subnet4(network="10.17.224.0/24"), Subnet4(network="192.168.0.0/24")]

>>> print(dhcpd.dumps(tree))
shared-network 224-29 {
    subnet 10.0.29.0 netmask 255.255.255.0 {
        option routers rtr-29.example.org;
    }
    subnet 10.17.224.0 netmask 255.255.255.0 {
        option routers rtr-224.example.org;
    }
    subnet 192.168.0.0 netmask 255.255.255.0 {
    }
    pool {
        allow members of "foo";
        range 10.17.224.10 10.17.224.250;
    }
    pool {
        deny members of "foo";
        range 10.0.29.10 10.0.29.230;
    }
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

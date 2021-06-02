# PyISC

A python library with the purpose of parsing and manipulating ISC configuration files. Currently only focused on the dhcpd.conf file but might be expanded in the future.
This module draws inspiration from the reconfigure library found [here](https://github.com/Eugeny/reconfigure).

## Scope of project

The aim of this project it to provide a working ORM for ISC configuration files so that one may use existing, as well as new, files and transform them to a easy to use python data structure.

It is not in scope to provide validation of provided data when supplying new data to a parsed configuration file.

## Installation

Currently a git clone is necessary. If project goes well a package on PyPi might be possible.

## Usage

```python
>>> from pyisc import dhcpd

>>> test = '''shared-network 224-29 {
    subnet 10.17.224.0 netmask 255.255.255.0 {
        option routers rtr-224.example.org;
    }
    subnet 10.0.29.0 netmask 255.255.255.0 {
        option routers rtr-29.example.org;
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
'''

>>> tree = dhcpd.loads(test)

>>> print(f'\nDumped string matches original string: {dhcpd.dumps(tree) == test}\n')

>>> print(dhcpd.dumps(tree))

>>> new_node = dhcpd.Node(type='subnet', value='172.16.0.0', parameters='netmask 255.255.255.0')

>>> tree.children[0].children.append(new_node)

>>> print(dhcpd.dumps(tree))
shared-network 224-29 {
    subnet 10.17.224.0 netmask 255.255.255.0 {
        option routers rtr-224.example.org;
    }
    subnet 10.0.29.0 netmask 255.255.255.0 {
        option routers rtr-29.example.org;
    }
    pool {
        allow members of "foo";
        range 10.17.224.10 10.17.224.250;
    }
    pool {
        deny members of "foo";
        range 10.0.29.10 10.0.29.230;
    }
    subnet 172.16.0.0 netmask 255.255.255.0 {
    }
}
```

## Withstanding issues

* Rework the generate_stmt.py to better group statements into groups and split on those (bools, split on nth occurence and so on).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

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
import pyisc

with open('dhcpd.conf', 'r') as input_file:
    isc_conf = input_file.read()

pyisc.loads(isc_conf)
```

## Withstanding issues

* N/A

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
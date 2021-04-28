# PyISC

A python library with the purpose of parsing ISC configuration files. Currently only focused on the dhcpd.conf file but might be expanded in the future.

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
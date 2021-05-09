# ToDos

* Function that sorts the tree. PropertyNodes need to come first and be sorted based on their key. After that comes the Nodes. Sorting is implemented but might need modification. Currently it sorts the supplied tree instead of returning a new one. Which method i preferable? Also might be of use to allow user to supply their own sorting algorithm by modifying the sort_tree function.
* Print tree should be able to accept Node and PropertyNode Object and not just Rootnode object.
* Currently dhcpd seems to handle everything but eval and leases very well. Issue with them is strings with '=' and maybe other stuff.
* Support for comments.
* Write tests
* Make dokumentation available on free GitHub pages.
* Investigate File lock options or queues for editing file.
* Full dictionary representation with the \__dict__ methods. Might actually skip this.
* In a api scenario it would be prudent to return the index of any children of an object so that it can be used as an key to identify the object. Practical for alterations, delations, insertions and more.
* Rewamp init files? I think one at the pyisc top level would suffice and maybe move the funcions in the current dhcpd init to a new py file.
* ~~Change constructor attributes of Node and ProprteyNode to match in order to make sorting cleaner?~~
* Inline Documentation....

```python
from pyisc import dhcpd
import copy

with open('tests/dhcpd1.conf', 'r') as infile:
    conf = infile.read()

kaka = dhcpd.loads(conf)

kaka_copy = copy.deepcopy(kaka)

sort_tree(kaka_copy)
```

```bash
.
├── LICENSE.txt
├── MANIFEST.in
├── README.md
├── TODO.md
├── data
│   ├── dhcpd-allow_deny.conf
│   ├── dhcpd-classes.conf
│   ├── dhcpd-declarations.conf
│   ├── dhcpd-dns.conf
│   ├── dhcpd-failover.conf
│   ├── dhcpd-options.conf
│   ├── dhcpd-parameters.conf
│   ├── dhcpd-reference\ copy.md
│   ├── dhcpd-reference.md
│   ├── generate_stmt_table.py
│   └── webscraping.py
├── docs
├── pyisc
│   ├── __init__.py
│   ├── bind
│   │   └── __init__.py
│   └── dhcpd
│       ├── __init__.py
│       ├── nodes.py
│       ├── parsers.py
│       └── utils.py
├── requirements.txt
├── setup.py
└── tests
    ├── context.py
    ├── dhcpd1.conf
    ├── named1.conf
    ├── named2.conf
    └── named3.conf
```

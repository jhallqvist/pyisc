# ToDos

* Function that sorts the tree. PropertyNodes need to come first and be sorted based on their key. After that comes the Nodes.
* Full dictionary representation with the \__dict__ methods. Might actually skip this.
* In a api scenario it would be prudent to return the index of any children of an object so that it can be used as an key to identify the object. Practical for alterations, delations, insertions and more.
* ~~Change constructor attributes of Node and ProprteyNode to match in order to make sorting cleaner?~~

```python
from pyisc import dhcpd

with open('tests/dhcpd1.conf', 'r') as infile:
    conf = infile.read()

kaka = dhcpd.loads(conf)

def sort_tree_algorithm(x):
    sort_order = {
        'key': 1,
        'failover': 2,
        'subnet': 3,
        'host': 4,
        'class': 5,
        'shared-network': 6,
        'group': 7,
        'subclass': 8}
    condition_one = sort_order.get(x.type, 0)
    condition_two = x.type
    condition_three = [int(y) for y in x.value.split('.')] if x.type == 'subnet' else x.value
    return (condition_one, condition_two, condition_three)

def sort_tree(tree):
    tree.children.sort(key=sort_tree_algorithm)
    for child in tree.children:
        if isinstance(child, dhcpd.Node):
            sort_tree(child)
    return tree


sort_tree(kaka)
```

```bash
.
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
│   ├── bind
│   │   └── __init__.py
│   ├── dhcpd
│   │   ├── __init__.py
│   │   ├── nodes.py
│   │   ├── parsers.py
│   │   └── utils.py
│   └── __init__.py
├── tests
│   ├── context.py
│   ├── dhcpd1.conf
│   ├── named1.conf
│   ├── named2.conf
│   └── named3.conf
├── LICENSE.txt
├── MANIFEST.in
├── README.md
├── TODO.md
├── requirements.txt
└── setup.py
```

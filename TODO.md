# ToDos

## DHCPD

- [ ]  Parsing status:
  - [x]  DHCPd Conf - Approved
  - [x]  DHCPd Option - Approved
  - [ ]  DHCPd Eval - Not implemented
  - [ ]  DHCPd Leases - Not implemented
- [ ]  A test and example of combining two files (i.e. load both and insert one into the other).
- [ ]  Change 'formula_general' to 'expression_general'.
- [ ]  Clean up commented code that is no longer needed.
- [ ]  Combine event and expression/formula action in build_tree with parameter action as they do the same thing.
- [ ]  Investigate if there is a gain to create more node types for events and expressions/formula.
- [ ]  Add missing Docstrings for event and expression functions in DhcpdSplitter class.
- [ ]  Find out more about events. Aside from log, execute, set and concat - what more actions exists if any. Should they all be treated equally when parsing?

## BIND

- [ ]  Differences from DHCPD sub-module that needs to be implemented here as well:
  - [ ]  Sorting. Is alphanumerical good enough?
  - [ ]  Split methods and tokenization.
  - [ ]  Reference markdown files

## Shared/Common

- [ ] Investigate if Node class should be inheriting from RootNode to avoid code deduplication?
- [ ] Function that sorts the tree. PropertyNodes need to come first and be sorted based on their key. After that comes the Nodes.
  - [x] Sorting is implemented but might need modification. Currently it sorts the supplied tree instead of returning a new one. Which method i preferable?
    - [x] Chose to rewrite sort_tree function with a nested function so now it does not modify the original tree but returns a new, sorted one instead.
  - [ ]  Might be of use to allow user to supply their own sorting algorithm by modifying the sort_tree function.
- [ ]  Make dokumentation available on free GitHub pages.
- [ ]  Full dictionary representation with the \__dict__ methods. Might actually skip this.
  -  Currently a as_dict method has been created for the RootNode class that works well enough for this.
- [ ]  Inline Documentation....
- [ ]  Make decorators for loads, dumps in order to reduce duplicate code?
- [x]  Make an \__iter__ method for objects with children (RootNode & Node) for easier iteration:
- [x] Change constructor attributes of Node and ProprteyNode to match in order to make sorting cleaner?
- [x] Make a dumps function take an argument for disabling comments. Defalt is enabled.
- [x] Support for comments is done. But inline comments will not be supported.
- [x] Print tree should be able to accept Node and PropertyNode Object and not just Rootnode object.
  - Done with the help of a nested inner function that handles the recursion. This function will now always print the supplied object and its children.

## Related to other projects

- [ ]  Investigate File lock options or queues for editing file.
- [ ]  In a api scenario it would be prudent to return the index of any children of an object so that it can be used as an key to identify the object. Practical for alterations, delations, insertions and more.
  -  This has been made possible with the enable_index parameter in the print_tree function of the shared sub-module

## Unrelated info

```python
from pyisc import dhcpd

with open('old_tests/dhcpd1.conf', 'r') as infile:
    conf = infile.read()

kaka = dhcpd.loads(conf)

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

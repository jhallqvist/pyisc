# ToDos

## DHCPD

- [ ] Based on ISC KB I believe that all parameters and all declarations are allowed within a scoped declaration (declaration with {}). This needs to be tested as it is relevant to the validation in the future RestAPI. If this is true then there will only be a few pydantid schemas necessary which would be great.
- [ ] Add print_tree, sort, get_node and other functions from shared.utils as methods to either the Parser class or a new class? Advantage of this would b a simpler way of working with the tree. Maybe combine this with a new init for the Parser class that would need the unparsed string (ie. a self.content to the parser class).
- [ ] Validator for the file. The flow of editing a file should be load file to Object Tree, Edit as needed, write dump to candidate file, verify candidate file with supplied ISC tools for the task, if file ok move original and append a date prefix to the file, rename candidate to the original file name and restart server to read the file.
- [ ] Parsing status:
  - [x] DHCPd Conf - Parses as expected.
  - [x] DHCPd Option - Parses as expected.
  - [ ] DHCPd Eval - Not implemented
  - [ ] DHCPd Leases - Not implemented
  - [ ] Tighten the RegExes even more. They are very generous currently.
- [ ] Tests:
  - [ ] A test and example of combining two files (i.e. load both and insert one into the other).
  - [ ] A test for loads and dumps function.
  - [ ] Tests to verify string gets expected token?
- [ ] Implement a isinstance check for append and extend to make certain only allowed objects gets injected.
- [ ] Clean up commented code that is no longer needed.
- [ ] Investigate if there is a gain to create more node types for events and expressions/formula.
- [ ] Find out more about events. Aside from log, execute, set and concat - what more actions exists if any. Should they all be treated equally when parsing?
  - ~~Currently the dumps function adds a space between execute/log and the paranthesis. This needs to be investigated to make certain that that space is allowed by dhcpd daemon and doesn't cause a errouneous conf file.~~
    - ~~A config verification of __dhcpd -t -cf /etc/dhcp/dhcpd.conf__ allows the space so whould be ok.~~
  - ~~UPDATE: I have modified the dunder str method for ProperyNode to return a different join if type is execute, log or concat. This returns the string in a more pleasing and correct manner.~~
- [x] Add missing Docstrings for event and expression functions in DhcpdSplitter class.
- [x] Combine event and expression/formula action in build_tree with parameter action as they do the same thing.
- [x] Change 'formula_general' to 'expression_general'.

## BIND

- [ ] Differences from DHCPD sub-module that needs to be implemented here as well:
  - [ ] Sorting. Is alphanumerical good enough?
  - [ ] Split methods and tokenization.
  - [ ] Reference markdown files
- [ ] Might rename to named and create another sub-module for zone files. Depends largely if it is worth doing zone parsing in stead of using dnspython library.

## Zone

- [ ] Learn more on how one works with zone files. Would it be feasable to implement my own parser/constructor for this instead of using dnspython or similar library?
- [ ] If I decide to make this there will be a need for a differnet type of parsing as the zone files are one object per line in the text. And based on how those rows are constructed there might be a need for new types of objects instead of RootNode, Node and ProperyNode.

## Shared/Common

- [ ] Investigate if Node class should be inheriting from RootNode to avoid code deduplication?
- [ ] Function that sorts the tree. PropertyNodes need to come first and be sorted based on their key. After that comes the Nodes.
  - [x] Sorting is implemented but might need modification. Currently it sorts the supplied tree instead of returning a new one. Which method i preferable?
    - [x] Chose to rewrite sort_tree function with a nested function so now it does not modify the original tree but returns a new, sorted one instead.
  - [x] Might be of use to allow user to supply their own sorting algorithm by modifying the sort_tree function.
- [x] Make documentation available on free GitHub pages.
- [x] Full dictionary representation with the \__dict__ methods. Might actually skip this.
  - Currently a as_dict method has been created for the RootNode class that works well enough for this.
- [ ] Inline Documentation....
- [ ] ~~Make decorators for loads, dumps in order to reduce duplicate code?~~
- [x] Make an \__iter__ method for objects with children (RootNode & Node) for easier iteration:
- [x] Change constructor attributes of Node and ProprteyNode to match in order to make sorting cleaner?
- [x] Make a dumps function take an argument for disabling comments. Defalt is enabled.
- [x] Support for comments is done. But inline comments will not be supported.
- [x] Print tree should be able to accept Node and PropertyNode Object and not just Rootnode object.
  - Done with the help of a nested inner function that handles the recursion. This function will now always print the supplied object and its children.

## Related to other projects

- [ ] Investigate File lock options or queues for editing file.
- [ ] In a api scenario it would be prudent to return the index of any children of an object so that it can be used as an key to identify the object. Practical for alterations, delations, insertions and more.
  - This has been made possible with the enable_index parameter in the print_tree function of the shared sub-module

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

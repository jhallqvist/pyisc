# ToDos

* Function that sorts the tree. PropertyNodes need to come first and be sorted based on their key. After that comes the Nodes.
  * ~~Sorting is implemented but might need modification. Currently it sorts the supplied tree instead of returning a new one. Which method i preferable?~~
    * ~~Chose to rewrite sort_tree function with a nested function so now it does not modify the original tree but returns a new, sorted one instead.~~
  * Might be of use to allow user to supply their own sorting algorithm by modifying the sort_tree function.
* Currently dhcpd seems to handle everything but eval and leases very well. Issue with them is strings with '=' and maybe other stuff.
* Write tests
* Make dokumentation available on free GitHub pages.
* Investigate File lock options or queues for editing file.
* Full dictionary representation with the \__dict__ methods. Might actually skip this.
* In a api scenario it would be prudent to return the index of any children of an object so that it can be used as an key to identify the object. Practical for alterations, delations, insertions and more.
* Inline Documentation....
* Make decorators for loads, dumps in order to reduce duplicate code?
* Bind sort seems to be ok if it is just alphanumerical sort.
* Split methods for bind module.
* A test and example of combining two files (i.e. load both and insert one into the other).
* Make an \__iter__ method for objects with children (RootNode & Node) for easier iteration:

  ```python
  def __iter__(self):
      return iter(self.children)
  ```

* ~~Change constructor attributes of Node and ProprteyNode to match in order to make sorting cleaner?~~
* ~~Make a dumps function take an argument for disabling comments. Defalt is enabled~~.
* ~~Support for comments is done. But inline comments will not be supported~~.
* ~~Print tree should be able to accept Node and PropertyNode Object and not just Rootnode object.~~
  * ~~Done with the help of a nested inner function that handles the recursion. This function will now always print the supplied object and its children.~~

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

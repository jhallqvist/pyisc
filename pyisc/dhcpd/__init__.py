# -*- coding: utf-8 -*-
r"""Manipulates ISC dhcpd configuration files.

Enables the conversion of ISC dhcpd conf file to a tree like structure of
objects suitable for alteration and the conversation of that structure to a
string that can easily be written to a file and read by dhcpd daemon.

Example:
    Loading a string from a file:

        >>> from pyisc import dhcpd
        >>> with open('tests/dhcpd1.conf', 'r') as infile:
        ...     isc_config = infile.read()
        >>> isc_tree = dhcpd.loads(isc_config)
        >>> isc_tree
        RootNode(Root)

    Dumping PyISC object tree to string:

        >>> from pyisc import dhcpd
        >>> dhcpd.dumps(isc_tree)
        'option domain-name "example.org";\noption domain-name-servers ...'

Attributes:
    dumps (object): Returns a string created from a PyISC DHCPd object tree
    loads (string): Returns a PyISC DHCPd object tree from a supplied string

"""

__all__ = ['dumps', 'loads', 'print_tree', 'sort_tree']
__version__ = '1.0'
__author__ = 'Jonas Hallqvist'

from pyisc.dhcpd.nodes import Node, PropertyNode
from pyisc.dhcpd.parsers import DhcpdParser
from pyisc.dhcpd.utils import sort_tree_algorithm


def loads(content):
    """Return a PyISC object tree from a supplied string.

    Takes a string, either a custom one or one read from a file, and converts
    it to a PyISC object tree.

    Args:
        content (str): The string that should be converted.

    Returns:
        RootNode: A tree like representation of the supplied string.

    """
    parser = DhcpdParser()
    return parser.build_tree(content)


def dumps(tree, level=0, result=''):
    """Return a string of the PyISC object tree.

    This function takes a PyISC object tree structure and converts it to a
    string ready to be written to a file.

    Args:
        tree (RootNode): The tree structure.
        level (int): The starting indentation for the RootNode.
                     Should be left alone in the default level 0.
        result (str): The string that all objects in the tree structure will
                      be added to. Should be left alone in the default blank
                      string state.

    Returns:
        str: A complete string that is ready to write to a suitable file

    """
    if not hasattr(tree, 'children'):
        return f'{tree};\n'
    for branch in tree.children:
        indent = level * ' '
        if isinstance(branch, PropertyNode):
            result += f'{indent}{branch};\n'
        if isinstance(branch, Node):
            result += f'{indent}{branch} {{\n'
            result = dumps(branch, level=level+4, result=result)
            result += f'{indent}}}\n'
    return result


def print_tree(tree, level=0):
    """Print a string representation of the PyISC object tree.

    This function takes a PyISC object tree structure and prints it.

    Args:
        tree (pyisc.dhcpd.RootNode): The tree structure.
        level (int): The starting indentation for the RootNode.
                     Should be left alone in the default level 0.

    Returns:
        stdout: A printed representaton of the PyISC tree object

    """
    for branch in tree.children:
        indent = level * ' '
        print(f'{indent}{branch}')
        if isinstance(branch, Node):
            print_tree(branch, level+4)


def sort_tree(tree):
    """Sorts the supplied PyISC tree object.

    This functions sorts the supplied object tree recursively, based on a
    sorting algorithm.

    Args:
        tree (pyisc.dhcpd.RootNode): The tree structure.

    Returns:
        nothing

    """
    tree.children.sort(key=sort_tree_algorithm)
    for child in tree.children:
        if isinstance(child, Node):
            sort_tree(child)


'''
Get full Dictionary representation of RootNode with all children
with open('tests/dhcpd1.conf', 'r') as infile:
    conf = infile.read()

import pyisc, json
mongo = pyisc.loads(conf)
json.dumps(mongo, default=lambda x: x.__dict__)
print(json.dumps(mongo, indent=4, default=lambda x: x.__dict__))
'''

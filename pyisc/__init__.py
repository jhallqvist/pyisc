# -*- coding: utf-8 -*-
"""Manipulates ISC dhcpd configuration files.

Enables the conversion of ISC dhcpd conf file to a tree like structure of
objects suitable for alteration and the conversation of that structure to a
string that can easily be written to a file and read by dhcpd daemon.

Example:
    Stuff

Attributes:
    dumps (object): 'Description'
    loads (string): 'Description'


"""

__all__ = ['dumps', 'loads']
__version__ = '1.0'
__author__ = 'Jonas Hallqvist'

from .nodes import Node, PropertyNode
from .parsers import DhcpParser


def loads(content):
    """Return a PyISC object tree from a supplied string.

    Takes a string, either a custom one or one read from a file, and converts
    it to a PyISC object tree.

    Args:
        content (str): The string that should be converted.

    Returns:
        pyisc.RootNode: A tree like representation of the supplied string.

    """
    parser = DhcpParser()
    return parser.build_tree(content)


def dumps(tree, level=0, result=''):
    """Return a string of the PyISC object tree.

    This function takes a PyISC object tree structure and converts it to a
    string ready to be written to a file.

    Args:
        tree (pyisc.RootNode): The tree structure.
        level (int): The starting indentation for the RootNode.
                     Should be left alone in the default level 0.
        result (str): The string that all objects in the tree structure will
                      be added to. Should be left alone in the default blank
                      string state.

    Returns:
        str: A complete string that is ready to write to a suitable file

    """
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
    """TEMP."""
    for branch in tree.children:
        indent = level * ' '
        print(f'{indent}{branch}')
        if isinstance(branch, Node):
            print_tree(branch, level+4)


'''
with open('tests/dhcpd1.conf', 'r') as infile:
    conf = infile.read()

import pyisc, json
mongo = pyisc.loads(conf)
json.dumps(mongo, default=lambda x: x.__dict__)
'''

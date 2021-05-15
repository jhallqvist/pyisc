# Copyright 2021 Jonas Hallqvist

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Manipulates ISC named configuration files.

Enables the conversion of ISC named conf file to a tree like structure of
objects suitable for alteration and the conversation of that structure to a
string that can easily be written to a file and read by dhcpd daemon.

Example:
    Load file and add statement:

        >>> from pyisc import bind
        >>> with open('etc/named.conf', 'r') as infile:
        ...     isc_config = infile.read()
        >>> isc_tree = bind.loads(isc_config)
        >>> print(bind.dumps(isc_tree))
        .........

Attributes:
    dumps (object): Returns a string created from a PyISC Named object tree
    loads (string): Returns a PyISC Named object tree from a supplied string

"""

__all__ = ['dumps', 'loads', 'print_tree', 'sort_tree']
__version__ = '1.0'
__author__ = 'Jonas Hallqvist'

from pyisc.shared.nodes import Node, PropertyNode
from pyisc.bind.parsing import BindParser
from pyisc.shared.utils import sort_tree_algorithm


def loads(content):
    """Return a PyISC object tree from a supplied string.

    Takes a string, either a custom one or one read from a file, and converts
    it to a PyISC object tree.

    Args:
        content (str): The string that should be converted.

    Returns:
        pyisc.shared.nodes.RootNode: A tree like representation of the
            supplied string.

    Examples:
        >>> from pyisc import bind
        >>> with open('tests/named.conf', 'r') as infile:
        ...     isc_config = infile.read()
        >>> isc_tree = bind.loads(isc_config)
        >>> isc_tree
        RootNode(Root)

    """
    parser = BindParser()
    return parser.build_tree(content)


def dumps(tree, level=0, result=''):
    r"""Return a string of the PyISC object tree.

    This function takes a PyISC object tree structure and converts it to a
    string ready to be written to a file.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.
        level (int): The starting indentation for the RootNode.
                     Should be left alone in the default level 0.
        result (str): The string that all objects in the tree structure will
                      be added to. Should be left alone in the default blank
                      string state.

    Returns:
        str: A complete string that is ready to write to a suitable file

    Examples:
        >>> from pyisc import bind
        >>> bind.dumps(isc_tree)
        'zone "example.com" {\n    type master;\n};\n'

    """
    for branch in tree.children:
        indent = level * ' '
        if branch.comment:
            result += f'{branch.comment}\n'
        if isinstance(branch, PropertyNode):
            result += f'{indent}{branch};\n'
        if isinstance(branch, Node):
            result += f'{indent}{branch} {{\n'
            result = dumps(branch, level=level+4, result=result)
            result += f'{indent}}};\n'
            if level == 0:
                result += '\n'
    return result


def print_tree(tree, level=0):
    """Print a string representation of the PyISC object tree.

    This function takes a PyISC object tree structure and prints it.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.
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
        tree (pyisc.shared.nodes.RootNode): The tree structure.

    Returns:
        nothing

    """
    tree.children.sort(key=sort_tree_algorithm)
    for child in tree.children:
        if isinstance(child, Node):
            sort_tree(child)

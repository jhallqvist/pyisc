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

"""General helper functions and classes for the module."""

import copy
import shlex

from pyisc.shared.nodes import Node, PropertyNode


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class TokenSplitter:
    """A static class used to provide case / switch like functionality.

    The switch takes a supplied token and matches the type of that
    token to a method. If a match is found that method is executed
    and the result returned.
    If a match is not found the default lambda expression will be
    used instead. The entire purpose is to split a value of the
    supplied token the desired way.
    """

    def switch(self, token):
        """
        Return list of splitted token string.

        Args:
            token (pyisc.shared.parsing.Token): A supplied token instance.

        Returns:
            list: List of the now splitted string

        Examples:
            >>> token = Token('parameter_option',
            ...               'option domain-name "example.org";')
            >>> splitter = TokenSplitter()
            >>> splitter.switch(token)
            ['option domain-name', '"example.org"', None, None]

        """
        self.token = token
        default = 'No split method found'
        return getattr(self, str(token.type), lambda: default)() + [None, None]


def split_at(string, pos):
    """
    Return string splitted at the desired separator.  Whitespace is normalized,
         except in quoted strings

    Args:
        string (str): The supplied string that will be splitted.
        pos (int): The desired occurence of the defined separator
            within the supplied string and hence the point of the split
            operation.

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'option domain-name "example.org";'
        >>> shared.utils.split_at(isc_string, 2)
        ['option domain-name', '"example.org";']

    """
    string = shlex.split(string, posix=False)
    return [' '.join(string[:pos]), ' '.join(string[pos:])]


def split_from(string, pos):
    """
    Return string splitted from the desired separator.  Whitespace is normalized.
         except in quoted strings

    Args:
        string (str): The supplied string that will be splitted.
        pos (int): The desired first occurence of the defined separator
            within the supplied string. This will be the position of
            the first split performed.

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'failover peer "dhcpd-failover" state'
        >>> shared.utils.split_from(isc_string, 2)
        ['failover peer', '"dhcpd-failover"', 'state']

    """
    string = shlex.split(string, posix=False)
    return [' '.join(string[:pos])] + string[pos:]


def event_split(string, event_type):
    """Return a list of event type and event action.

    Args:
        string (str): The supplied string that will be splitted.
        event_type (str): The event type (execute, log, set, etc).

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'set ClientIP = binary-to-ascii(10, 8, ".", leased-address);'
        >>> shared.utils.event_split(isc_string, 'set')
        ['set', ' ClientIP = binary-to-ascii(10, 8, ".", leased-address);']

    """ # noqa
    word_len = len(event_type)
    return [string[:word_len].strip(), string[word_len:].strip()]


def sort_tree(tree, sort_algorithm=None):
    """Sorts the supplied PyISC tree object.

    This functions sorts the supplied object tree recursively, based on
    a sorting algorithm.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.

    Returns:
        pyisc.shared.nodes.RootNode: A sorted copy of the inputted tree object.

    """
    tree_copy = copy.deepcopy(tree)

    def inner_func(tree):
        tree.children.sort(key=sort_algorithm)
        for child in tree.children:
            if isinstance(child, Node):
                inner_func(child)

    inner_func(tree_copy)
    return tree_copy


def print_tree(tree, level=0, enable_index=False):
    """Print a string representation of the PyISC object tree.

    This function takes a PyISC object tree structure and prints it.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.
        level (int): The starting indentation for the RootNode.
            Should be left alone in the default level 0.
        enable_index (boolean): If set to True the function will print an index
            number in front of each object in the tree.

    Returns:
        stdout: A printed representaton of the PyISC tree object

    """
    print(tree)

    def inner_func(tree, level):
        for index, branch in enumerate(tree.children):
            indent = level * ' '
            if enable_index:
                print(f'{indent}{index}: {branch}')
            else:
                print(f'{indent}{branch}')
            if isinstance(branch, Node):
                inner_func(branch, level+4)

    inner_func(tree, level+4)


def get_node(tree, node_type, node_value=None):
    """Return a specific node that matches the search criteria.

    This function will return the first match of an object from a PyISC object
    tree.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.
        node_type (str): A string that will should be matched to the type
            attribute of Node instance.
        node_value (str): A string that will should be matched to the value
            attribute of Node instance.

    Returns:
        pyisc.shared.nodes.Node: The found object.

    Examples:
        >>> pyisc.shared.utils.get_node(isc_tree, 'subnet', '192.168.1.0')
        Node(subnet, 192.168.1.0, netmask 255.255.252.0)

    """
    for branch in tree.children:
        if (node_type == branch.type and node_value == branch.value):
            return branch
        if isinstance(branch, Node):
            result = get_node(
                branch,
                node_type=node_type,
                node_value=node_value)
            if result:
                return result


def get_node_types(tree, node_type, node_list=None):
    """Return a list of nodes matching search criteria.

    The function returns a list containing all the nodes of a certain type
    found in the supplied PyISC object tree.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.
        node_type (str): A string that will should be matched to the type
            attribute of Node instance.
        node_list (None): Initially this will be None but as the function runs
            this will be replaced by a list that contains all nodes matching
            the search string.

    Returns:
        list: A list that contains all found node objects.

    Examples:
        >>> get_node_types(isc_tree, 'host')
        [Node(host, passacaglia, None), Node(host, fantasia, None), Node(...)]

    """
    if not node_list:
        node_list = []
    for branch in tree.children:
        if branch.type == node_type:
            node_list.append(branch)
        if isinstance(branch, Node):
            get_node_types(branch, node_type=node_type, node_list=node_list)
    return node_list


def find_node(tree, node_type, node_value=None, level=0):
    """Prints entire tree and highlights the specific node with bold text or
    similar."""
    print(tree)

    def inner_func(tree, level):
        for branch in tree.children:
            indent = level * ' '
            if (node_type == branch.type and node_value == branch.value):
                print(f'{indent}{color.BOLD}{branch}{color.END}')
            else:
                print(f'{indent}{branch}')
            if isinstance(branch, Node):
                inner_func(branch, level+4)

    inner_func(tree, level+4)


def find_node_types(tree, node_type, level=0):
    """Prints entire tree and highlights the node with a specific node type
    with bold text or similar."""
    print(tree)

    def inner_func(tree, level):
        for branch in tree.children:
            indent = level * ' '
            if (node_type == branch.type):
                print(f'{indent}{color.BOLD}{branch}{color.END}')
            else:
                print(f'{indent}{branch}')
            if isinstance(branch, Node):
                inner_func(branch, level+4)

    inner_func(tree, level+4)


def string_constructor(tree, level=0, result='', enable_comments=True,
                       section_end=None):
    """Return a string of PyISC tree."""
    for branch in tree.children:
        indent = level * ' '
        if branch.comment and enable_comments:
            result += f'{branch.comment}\n'
        if isinstance(branch, PropertyNode):
            result += f'{indent}{branch};\n'
        if isinstance(branch, Node):
            result += f'{indent}{branch} {{\n'
            result = string_constructor(
                            tree=branch, level=level+4, result=result,
                            enable_comments=enable_comments,
                            section_end=section_end)
            result += f'{indent}{section_end}\n'
            # if level == 0:
            #     result += '\n'
    return result

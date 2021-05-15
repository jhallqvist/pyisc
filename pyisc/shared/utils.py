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


def split_at(string, sep, pos):
    """
    Return string splitted at the desired separator.

    Args:
        string (str): The supplied string that will be splitted.
        sep (str): The desired separator to use for the split.
        pos (int): The desired occurence of the defined separator
            within the supplied string and hence the point of the split
            operation.

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'option domain-name "example.org";'
        >>> shared.utils.split_at(isc_string, ' ', 2)
        ['option domain-name', '"example.org";']

    """
    string = string.split(sep)
    return [sep.join(string[:pos]), sep.join(string[pos:])]


def split_from(string, sep, pos):
    """
    Return string splitted from the desired separator.

    Args:
        string (str): The supplied string that will be splitted.
        sep (str): The desired separator to use for the split.
        pos (int): The desired first occurence of the defined separator
            within the supplied string. This will be the position of
            the first split performed.

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'failover peer "dhcpd-failover" state'
        >>> shared.utils.split_from(isc_string, ' ', 2)
        ['failover peer', '"dhcpd-failover"', 'state']

    """
    string = string.split(sep)
    return [sep.join(string[:pos])] + string[pos:]


def sort_tree_algorithm(child):
    """Return tuple of values for sorting.

    This is meant to be supplied to the sort functions key attribute.
    It will sort sort on the object type where mostly all PropertyNodes
    will be prioritized.

    Args:
        string (str): The supplied string that will be splitted.
        child (pyisc.shared.nodes.Node, pyisc.shared.nodes.PropertyNode): The
            child instance supplied by the sort function.

    Returns:
        tuple: A tuple with three entires representing the sorting conditions
            in order of decreasing order.
    """
    sort_order = {
        'key': 1,
        'failover': 2,
        'subnet': 3,
        'host': 4,
        'class': 5,
        'shared-network': 6,
        'group': 7,
        'subclass': 8}
    condition_one = sort_order.get(child.type, 0)
    condition_two = child.type
    condition_three = [int(octet) for octet in child.value.split('.')] if \
        child.type == 'subnet' else child.value
    return (condition_one, condition_two, condition_three)

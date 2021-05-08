"""General helper functions and classes for the module."""


class TokenSplitter:
    """A static class used to provide case / switch like functionality.

    The switch takes a supplied token and matches the type of that token to a
    method. If a match is found that method is executed and the result
    returned.
    If a match is not found the default lambda expression will be used instead.
    The entire purpose is to split a value of the supplied token the desired
    way.
    """

    def switch(self, token):
        """
        Return list of splitted token string.

        Args:
            token (Token): A supplied token instance.

        Returns:
            list: List of the now splitted string

        Examples:
            >>> token = Token('parameter_option','option domain-name "example.org";')
            >>> TokenSplitter.switch(token)
            ['option domain-name', '"example.org"', None, None]

        """
        self.token = token
        default = token.value[:-1].split() + [None, None]
        return getattr(self, str(token.type), lambda: default)()

    def parameter_option(self):
        """Return a list where the first two words of the string is the key."""
        return split_at(self.token.value[:-1], ' ', 2) + [None, None]

    def parameter_single_value(self):
        """Return a list where the last word in the string is the value."""
        return self.token.value[:-1].rsplit(None, 1) + [None, None]

    def parameter_multiple_values(self):
        """Return a list where the expected value of the string contains space."""
        return self.token.value[:-1].split(None, 2) + [None, None]

    def parameter_single_key(self):
        """Return a list where the first word in the string is the key."""
        return self.token.value[:-1].split(None, 1) + [None, None]


def split_at(string, sep, pos):
    """
    Return string splitted at the desired separator.

    Args:
        string (str): The supplied string that will be splitted.
        sep (str): The desired separator to use for the split.
        pos (int): The desired occurence of the defined separator within the
            supplied string and hence the point of the split operation.

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'option domain-name "example.org";'
        >>> dhcpd.utils.split_at(isc_string, ' ', 2)
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
        pos (int): The desired first occurence of the defined separator within
            the supplied string. This will be the position of the first split
            performed.

    Returns:
        list: A list of the splitted string

    Examples:
        >>> isc_string = 'failover peer "dhcpd-failover" state'
        >>> dhcpd.utils.split_from(isc_string, ' ', 2)
        ['failover peer', '"dhcpd-failover"', 'state']

    """
    string = string.split(sep)
    return [sep.join(string[:2])] + string[2:]


def sort_tree_algorithm(child):
    """Return tuple of values for sorting.

    This is meant to be supplied to the sort functions key attribute. It will
    sort sort on the object type where mostly all PropertyNodes will be
    prioritized.
    Args:
        child (Node, PropertyNode): The child instance supplied by the sort
            function.

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

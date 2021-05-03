"""General helper functions and classes for the module."""


class TokenSplitter:
    """A static class used to provide case / switch functionality."""

    def switch(self, token):
        """
        Return list of splitted token string.

        :param token: A supplied token instance of the Token named tuple type.
        :type token: pyisc.Token
        :return: Returns a list of values from a supplied Token value.
        :rtype: list
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
        """Return a list where the value derived from the string contains space."""
        return self.token.value[:-1].split(None, 2) + [None, None]

    def parameter_single_key(self):
        """Return a list where the first word in the string is the key."""
        return self.token.value[:-1].split(None, 1) + [None, None]

def split_at(string, sep, pos):
    """
    Return string splitted at the desired separator.

    :param string: The supplied string that will be splitted.
    :type string: str
    :param sep: The desired separator to use for the split.
    :type sep: str
    :param pos: The desired occurence of the defined separator within the
        supplied string and hence the point of the split operation.
    :type pos: int
    :return: Returns a list of the values derived from the split of supplied
        string.
    :rtype: list
    """
    string = string.split(sep)
    return [sep.join(string[:pos]), sep.join(string[pos:])]


def split_from(string, sep, pos):
    """
    Return string splitted from the desired separator.

    :param string: The supplied string that will be splitted.
    :type string: str
    :param sep: The desired separator to use for the split.
    :type sep: str
    :param pos: The desired first occurence of the defined separator within
        the supplied string. This will be the position of the first split
        performed.
    :type pos: int
    :return: Returns a list of the values derived from the split of supplied
        string.
    :rtype: list
    """
    string = string.split(sep)
    return [sep.join(string[:2])] + string[2:]

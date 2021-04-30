"""TEMP."""


def nth_split(string, sep, pos):
    """TEMP."""
    string = string.split(sep)
    return [sep.join(string[:pos]), sep.join(string[pos:])]


def split_from(string, sep, pos):
    """TEMP."""
    string = string.split(sep)
    return [sep.join(string[:2])] + string[2:]


"""
Possibly needed function:
* ?
"""

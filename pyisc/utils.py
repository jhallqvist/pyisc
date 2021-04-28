"""TEMP."""


def nth_split(string, sep, pos):
    """TEMP."""
    string = string.split(sep)
    return sep.join(string[:pos]), sep.join(string[pos:])

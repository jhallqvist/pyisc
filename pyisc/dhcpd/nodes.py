"""TEMP."""

from collections import namedtuple


class RootNode:
    """Represents the root of the tree."""

    def __init__(self, type='Root'):
        """TEMP."""
        self.type = type
        self.children = []

    def __str__(self):
        """TEMP."""
        return f'{self.type}'

    def __repr__(self):
        """TEMP."""
        return f'RootNode({self.type})'
        # return repr(self.__dict__)


class Node:
    """Represents an entity capable of having properties."""

    def __init__(self, type=None, value=None, parameters=None):
        """TEMP."""
        self.type = type
        self.value = value
        self.children = []
        self.parameters = parameters

    def __eq__(self, other):
        """TEMP."""
        if other is None:
            return False
        return (
            self.type == other.type and
            self.value == other.value and
            self.parameters == other.parameters and
            set(self.children) == set(other.children)
        )

    def __str__(self):
        """TEMP."""
        return f'{" ".join(filter(None, (self.type, self.value, self.parameters)))}'

    def __repr__(self):
        """TEMP."""
        return f'Node({self.type}, {self.value}, {self.parameters})'
        # return repr(self.__dict__)


class PropertyNode:
    """Represents a property of a node."""

    def __init__(self, type=None, value=None, parameters=None):
        """TEMP."""
        self.type = type
        self.value = value
        self.parameters = parameters

    def __eq__(self, other):
        """TEMP."""
        if other is None:
            return False
        return (
            self.type == other.type and
            self.value == other.value and
            self.parameters == other.parameters
        )

    def __lt__(self, other):
        return self.type < other.type

    def __str__(self):
        """TEMP."""
        return f'{" ".join(filter(None, (self.type, self.value, self.parameters)))}'
        # return f'{self.name} {self.value}'

    def __repr__(self):
        """TEMP."""
        return f'PropertyNode({self.type}, {self.value}, {self.parameters})'
        # return repr(self.__dict__)


Token = namedtuple('Token', ['type', 'value'])

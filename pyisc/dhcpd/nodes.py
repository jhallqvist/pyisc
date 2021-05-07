"""Contains the different node object definitions."""

from collections import namedtuple


class RootNode:
    """Represents the root of the tree."""

    def __init__(self, type='Root'):
        """Initialize attributes for the class.

        Args:
            type (str): A name for the instance. Defaults to 'Root' if none is
                supplied.
            children (list): Initially an empty list. Children will get
                appended as needed.

        """
        self.type = type
        self.children = []

    def __str__(self):
        """Return string of instance."""
        return f'{self.type}'

    def __repr__(self):
        """Return representation of instance."""
        return f'RootNode({self.type})'


class Node:
    """Represents an entity capable of having properties."""

    def __init__(self, type=None, value=None, parameters=None):
        """Initialize attributes for the class.

        Args:
            type (str): A name for the instance.
            value (str): The value for the type. In the case of a subnet type
                this would be an ip address. Not always assigned.
            children (list): Initially an empty list. Children will get
                appended as needed.
            parameters (str): Optional data for some of the nodes. Nodes of
                type subnet will have 'netmask x.x.x.x' as parameters.

        """
        self.type = type
        self.value = value
        self.children = []
        self.parameters = parameters

    def __eq__(self, other):
        """Return boolean value from comparison with other object."""
        if other is None:
            return False
        return (
            self.type == other.type and
            self.value == other.value and
            self.parameters == other.parameters and
            set(self.children) == set(other.children)
        )

    def __str__(self):
        """Return string of instance."""
        return f'{" ".join(filter(None, (self.type, self.value, self.parameters)))}'

    def __repr__(self):
        """Return representation of instance."""
        return f'Node({self.type}, {self.value}, {self.parameters})'


class PropertyNode:
    """Represents a property of a node."""

    def __init__(self, type=None, value=None, parameters=None):
        """Initialize attributes for the class.

        Args:
            type (str): A name for the instance.
            value (str): The value for the type.
            parameters (str): Optional data for some of the nodes. Nodes of
                type failover or subclass will have parameters.

        """
        self.type = type
        self.value = value
        self.parameters = parameters

    def __eq__(self, other):
        """Return boolean value from comparison with other object."""
        if other is None:
            return False
        return (
            self.type == other.type and
            self.value == other.value and
            self.parameters == other.parameters
        )

    def __lt__(self, other):
        """Return boolean value from comparison with other object."""
        return self.type < other.type

    def __str__(self):
        """Return string of instance."""
        return f'{" ".join(filter(None, (self.type, self.value, self.parameters)))}'

    def __repr__(self):
        """Return representation of instance."""
        return f'PropertyNode({self.type}, {self.value}, {self.parameters})'


Token = namedtuple('Token', ['type', 'value'])

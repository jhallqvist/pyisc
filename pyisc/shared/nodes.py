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

"""Contains the different node object definitions."""
import json


class RootNode:
    """Represents the root of the tree."""

    def __init__(self, type='Root', children=None):
        """Initialize attributes for the class.

        Args:
            type (str): A name for the instance. Defaults to 'Root' if
                none is supplied.
            children (list): Initially an empty list. Children will get
                appended as needed.

        """
        self.type = type
        self._children = [] if not children else children

    def __eq__(self, other):
        """Return boolean value from comparison with other object."""
        if other is None:
            return False
        return (
            self.type == other.type and
            set(self.children) == set(other.children)
        )

    def __hash__(self):
        """Return hash(self)."""
        return sum(hash(x) for x in [self.type] + self.children)

    def __str__(self):
        """Return string of instance."""
        return f'{self.type}'

    def __repr__(self):
        """Return representation of instance."""
        return f'RootNode({self.type}, children: {len(self.children)})'

    def __iter__(self):
        """Implement iter(self) with child objects in instance."""
        return iter(self.children)

    def as_dict(self):
        json_str = json.dumps(self, default=lambda x: x.__dict__)
        return json.loads(json_str)

    @property
    def children(self):
        """Getter for self._children."""
        return self._children

    @children.setter
    def children(self, val):
        """Setter for self._children."""
        self._children = val

    def append(self, val):
        """Implements append method on self to append directly to children."""
        return self.children.append(val)

    def extend(self, val):
        """Implements extend method on self to extend directly to children."""
        return self.children.extend(val)


class Node:
    """Represents an entity capable of having properties."""

    def __init__(self, type=None, value=None, parameters=None, children=None):
        """Initialize attributes for the class.

        Args:
            type (str): A name for the instance.
            value (str): The value for the type. In the case of a
                subnet type this would be an ip address. Not always
                assigned.
            children (list): Initially an empty list. Children will get
                appended as needed.
            parameters (str): Optional data for some of the nodes.
                Nodes of type subnet will have 'netmask x.x.x.x' as
                parameters.

        """
        self.type = type
        self.value = value
        self.children = [] if not children else children
        self.parameters = parameters
        self.comment = None

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

    def __lt__(self, other):
        """Return boolean value from comparison with other object."""
        return self.type < other.type

    def __hash__(self):
        return sum(
            hash(x) for x in [self.type, self.value, self.parameters]
            + self.children)

    def __str__(self):
        """Return string of instance."""
        string_repr = filter(None, (self.type, self.value, self.parameters))
        return f'{" ".join(string_repr)}'

    def __repr__(self):
        """Return representation of instance."""
        return f'Node({self.type}, {self.value}, {self.parameters})'

    def __iter__(self):
        """Implement iter(self) with child objects in instance."""
        return iter(self.children)

    @property
    def children(self):
        """Getter for self._children."""
        return self._children

    @children.setter
    def children(self, val):
        """Setter for self._children."""
        self._children = val

    def append(self, val):
        """Implements append method on self to append directly to children."""
        return self.children.append(val)

    def extend(self, val):
        """Implements extend method on self to extend directly to children."""
        return self.children.extend(val)


class PropertyNode:
    """Represents a property of a node."""

    def __init__(self, type=None, value=None, parameters=None):
        """Initialize attributes for the class.

        Args:
            type (str): A name for the instance.
            value (str): The value for the type.
            parameters (str): Optional data for some of the nodes. Nodes
                of type failover or subclass will have parameters.

        """
        self.type = type
        self.value = value
        self.parameters = parameters
        self.comment = None

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

    def __hash__(self):
        return sum(hash(x) for x in [self.type, self.value, self.parameters])

    def __str__(self):
        """Return string of instance."""
        string_repr = filter(None, (self.type, self.value, self.parameters))
        if self.type in ('execute', 'log', 'concat'):
            return f'{"".join(string_repr)}'
        return f'{" ".join(string_repr)}'

    def __repr__(self):
        """Return representation of instance."""
        return f'PropertyNode({self.type}, {self.value}, {self.parameters})'

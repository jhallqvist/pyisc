"""TEMP."""

__version__ = '1.0'
__all__ = [
    'dumps', 'loads',
]

__author__ = 'Jonas Hallqvist'

from .nodes import Node, PropertyNode
from .parsers import IscParser


def loads(content):
    """TEMP."""
    parser = IscParser()
    return parser.build_tree(content)


def dumps(tree, level=0, result=''):
    """TEMP."""
    for branch in tree.children:
        indent = level * ' '
        if isinstance(branch, PropertyNode):
            result += f'{indent}{branch};\n'
        if isinstance(branch, Node):
            result += f'{indent}{branch} {{\n'
            result = dumps(branch, level=level+4, result=result)
            result += f'{indent}}}\n'
    return result


def print_tree(tree, level=0):
    """TEMP."""
    for branch in tree.children:
        indent = level * ' '
        print(f'{indent}{branch}')
        if isinstance(branch, Node):
            print_tree(branch, level+4)


'''
with open('tests/dhcpd1.conf', 'r') as infile:
    conf = infile.read()

import parse_isc, json
mongo = parse_isc.loads(conf)
json.dumps(mongo, default=lambda x: x.__dict__)
'''

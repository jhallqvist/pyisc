"""TEMP."""


from pyisc import shared

expected_bind = shared.nodes.RootNode('Root')

# Child 1
new_node = shared.nodes.Node('options', None, None)
child = shared.nodes.PropertyNode('directory', '"/var/lib/named"', None)
new_node.children.append(child)
child = shared.nodes.PropertyNode(
    'dump-file',
    '"/var/log/named_dump.db"',
    None)
new_node.children.append(child)
child = shared.nodes.PropertyNode(
    'statistics-file',
    '"/var/log/named.stats"',
    None)
new_node.children.append(child)
child = shared.nodes.Node('forwarders', None, None)
sub_child = shared.nodes.PropertyNode('62.31.176.39', None, None)
child.children.append(sub_child)
sub_child = shared.nodes.PropertyNode('193.38.113.3', None, None)
child.children.append(sub_child)
new_node.children.append(child)
child = shared.nodes.Node('listen-on-v6', None, None)
sub_child = shared.nodes.PropertyNode('any', None, None)
child.children.append(sub_child)
new_node.children.append(child)
child = shared.nodes.PropertyNode('notify', 'no', None)
new_node.children.append(child)
expected_bind.children.append(new_node)
# Child 2
new_node = shared.nodes.Node('zone', '"."', 'in')
child = shared.nodes.PropertyNode('type', 'hint', None)
new_node.children.append(child)
child = shared.nodes.PropertyNode('file', '"root.hint"', None)
new_node.children.append(child)
expected_bind.children.append(new_node)
# Child 3
new_node = shared.nodes.Node('zone', '"localhost"', 'in')
child = shared.nodes.PropertyNode('type', 'master', None)
new_node.children.append(child)
child = shared.nodes.PropertyNode('file', '"localhost.zone"', None)
new_node.children.append(child)
expected_bind.children.append(new_node)
# Child 4
new_node = shared.nodes.Node('zone', '"0.0.127.in-addr.arpa"', 'in')
child = shared.nodes.PropertyNode('type', 'master', None)
new_node.children.append(child)
child = shared.nodes.PropertyNode('file', '"127.0.0.zone"', None)
new_node.children.append(child)
expected_bind.children.append(new_node)
# Child 5
new_node = shared.nodes.Node('zone', '"spring.wellho.net"', 'in')
child = shared.nodes.PropertyNode('type', 'master', None)
new_node.children.append(child)
child = shared.nodes.PropertyNode(
    'file',
    '"/var/lib/named/wellho.zone"',
    None)
new_node.children.append(child)
expected_bind.children.append(new_node)
# Child 6
new_node = shared.nodes.PropertyNode(
    'include',
    '"/etc/named.conf.include"',
    None)
expected_bind.children.append(new_node)

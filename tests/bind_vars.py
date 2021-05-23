"""TEMP."""


from pyisc.shared.nodes import RootNode, Node, PropertyNode

expected_bind = RootNode('Root')

child1 = Node(
    type='options',
    value=None,
    parameters=None,
    children=[
        PropertyNode(
            type='directory',
            value='"/var/lib/named"',
            parameters=None),
        PropertyNode(
            type='dump-file',
            value='"/var/log/named_dump.db"',
            parameters=None),
        PropertyNode(
            type='statistics-file',
            value='"/var/log/named.stats"',
            parameters=None),
        Node(
            type='forwarders',
            value=None,
            parameters=None,
            children=[
                PropertyNode(
                    type='62.31.176.39',
                    value=None,
                    parameters=None),
                PropertyNode(
                    type='193.38.113.3',
                    value=None,
                    parameters=None)
            ]
        ),
        Node(
            type='listen-on-v6',
            value=None,
            parameters=None,
            children=[
                PropertyNode(
                    type='any',
                    value=None,
                    parameters=None)
            ]
        ),
        PropertyNode(
            type='notify',
            value='no',
            parameters=None)
        ])

child2 = Node(
    type='zone',
    value='"."',
    parameters='in',
    children=[
        PropertyNode(
            type='type',
            value='hint',
            parameters=None),
        PropertyNode(
            type='file',
            value='"root.hint"',
            parameters=None)
    ]
)

child3 = Node(
    type='zone',
    value='"localhost"',
    parameters='in',
    children=[
        PropertyNode(
            type='type',
            value='master',
            parameters=None),
        PropertyNode(
            type='file',
            value='"localhost.zone"',
            parameters=None)
    ]
)

child4 = Node(
    type='zone',
    value='"0.0.127.in-addr.arpa"',
    parameters='in',
    children=[
        PropertyNode(
            type='type',
            value='master',
            parameters=None),
        PropertyNode('file', '"127.0.0.zone"', None)
    ]
)

child5 = Node(
    type='zone',
    value='"spring.wellho.net"',
    parameters='in',
    children=[
        PropertyNode(
            type='type',
            value='master',
            parameters=None),
        PropertyNode(
            type='file',
            value='"/var/lib/named/wellho.zone"',
            parameters=None)
    ]
)

child6 = PropertyNode(
    type='include',
    value='"/etc/named.conf.include"',
    parameters=None
)

expected_bind.extend(
    [
        child1,
        child2,
        child3,
        child4,
        child5,
        child6
    ]
)

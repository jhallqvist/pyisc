"""TEMP."""


from context import pyisc

expected_dhcpd = pyisc.dhcpd.nodes.RootNode('Root')

new_node = (pyisc.dhcpd.nodes.Node('class', '"ras-clients"', None))
new_node.children.append(pyisc.dhcpd.PropertyNode('match', 'if substring (option dhcp-client-identifier, 1, 3) = "RAS"', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('class', '"allocation-class-1"', None))
new_node.children.append(pyisc.dhcpd.PropertyNode('match', 'pick-first-value (option dhcp-client-identifier, hardware)', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('class', '"allocation-class-2"', None))
new_node.children.append(pyisc.dhcpd.PropertyNode('match', 'pick-first-value (option dhcp-client-identifier, hardware)', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('class', '"limited-1"', None))
new_node.children.append(pyisc.dhcpd.PropertyNode('lease limit', '4', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.PropertyNode('subclass', '"allocation-class-1"', '1:8:0:2b:4c:39:ad'))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.PropertyNode('subclass', '"allocation-class-2"', '1:8:0:2b:a9:cc:e3'))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.PropertyNode('subclass', '"allocation-class-1"', '1:0:0:c4:aa:29:44'))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('subnet', '10.0.0.0', 'netmask 255.255.255.0'))
child_node = (pyisc.dhcpd.nodes.Node('pool', None, None))
child_node.children.append(pyisc.dhcpd.nodes.PropertyNode('allow', 'members of "allocation-class-1"', None))
child_node.children.append(pyisc.dhcpd.nodes.PropertyNode('range', '10.0.0.11 10.0.0.50', None))
new_node.children.append(child_node)
child_node = (pyisc.dhcpd.nodes.Node('pool', None, None))
child_node.children.append(pyisc.dhcpd.nodes.PropertyNode('allow', 'members of "allocation-class-2"', None))
child_node.children.append(pyisc.dhcpd.nodes.PropertyNode('range', '10.0.0.51 10.0.0.100', None))
new_node.children.append(child_node)
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('subclass', '"allocation-class-2"', '1:08:00:2b:a1:11:31'))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('option root-path', '"samsara:/var/diskless/alphapc"', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('filename', '"/tftpboot/netbsd.alphapc-diskless"', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('class', '"customer"', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('spawn', 'with option agent.circuit-id', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('lease limit', '4', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('class', '"jr-cable-modems"', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('match', 'if option dhcp-vendor-identifier = "jrcm"', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('spawn', 'with option agent.circuit-id', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('lease limit', '4', None))
expected_dhcpd.children.append(new_node)

new_node = (pyisc.dhcpd.nodes.Node('class', '"dv-dsl-modems"', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('match', 'if option dhcp-vendor-identifier = "dvdsl"', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('spawn', 'with option agent.circuit-id', None))
new_node.children.append(pyisc.dhcpd.nodes.PropertyNode('lease limit', '16', None))
expected_dhcpd.children.append(new_node)
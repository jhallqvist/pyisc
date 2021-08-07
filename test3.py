from pyisc.dhcpd.parsing import DhcpdParser

parser = DhcpdParser()

with open('old_tests/dhcpd2.conf', 'r') as infile:
    conf = infile.read()

temp = parser.construct_tree(conf)

print(temp.to_isc())

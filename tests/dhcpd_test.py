"""TEMP."""


from .dhcpd_vars import expected_dhcpd
import pathlib
import unittest
from pyisc import dhcpd, shared


class TestStringToTree(unittest.TestCase):
    def setUp(self):
        data_folder = pathlib.Path(__file__).parent.parent.joinpath('data')
        dhcpd_file = data_folder.joinpath('dhcpd-classes.conf')
        self.testfile = open(dhcpd_file)
        self.testdata = self.testfile.read()

    def tearDown(self):
        self.testfile.close()

    def test_load_function(self):
        isc_tree = dhcpd.loads(self.testdata)
        self.assertIsInstance(isc_tree, shared.nodes.RootNode)
        self.assertEqual(isc_tree, expected_dhcpd)
        self.assertEqual(len(isc_tree.children), 12)


class TestTokenization(unittest.TestCase):
    def setUp(self):
        self.parser = dhcpd.parsing.DhcpdParser()
        self.parameter_string = 'max-lease-time 86400;'
        self.option_string = 'option domain-name-servers 1.1.1.1, 2.2.2.2;'
        self.declaration_string = 'subnet 10.0.0.0 netmask 255.255.255.0 {'

    def test_tokenization(self):
        parameter_token = self.parser.tokenize(self.parameter_string)
        expected_paramater = [
            shared.parsing.Token(
                type='parameter_general',
                value='max-lease-time 86400;')]
        self.assertEqual(parameter_token, expected_paramater)
        option_token = self.parser.tokenize(self.option_string)
        expected_option = [
            shared.parsing.Token(
                type='parameter_option',
                value='option domain-name-servers 1.1.1.1, 2.2.2.2;')]
        self.assertEqual(option_token, expected_option)
        declaration_token = self.parser.tokenize(self.declaration_string)
        expected_declaration = [
            shared.parsing.Token(
                type='declaration_general',
                value='subnet 10.0.0.0 netmask 255.255.255.0 {')]
        self.assertEqual(declaration_token, expected_declaration)


class TestInsertIntoTree(unittest.TestCase):
    def setUp(self):
        self.original_string = 'subnet 10.152.187.0 netmask 255.255.255.0 {\n}'
        self.modified_string = 'subnet 10.152.187.0 netmask 255.255.255.0 ' + \
            '{\n    option domain-name-servers ns1.example.org, ' + \
            'ns2.example.org;\n}\n'

    def test_modify_tree(self):
        tree = dhcpd.loads(self.original_string)
        new_prop = shared.nodes.PropertyNode(
            type='option domain-name-servers',
            value='ns1.example.org, ns2.example.org')
        tree.children[0].children.append(new_prop)
        self.new_string = dhcpd.dumps(tree)
        self.assertEqual(self.modified_string, self.new_string)


if __name__ == '__main__':
    unittest.main()

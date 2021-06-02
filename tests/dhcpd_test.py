import unittest
import inspect
from .dhcpd_vars import expected_dhcpd
from pyisc import dhcpd, shared


class TestStringToTree(unittest.TestCase):
    def setUp(self):
        dhcpd_file = 'tests/data/dhcpd-classes.conf'
        self.testfile = open(dhcpd_file, 'r')
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


class TestParsingConfFile(unittest.TestCase):
    def setUp(self):
        conf_reference_file = 'data/dhcpd_ref-conf.conf'
        self.conf_file = open(conf_reference_file, 'r')
        self.confdata = self.conf_file.read()
        reference_file = 'data/dhcpd_ref-conf.md'
        self.ref_file = open(reference_file, 'r')
        self.refdata = self.ref_file.read()
        self.parser = dhcpd.parsing.DhcpdParser()
        self.reference_head = inspect.cleandoc('''# DHCPd statements

        | Original statement | Key | Value | Optional/Parameter |
        | :----------------- | :-- | :---- | :----------------- |
        ''') + '\n'

    def tearDown(self):
        self.conf_file.close()
        self.ref_file.close()

    def test_parse_equality(self):
        result = ''
        result += self.reference_head
        conf_splitted = self.confdata.splitlines()
        for row in conf_splitted:
            if not row.startswith('#'):
                node = self.parser.build_tree(row).children[0]
                joined_str = "|".join(
                    [str(x) for x in [node.type, node.value, node.parameters]])
                final_string = "|" + "|".join((row, joined_str)) + "|" + '\n'
                result += final_string
        self.assertEqual(self.refdata, result)


if __name__ == '__main__':
    unittest.main()

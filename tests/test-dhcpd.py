"""TEMP."""

"""
* test tokenize
* test modifying tree
"""

from context import pyisc, data_folder
import unittest


class TestStringToTree(unittest.TestCase):
    def setUp(self):
        dhcpd_file = data_folder.joinpath('dhcpd-classes.conf')
        self.testfile = open(dhcpd_file)
        self.testdata = self.testfile.read()

    def tearDown(self):
        self.testfile.close()

    def test_load_function(self):
        isc_tree = pyisc.dhcpd.loads(self.testdata)
        self.assertIsInstance(isc_tree, pyisc.dhcpd.nodes.RootNode)


if __name__ == '__main__':
    unittest.main()

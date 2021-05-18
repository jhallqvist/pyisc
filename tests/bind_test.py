"""TEMP."""

from .bind_vars import expected_bind
import pathlib
import unittest
from pyisc import bind, shared


class TestStringToTree(unittest.TestCase):
    def setUp(self):
        data_folder = pathlib.Path(__file__).parent.parent.joinpath('data')
        bind_file = data_folder.joinpath('named-example1.conf')
        self.testfile = open(bind_file)
        self.testdata = self.testfile.read()

    def tearDown(self):
        self.testfile.close()

    def test_load_function(self):
        isc_tree = bind.loads(self.testdata)
        self.assertIsInstance(isc_tree, shared.nodes.RootNode)
        self.assertEqual(isc_tree, expected_bind)
        self.assertEqual(len(isc_tree.children), 6)

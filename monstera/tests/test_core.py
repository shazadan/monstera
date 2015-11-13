__author__ = 'shazada nawaz'

import unittest

from monstera.core import MLObject

class TestMLObject(unittest.TestCase):

    def test_instantiate_without_csv(self):
        self.failUnlessRaises(TypeError, MLObject)

    def test_instantiate_with_non_csv(self):
        pass

    def test_instantiate_with_csv(self):
        pass

    def test_instantiate_where_csv_has_header(self):
        pass

    def test_instantiate_where_csv_has_no_header(self):
        pass
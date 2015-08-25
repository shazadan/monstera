__author__ = 'shazada nawaz'

import unittest

from monstera.core import MLObject

class TestCorePackage(unittest.TestCase):

    def test_MLObject_instantiate_without_csv(self):
        ml = MLObject()

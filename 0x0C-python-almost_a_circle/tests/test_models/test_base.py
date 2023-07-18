#!/usr/bin/python3
""" Unittests for base.py """

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Defines a Class that runs tests fo base.py """
    #Test one
    def test_instance_type(self):
        """ Checks if id is a clasz instance """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b1.id, int)
        self.assertEqual(type(b1), Base)
        self.assertEqual(b1, b1)
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertIsInstance(b2, Base)
        self.assertIsInstance(b2.id, int)
        self.assertEqual(type(b2), Base)
        self.assertEqual(b2, b2)
        self.assertNotEqual(b1, b2)

    #Test two
    def test_inheritance(self):
        """ Checks inheritance from base """
        class Derived(Base):
            """Empty"""
            pass
        d1 = Derived()
        d2 = Derived()
        self.assertIsInstance(d1, Base)
        self.assertTrue(type(d1) == type(d2))
        self.assertFalse(id(d1) == id(d2))

if __name__ == '__main__':
    unittest.main

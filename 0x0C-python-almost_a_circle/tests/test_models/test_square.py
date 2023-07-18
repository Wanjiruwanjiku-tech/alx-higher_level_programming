#!/usr/bin/python3
""" Test Cases for square.py """

# import modules
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class SquareTestCases(Square):
    """ Class to evaluate Test Cases """

    def test_class_instance(self):
        """ Test class instances """
        s1 = Square(12)
        self.assertIsInstance(s1, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(id(Square) != id(Rectangle)
        self.assertTrue(id(Square) != id(Base)
        self.assertTrue(type(Square) == type(Rectangle)
        self.assertTrue(type(Square) ==type(Base)

        s2 = Square(10)
        self.assertTrue(type(s1) == type(s2)
        self.assertFalse(id(s1) == id(s2


    def test_area(self):
        """ Test area calculation """
        sq1 = Square(20)
        area = sq1.area()
        self.assertEqual(area, 400)

        sq2 = Square(5, 5)
        area = sq2.area()
        self.assertEqual(area, 25)

        sq3 = Square(3, 4, 6, 8)
        area = sq3.area
        self.assertEqual(area, 6)

if __name__ == '__main__':
    unittest.main()

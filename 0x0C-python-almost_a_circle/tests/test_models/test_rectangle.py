#!/usr/bin/python3
"""This Mofule runs tests for the module
rectangle.py
"""
# Import Modules

import unittest
from models.rectangle import Rectangle

class RectangleTestCases(Rectangle):
    """ A class to evaluate different test cases """
    def test_area_calculation(self):
        """ Test the area calculation """
        r = Rectangle(5, 9)
        self.assertEqual(r.area(), 45)

        r1 = Rectangle(12, 10)
        my_area = r1.area()
        self.assertEqual(my_area, 120)

    def test_class_instance(self):
        """ Check if Rectangle is a subclass of Base """
        rect1 = Rectangle(4, 6)
        self.assertIsInstance(rect1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))

        rect2 = Rectangle(10, 8)
        self.assertTrue(type(rect1) == type(rect2))
        self.assertFalse(id(rect1) == id(rect2))

if __name__ == '__main__':
    unittest.main()

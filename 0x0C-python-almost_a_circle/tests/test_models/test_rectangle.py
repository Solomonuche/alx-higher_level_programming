#!/usr/bin/python3
""" Test_rectangle unit test"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit testing Rectangle class"""

    def test_RectangleNormalOperation(self):
        """Test for norning class opeartion and assignment"""

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r1.id

        r2 = Rectangle(2, 10)
        r2.id

        r3 = Rectangle(10, 2, 0, 0, 12)
        r3.id

        """Assert"""
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_rectAssertRaises(self):
        """ Test that appropriate error are raised"""

        """Assert height"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        """Assert width"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        """Assert x"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        """Assert y"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

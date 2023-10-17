#!/usr/bin/python3
""" Test_base unit test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit testing Basse class"""

    def test_BaseNormalOperation(self):
        """Test for norning class opeartion and assignment"""

        b1 = Base()
        b1.id

        b2 = Base()
        b2.id

        b3 = Base()
        b3.id

        b4 = Base(12)
        b4.id

        b5 = Base()
        b5.id

        """Assert"""
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def base_instance(x, y, z):
        return Base(x, y, z)

    def test_Base_withMoreThan1Argument(self):
        """ Test for when more than one argument is passed"""

        """ Assert raises"""
        self.assertRaises(TypeError, self.base_instance, 2, 3, 4)

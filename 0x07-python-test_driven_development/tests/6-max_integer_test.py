#!/usr/bin/python3
"""
Unit test for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test calss for max_integer"""

    def test_emptyList(self):
        """Test case for empty list"""

        self.assertIsNone(max_integer(list=[]))

    def test_normal_max_integer_operation(self):
        """Test cases for normal function operation"""

        a = [1, 2, 3, 4]
        b = [-1, -3, -4, -2]
        c = [1, 3, 4, -2]
        d = [2]

        self.assertEqual(max_integer(a), 4)
        self.assertEqual(max_integer(b), -1)
        self.assertEqual(max_integer(c), 4)
        self.assertEqual(max_integer(d), 2)

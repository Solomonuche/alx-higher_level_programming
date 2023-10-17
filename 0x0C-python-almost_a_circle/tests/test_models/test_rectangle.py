#!/usr/bin/python3
""" Test_rectangle unit test"""
import unittest
from unittest.mock import patch
import io
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

    def test_Area(self):
        """ Unittest for area of a rectangle class"""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        """Test display method"""

        r1 = Rectangle(4, 6)
        r1.display()

        printed_output = mock_stdout.getvalue()

        expected_output = "####\n####\n####\n####\n####\n####\n"

        self.assertEqual(printed_output, expected_output)

        """ Test display method with x, y parameter"""
        """reset the mock_stdout"""

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        r2 = Rectangle(2, 3, 2, 2)
        r2.display()

        printed_output = mock_stdout.getvalue()

        expected_output = "\n\n  ##\n  ##\n  ##\n"

        self.assertEqual(printed_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        """Test __str__ method"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)

        printed_output = mock_stdout.getvalue()

        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"

        self.assertEqual(printed_output, expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update(self, mock_stdout):
        """Test update method"""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        print(r1)

        printed_output = mock_stdout.getvalue()

        expected_output = "[Rectangle] (89) 10/10 - 10/10\n"

        self.assertEqual(printed_output, expected_output)

        """ Test update method with **kwargs parameter"""
        """reset the mock_stdout"""

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, id=89)
        print(r1)

        printed_output = mock_stdout.getvalue()

        expected_output = "[Rectangle] (89) 1/3 - 4/2\n"

        self.assertEqual(printed_output, expected_output)

#!/usr/bin/python3
""" Unite test Module for Square class"""
import io
import unittest
from unittest.mock import patch
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """ Unit testing of different parameter and methods of Square class"""

    def test_square_str(self):
        """ test Str method"""

        with patch("sys.stdout", new_callable=io.StringIO) as mocked_obj:
            Base._Base__nb_objects = 0
            s1 = Square(5)
            print(s1)

            printed_value = mocked_obj.getvalue()
            expected_value = "[Square] (1) 0/0 - 5\n"

            self.assertEqual(printed_value, expected_value)

            """Reset Mocked object in order to save new outputs"""
            mocked_obj.truncate(0)
            mocked_obj.seek(0)

            Base._Base__nb_objects = 0
            s1 = Square(5)
            s1.size = 10
            print(s1)

            printed_value = mocked_obj.getvalue()
            expected_value = "[Square] (1) 0/0 - 10\n"

            self.assertEqual(printed_value, expected_value)

    def test_square_size(self):
        """ test size attribute method"""

        with patch("sys.stdout", new_callable=io.StringIO) as mocked_obj:
            Base._Base__nb_objects = 0
            s1 = Square(5)
            print(s1.size)

            printed_value = mocked_obj.getvalue()
            expected_value = "5\n"

            self.assertEqual(printed_value, expected_value)

    def test_square_assertRaises(self):
        """ validate that appropriate exception are raised"""

        with self.assertRaises(TypeError):
            s1 = Square(5)
            s1.size = "9"

    def test_square_area(self):
        """ Assert Square area method"""

        s1 = Square(5)
        self.assertEqual(25, s1.area())

    def test_square_display(self):
        """ assert square display method"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock:
            s1 = Square(5)
            s1.display()

            printed_value = mock.getvalue()
            expected_value = "#####\n#####\n#####\n#####\n#####\n"

            self.assertEqual(printed_value, expected_value)

    def test_square_update(self):
        """Test Square update method"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock:
            Base._Base__nb_objects = 0
            s1 = Square(5)
            s1.update(10)
            print(s1)

            printed_value = mock.getvalue()
            expected_value = "[Square] (10) 0/0 - 5\n"

            self.assertEqual(printed_value, expected_value)

            """Reset Mocked object in order to save new outputs"""
            mock.truncate(0)
            mock.seek(0)

            s1 = Square(5)
            s1.update(size=7, id=89, x=12, y=1)
            print(s1)

            printed_value = mock.getvalue()
            expected_value = "[Square] (89) 12/1 - 7\n"

            self.assertEqual(printed_value, expected_value)

    def test_square_to_dictionary(self):
        """Test Square instance to dictionary representation"""

        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()

        expected_value = {'id': 1, 'x': 2, 'size': 10, 'y': 1}

        self.assertEqual(s1_dictionary, expected_value)

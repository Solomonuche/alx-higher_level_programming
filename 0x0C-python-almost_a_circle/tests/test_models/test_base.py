#!/usr/bin/python3
""" Test_base unit test"""
import unittest
import json
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


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

    def test_base_to_json_string(self):
        """TEST Dictionary to JSON string"""

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        parsed_json = json.loads(json_dictionary)
        expected_dict = json.loads(expected)

        json_dictionary1 = Base.to_json_string([])

        expected_output1 = '[]'

        self.assertEqual(json_dictionary1, expected_output1)
        self.assertEqual(parsed_json, expected_dict)

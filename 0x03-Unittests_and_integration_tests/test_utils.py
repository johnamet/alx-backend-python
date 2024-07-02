#!/usr/bin/env python3
"""
Test cases for the utils module
"""
import unittest
from parameterized import parameterized, parameterized_class

utils = __import__("utils")
access_nested_map = utils.access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    """
    Test cases for the utils module
    """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b":2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, mapping, path, expected_value):
        self.assertEqual(access_nested_map(mapping, path), expected_value)




#!/usr/bin/env python3
""" Unit Test and Integration Test"""

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test access_nested_map """
    # parameter value
    # nested_map={"a": 1}, path=("a",)
    # nested_map={"a": {"b": 2}}, path=("a",)
    # nested_map={"a": {"b": 2}}, path=("a", "b")
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test exception access_nested_map """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test memoize """

    def test_memoize(self):
        """ Test memoize """
        class TestClass:
            """ Test class """

            def a_method(self):
                """ Test a_method """
                return 42

            @memoize
            def a_property(self):
                """ a property method"""
                return self.a_method()
        test_obj = TestClass()
        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            result1 = test_obj.a_property
            result2 = test_obj.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()

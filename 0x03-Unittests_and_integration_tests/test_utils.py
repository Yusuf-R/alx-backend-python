#!/usr/bin/env python3
""" Unit Test and Integration Test"""

import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map

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
    ({"a": 1}, ("a","b"))     
  ])
  def test_access_nested_map_exception(self, nested_map, path):
    """ Test exception access_nested_map """
    with self.assertRaises(KeyError):
      access_nested_map(nested_map, path)



if __name__ == "__main__":
  unittest.main()
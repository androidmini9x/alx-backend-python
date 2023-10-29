#!/usr/bin/env python3
'''Unit Test for verifying the work of
utils functions.
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Dict,
    Union
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    '''
    Test class unit the has all testing function
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]) -> None:
        '''Test access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence) -> None:
        '''Test access_nested_map_exception'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Testing implementation for get json'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict
    ) -> None:
        '''Test get json method'''
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload

        with patch('requests.get', return_value=mock_resp) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''Unit test for Memoize methods'''

    def test_memoize(self) -> None:
        '''Test memoize function'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42) as memo:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo.assert_called_once()

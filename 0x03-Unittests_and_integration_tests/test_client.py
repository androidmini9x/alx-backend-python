#!/usr/bin/env python3
'''Unit Test for verifying the work of
client functions.
'''
import unittest
from unittest.mock import (
    patch,
    MagicMock,
    PropertyMock
)
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''Class block contain all test method'''

    @parameterized.expand([
        ("google", {"repo": "google"}),
        ("abc", {"repo": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, resp, mock_read):
        '''Test org function'''
        mock_read.return_value = MagicMock(return_value={"repo": org_name})
        git_client = GithubOrgClient(org_name)
        self.assertEqual(git_client.org(), resp)
        mock_read.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )

    @parameterized.expand([
        ('user', {'repos_url': 'http://exmaple.com'})
    ])
    def test_public_repos_url(self, acct, resp):
        '''5. Mocking a property'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock(return_value=resp)) as mk:
            self.assertEqual(GithubOrgClient(acct)._public_repos_url,
                             resp.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        '''Test: public_repos function'''
        test_payload = [
            {"id": 23, "name": "project!"},
            {"id": 52, "name": "proj32"}
        ]
        mock_json.return_value = test_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mk:
            mk.return_value = 'http://exmaple.com'
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            check = [i["name"] for i in test_payload]

            self.assertEqual(result, check)
            mk.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''Test has license function'''
        has_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(has_license, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Test Integration for methods'''

    @classmethod
    def setUpClass(cls):
        config = {
            'return_value.json.side_effect': [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        '''Test public repos method'''
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        '''Test public with_license repos method'''
        test_class = GithubOrgClient("google")
        self.assertEqual(
            test_class.public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls):
        '''Clean fixtures after running all tests'''
        cls.get_patcher.stop()

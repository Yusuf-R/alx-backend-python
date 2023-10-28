#!/usr/bin/env python3
""" Unit Test and Integration Test"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
GithubOrgClient = __import__('client').GithubOrgClient
utils = __import__('utils')
client = __import__('client')


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        dict_ = {"payload": True}
        mock_get_json.return_value = dict_
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, dict_)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            dict_ = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            mock_org.return_value = dict_
            test_client = GithubOrgClient('google')
            self.assertEqual(test_client._public_repos_url, dict_['repos_url'])
            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
""" Unit Test and Integration Test"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock

GithubOrgClient = __import__("client").GithubOrgClient
utils = __import__("utils")
client = __import__("client")


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        dict_ = {"payload": True}
        mock_get_json.return_value = dict_
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, dict_)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test public_repos_url method"""
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            dict_ = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock_org.return_value = dict_
            test_client = GithubOrgClient("google")
            self.assertEqual(test_client._public_repos_url, dict_["repos_url"])
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ set up mock_get_json """
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        # using context manager for the mock_repo_url
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            url = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = url

            # Create an instance of GithubOrgClient
            test_client = GithubOrgClient("google")

            # Call the method being tested
            repos = test_client.public_repos()

            # Assert the returned list of repos is what you expect
            self.assertEqual(repos, ["repo1", "repo2"])

            # Assert that the mocks were called exactly once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()

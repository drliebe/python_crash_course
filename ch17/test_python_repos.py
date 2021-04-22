import unittest

from python_repos import get_repo_list, get_repo_dicts

class TestPythonRepos(unittest.TestCase):
    """Tests for 'python_repos.py'."""

    def test_get_repo_list(self):
        """Is the status code returned 200?"""
        r = get_repo_list()
        self.assertEqual(r.status_code, 200)


    def test_get_repo_dicts(self):
        """Is the number of repositories returned greater than 0?"""
        r = get_repo_list()
        repo_dicts = get_repo_dicts(r)
        self.assertGreater(len(repo_dicts), 0)

unittest.main()
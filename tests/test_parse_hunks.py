import unittest
import imp

git_af = imp.load_source("git_af", "git-af")


class TestSomeFunction(unittest.TestCase):
    def test_parse_hunks(self):
        git_af.parse_hunks("tests/hunk.diff")
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()

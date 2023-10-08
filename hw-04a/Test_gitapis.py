import unittest
from git_apis import getCommits,getRepos

class TestGit(unittest.TestCase):
    
    def test_getCommits(self):
        result = getCommits("Ashayp", "HelloWorld")
        self.assertEqual(result, 8)

    def test_checkgitapistate(self):
        result = getRepos("Ashayp")
        self.assertGreater(len(result), 0)

    def test_getCommits(self):
        result = getCommits("ahsgdkeh", "ahsjdgs")
        self.assertNotEqual(result, 1)
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
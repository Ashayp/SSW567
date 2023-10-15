import unittest
from unittest.mock import patch
from git_apis import getCommits,getRepos

class TestGit(unittest.TestCase):

    @patch('git_apis.requests.get')
    def test_getCommits(self, mocks_req):
        mocks_req.status_code = 200
        mocks_req.json.return_value =  [{'commit' : {"message": "Merge branch"}}, {'commit' : {"message": ""}}, {'commit' : {"message": ""}}, {'commit' : {"message": ""}}, {'commit' : {"message": ""}}, {'commit' : {"message": ""}}, {'commit' : {"message": ""}}, {'commit' : {"message": ""}}]
        mocks_req.side_effect = [mocks_req]
        result = getCommits("Ashayp", "HelloWorld")        
        self.assertEqual(result, 8)

    @patch('git_apis.requests.get')
    def test_checkgitapistate(self, mocks_req):        #should not be mocked as it defeats the purpose of this test, but done for the sake of completion
        mocks_req.status_code = 200
        mocks_req.json.return_value = [{"name": 'Ashayp'}, {"name": 'HelloWorld'}]
        mocks_req.side_effect = [mocks_req]
        result = getRepos("Ashayp")        
        self.assertGreater(len(result), 0)

    @patch('git_apis.requests.get')
    def test_getCommits2(self, mocks_req):
        mocks_req.status_code = 200
        mocks_req.json.return_value =  []
        mocks_req.side_effect = [mocks_req]
        result = getCommits("ahsgdkeh", "ahsjdgs")
        self.assertNotEqual(result, 1)
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
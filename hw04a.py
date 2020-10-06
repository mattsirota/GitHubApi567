#Matt Sirota
#SSW-567 HW05a

import unittest
import requests
import json
from unittest import mock

mock_results = ["Input is Invalid", "User does not exist", {"csp":2, "hellogitworld":30, "helloworld":6, "Mocks":10, "Project1":2, "richkempinski.github.io":9, "threads-of-life":1, "try_nbdev":2, "try_nbdev2":5}]

def getGitHubInfo(userID):
    if (userID == None):
        return "Input is Invalid"
    r = requests.get("https://api.github.com/users/" + userID + "/repos")
    repoList = r.json()

    if ("message" in repoList and repoList["message"] == "Not Found"):
        return "User does not exist"

    repoDict = {}

    for repo in repoList:
        r = requests.get("https://api.github.com/repos/" + userID + "/" + repo["name"] + "/commits")
        commitList = r.json()
        numCommits = len(commitList)
        repoDict[repo["name"]] = numCommits
    
    return repoDict

class TestGitHubAPI(unittest.TestCase):
    maxDiff = None

    @mock.patch(__name__+'.getGitHubInfo', return_value = mock_results[0])
    @mock.patch('requests.get')
    def testInvalidInput(self, mock_result, mock_request):
        self.assertEqual(getGitHubInfo(None), "Input is Invalid")
    
    @mock.patch(__name__+'.getGitHubInfo', return_value = mock_results[1])
    @mock.patch('requests.get')
    def testInvalidID(self, mock_result, mock_request):
        mock_request.return_value = mock_results[1]
        self.assertEqual(getGitHubInfo("ThisIsAnInvalidID123456789"), "User does not exist")

    @mock.patch(__name__+'.getGitHubInfo', return_value = mock_results[2])
    @mock.patch('requests.get')
    def testRichkempinkskiKeysAndValues(self, mock_result, mock_request):
        mock_request.return_value = mock_results[2]
        self.assertEqual(getGitHubInfo("richkempinkski"), mock_results[2])

if __name__ == '__main__':
    unittest.main(exit=True)


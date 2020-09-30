#Matt Sirota
#SSW-567 HW04a

import unittest
import requests
import json

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
    def testInvalidInput(self):
        self.assertEqual(getGitHubInfo(None), "Input is Invalid")
    def testInvalidID(self):
        self.assertEqual(getGitHubInfo("ThisIsAnInvalidID123456789"), "User does not exist")
    def testRichkempinkskiKeysAndValues(self):
        self.assertEqual(getGitHubInfo("richkempinski"), {"csp":2, "hellogitworld":30, "helloworld":6, "Mocks":10, "Project1":2, "richkempinski.github.io":9, "threads-of-life":1, "try_nbdev":2, "try_nbdev2":5})

if __name__ == '__main__':
    unittest.main(exit=True)


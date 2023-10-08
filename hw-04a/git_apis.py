import requests
import json

def getRepos(username):
    result = requests.get(f"https://api.github.com/users/{username}/repos").json()
    ret = []    
    for i in result:
        try:
            ret.append(i["name"])
        except:
            ret = []
         
    return ret

def getCommits(username, repo):          
    URL = f"https://api.github.com/repos/{username}/{repo}/commits"
    commits = requests.get(URL).json()
    number = len(commits)

    return number
        


user = "Ashayp"
Repos = getRepos(user) 
print("Username: " + user)
for i in Repos:              
    number = getCommits(user, i)
    print("Repo: " + i + " Number of Commits: " + str(number))
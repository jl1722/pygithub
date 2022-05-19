from tkinter import PAGES
from unicodedata import name
from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time
from datetime import datetime
import config
import requests



from github import Github
#import github
#import time

"""
def findPullBylabel(repo = None, labelName = 'hacktoberfest'):
    if(labelName is None or repo is None):
        raise DemoException("Error in Parameters")
    #---------------------------------------
    labels = repo.get_labels()
    pulls = repo.get_pulls(state = 'close')#, sort='created', base='master')
    lista = []
    for label in labels:
        if labelName in label.name:
            #lista.append(label)
            print("Label: ", label.name)
            for pr in pulls:
                #time.sleep(0.1)
                for labelx in pr.labels:
                    #print(pr.number)
                    if label.name in labelx.name:
                        print("\tpull number: ", pr.number)
                        lista.append(pr)
    return lista
"""

"""
def get_issue_By_Label(repo,nome):

        #curl 'https://api.github.com/repos/travis-ci/travis-ci/issues?labels=bug;state=closed'

        #api.github.com/repos/{owner}/{repo}/issues?labels=hacktoberfest-accepted?state=closed
        #print(repo._requester)
        #url = f"{repo.url}/issues?labels={nome};state=closed"
        url = f"/issues?labels={nome};state=closed"
        #print(url)
        return github.PaginatedList.PaginatedList(
            github.Issue.Issue, repo._requester, url, None
        )
"""

access_token = config.get_access_token()
g = Github(access_token, per_page=300)
print(g.rate_limiting)

topic = 'hacktoberfest'
labelName = "hacktoberfest"

repos = g.search_repositories(query=f'topic:{topic}')
for repo in repos:
    print(repo.name)

    labels = repo.get_labels()

    for lab in labels:
        #print("\t",lab.name)
        if labelName in lab.name:
            #https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.get_issues
            issues = repo.get_issues(state='all', labels = [lab])
            for issue in issues: #https://pygithub.readthedocs.io/en/latest/github_objects/Issue.html#github.Issue.Issue
                if issue is None:
                    continue
                try:
                    pull = issue.as_pull_request() #https://pygithub.readthedocs.io/en/latest/github_objects/PullRequest.html#github.PullRequest.PullRequest
                except:
                    print("An exception occurred")
                    continue
                if pull is None:
                    continue
                commits = pull.get_commits() #https://pygithub.readthedocs.io/en/latest/github_objects/Commit.html#github.Commit.Commit
                commitsUser = []
                for commit in commits:
                    if commit.author not in commitsUser:
                        commitsUser.append(commit.author)
                        print("\t\t",commit.author)
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
access_token = config.get_access_token()
df_issues = pd.DataFrame()
while True:
    try:
        g = Github(access_token, retry=10, timeout=15, per_page=300)
        print(g.rate_limiting)
        topic = 'hacktoberfest'
        labelName = ["hacktoberfest"]
        repos = g.search_repositories(query=f'topic:{topic}')
        for repo in repos:
            try:
                repoName = repo.name
                print(repoName)
                issues = repo.get_issues(state='closed', sort='created',labels=labelName)
                for issue in issues:
                    print(issue)
                    issue_comments = []
                    for comment in issue.get_comments():
                        cmt = {
                            'user': comment.user.name,
                            'user_id': comment.user.id,
                            'user_site_admin': comment.user.site_admin,
                            'body': comment.body
                        }
                        issue_comments.append(cmt)
                        print(issue.id)
                        print(issue.pull_request)

                    df_issues = df_issues.append({
                        'issue_id': issue.id,
                        'issue_number': issue.number, # issue features
                        'issue_labels': [l.name for l in issue.labels],
                        'issue_title': issue.title,
                        'issue_body': issue.body,
                        'owner': issue.user.name if issue.user is not None else '', # Issue owner features
                        'owner_username': issue.user.login if issue.user is not None else '',
                        'followers': issue.user.followers,
                        'followings': issue.user.following,
                        'contributions': issue.user.contributions,
                        'stars': issue.user.get_starred().totalCount,
                        'issue_date': issue.created_at,
                        'issue_comments': issue_comments,
                        'issueORPR': issue.pull_request
                    }, ignore_index=True)
                    df_issues.to_csv('../Dataset/open_issues.csv', sep=',', encoding='utf-8', index=True)   



            
            except RateLimitExceededException as e:
                    print(e.status)
                    print('Rate limit exceeded')
                    time.sleep(300)
                    continue
            except BadCredentialsException as e:
                    print(e.status)
                    print('Bad credentials exception')
                    break
            except UnknownObjectException as e:
                    print(e.status)
                    print('Unknown object exception')
                    break
            except GithubException as e:
                    print(e.status)
                    print('General exception')
                    break
            except requests.exceptions.ConnectionError as e:
                    print('Retries limit exceeded')
                    print(str(e))
                    time.sleep(10)
                    continue
            except requests.exceptions.Timeout as e:
                    print(str(e))
                    print('Time out exception')
                    time.sleep(10)
                    continue

    except RateLimitExceededException as e:
        print(e.status)
        print('Rate limit exceeded')
        time.sleep(300)
        continue
    except BadCredentialsException as e:
        print(e.status)
        print('Bad credentials exception')
        break
    except UnknownObjectException as e:
        print(e.status)
        print('Unknown object exception')
        break
    except GithubException as e:
        print(e.status)
        print('General exception')
        break
    except requests.exceptions.ConnectionError as e:
        print('Retries limit exceeded')
        print(str(e))
        time.sleep(10)
        continue
    except requests.exceptions.Timeout as e:
        print(str(e))
        print('Time out exception')
        time.sleep(10)
        continue
    break
    


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


access_token = config.get_access_token()
access_token = "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"
resp = requests.get('https://api.github.com/users/BerkeleyTrue/events?page=0&per_page=10', headers={'Authorization': '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'})
data= resp.json#simple list of user_events
id = data[0]['id']#attribute called id the of the event at position 0 
def extract_user(user_id):
    df_PRs = pd.DataFrame()
    while True:
        try:
            



            g = Github(access_token, retry=10, timeout=15, per_page=100)#create object github of my github account
            user = g.get_user_by_id(user_id)#create object user do id
            print(f'ACcessing data from {user.name} ')
            
            try:
                print(g.rate_limiting)#object in format(a,b) a is the number of remaining request chance, b is the total number of request chance
                print(f'Extracting data from {user.name} ')
                    
                
                print(resp.json)
                

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
    df_PRs.to_csv('../Dataset/users_dataset_2.csv', sep=',', encoding='utf-8', index=True)

extract_user(6775919)
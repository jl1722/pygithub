from github import Github

access_token = "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"

g = Github(access_token, retry=20)

current_user = g.get_user()
print(current_user.name)
print(current_user.bio)

repos = g.get_user().get_repos()

for repo in repos:
    print(repo.name)

java_repos = g.search_repositories(query="language:java")

for repo in java_repos:
    print(repo.name)








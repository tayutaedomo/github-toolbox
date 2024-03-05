import os
import sys

from github import Github
from github.Repository import Repository


if __name__ == "__main__":
    g = Github(os.environ["GITHUB_TOKEN"])

    repo_name = sys.argv[1]
    repo = g.get_repo(repo_name)
    
    for issue in repo.get_issues(state="closed", assignee="me"):
        print(issue.title)

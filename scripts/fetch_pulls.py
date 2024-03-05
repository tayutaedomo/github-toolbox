import os
import sys

from github import Github


if __name__ == "__main__":
    g = Github(os.environ["GITHUB_TOKEN"])

    repo_name = sys.argv[1]

    repo = g.get_repo(repo_name)
    
    # Not found assignee parameter
    for pr in repo.get_pulls():
        title = pr.title
        state = pr.state
        assignee = pr.assignee.login if pr.assignee else ""
        created_at = pr.created_at.isoformat()
        closed_at = pr.closed_at.isoformat() if pr.state == "closed" else ""
        print("\t".join([title, state, assignee, created_at, closed_at]))

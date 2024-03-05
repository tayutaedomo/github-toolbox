import os
import sys

from github import Github


if __name__ == "__main__":
    g = Github(os.environ["GITHUB_TOKEN"])

    repo_name = sys.argv[1]
    assignee = sys.argv[2]

    repo = g.get_repo(repo_name)
    
    for issue in repo.get_issues(state="closed", assignee=assignee):
        title = issue.title
        state = issue.state
        item_type = "issue" if issue.pull_request is None else "pr"
        created_at = issue.created_at.isoformat()
        closed_at = issue.closed_at.isoformat() if issue.state == "closed" else ""
        print("\t".join([item_type, title, state, created_at, closed_at]))

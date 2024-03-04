from __future__ import annotations

import os

from github import Github
from github.Repository import Repository


def print_header(attr_names: tuple[str, ...]) -> None:
    names = [name.capitalize() for name in attr_names]
    print("\t".join(names))


def print_repository(repository: Repository, attr_names: tuple[str, ...]) -> None:
    values: list[str] = []
    for name in attr_names:
        value = getattr(repository, name)
        if value is None:
            values.append("")
        elif name == "created_at":
            values.append(value.isoformat())
        else:
            values.append(str(value))

    print("\t".join(values))


if __name__ == "__main__":
    # Ref: https://github.com/PyGithub/PyGithub#simple-demo
    g = Github(os.environ["GITHUB_TOKEN"])

    attr_names = ("name", "archived", "created_at", "description")

    print_header(attr_names)

    for repository in g.get_user().get_repos():
        print_repository(repository, attr_names)

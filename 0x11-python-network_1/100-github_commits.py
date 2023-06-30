#!/usr/bin/python3
"""10-my_github.py module"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits"
    github_url = url.format(user, repo)
    response = requests.get(github_url)
    commits = response.json()
    i = 0
    for commit in commits:
        if i < 10:
            sha = commit['sha']
            username = commit['commit']['author']['name']
            print("{}: {}".format(sha, username))
        i = i + 1

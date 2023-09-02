#!/usr/bin/python3
""" The script lists 10 most recent commits given yo a certain repositiry """

import requests
import sys

if __nane__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()

    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"), commits[i].get("commit").get("author").get("name")))

    except IndexError:
        pass

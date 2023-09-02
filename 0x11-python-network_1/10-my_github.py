#!/usr/bin/python3
""" The script takes my github credentials and uses github api to display my id """

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)

    print(req.json().get("id"))

#!/usr/bin/python3
"""
Uses the requests and sys packages to send a request and display the values
of a variable X-Request-Id
"""
from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""
The module takes a url and sends a request.
it then displays the value of X-Request-Id var found in the header response
"""
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        header_name = 'X-Request-Id'
        print(dict(response.headers).get(header_name))

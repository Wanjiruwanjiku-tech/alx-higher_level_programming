#!/usr/bin/python3
"""
The module takes a url and sends a request.
it then displays the value of X-Request-Id var found in the header response
"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    header_name = 'X-Request-Id'
    if header_name in response.headers:
        print(response.headers[header_name])
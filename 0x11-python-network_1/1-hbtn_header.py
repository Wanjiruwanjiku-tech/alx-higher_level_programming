#!/usr/bin/python3
""" The script takes in a url, sends a request and displays the value of X-Request-Id """

import urllib.request
import sys

if __name__  == "__main__":
	url = sys.argv[1]

	with urllib.request.urlopen(url) as response:
		header = response.info()
		print(header.get("X-Request-Id"))

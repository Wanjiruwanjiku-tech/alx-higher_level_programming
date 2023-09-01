#!/usr/bin/python3
""" The script uses a requests package """

import requests
import sys

if __name__ == "__main__":
	url = sys.argv[1]
	response = requests.get(url)
	header = response.headers.get("X-Request-Id")

	print(header)

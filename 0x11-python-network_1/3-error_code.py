#!/usr/bin/python3
""" manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code """

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
	url = sys.argv[1]

	try:
		with urllib.request.urlopen(url) as response:
			body = response.read()
			print(body.decode("utf-8"))

	except urllib.error.HTTPError as error:
		print("Error code: {}".format(error.code))

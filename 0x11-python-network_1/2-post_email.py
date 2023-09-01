#!/usr/bin/python3
""" The script takes in a url and an email, sends a post request and displays the response body """

import urllib.request
import urlib.parse
import sys

if __name__ == "__main__":
	url = sys.argv[1]
	email = sys.argv[2]

	data = urllib.parse.urlencode({"email": email}).encode("utf-8")
	req = urllib.request.Request(url, data)

	with urllib.request.urlopen(req) as resonse:
		body = response.read(
		print("Your email is: {}".format(body.decode('utf-8')))

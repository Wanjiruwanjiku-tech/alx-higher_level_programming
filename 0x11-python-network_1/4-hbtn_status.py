#!/usr/bin/python3
""" The script uses the requests package to fetch a ur """

import requests

if __name__ == "__main__":
	url = "https://alx-intranet.hbtn.io/status"
	response = requests.get(url)
	content = response.text

	print("Body response:")
	print("\t- type: {}".format(type(content)))
	print("\t- content: {}".format(content))

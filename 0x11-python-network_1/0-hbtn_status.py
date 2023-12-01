#!/usr/bin/python3
"""
This module runs a script that fetches a url using the urllib package
"""
# Import necessary modules
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    # Read the response body
    content = response.read()
    # Display the response body as stated
    print("Body response")
    print("\t- type:", type(content))
    print("\t- content:", content)
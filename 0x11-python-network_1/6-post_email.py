#!/usr/bin/python3
"""
Sends a post request with the email as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.post(argv[1], data={'email' : argv[2]})
    print(response.text)


#!/usr/bin/python3
"""
The module uses the requests package to fetch a url
And displays the response body
"""
import requests

if __name__ == "__main__":
    
    response = requests.get('https://alx-intranet.hbtn.io/status')
    decoded = response.content.decode('utf-8')

    print("Body response:")
    print("\t- type {}".format(type(decoded)))
    print("\t- content: {}".format(decoded))

#!/usr/bin/python3
"""
The module uses the urllib and sys packages to send a POST request
The first arg will be the url and the second is an email passed as a parameter
Decoded inutf-8
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":

    # Get the url and email
    url = sys.argv[1]
    email = sys.argv[2]

    # Set the values to encode
    values = {
    'email' : email
    }

    # Encode the values
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    # Fetch the url with a POST request
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print('Your email is: {}'.format(content))

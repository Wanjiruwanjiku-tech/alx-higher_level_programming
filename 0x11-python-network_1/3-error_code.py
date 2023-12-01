#!/usr/bin/python3
"""
The script manages errors
"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":

    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(response.read().decode("ascii"))  
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
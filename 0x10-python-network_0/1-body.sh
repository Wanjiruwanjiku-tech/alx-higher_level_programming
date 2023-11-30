#!/bin/bash
#The script takes in a url, sends a Get request and displays the body of the response
curl -s -X GET "$1" -o output.txt | cat output.txt
#!/bin/bash
#The script takes in a url, sends a Get request and displays the body of the response And sends info
curl -sL "$1" -H "X-School-User-Id:98"
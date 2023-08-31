#!/bin/bash
# The Script send the request to a url and displays the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
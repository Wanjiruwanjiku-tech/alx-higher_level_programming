#!/bin/bash
#The script displays all http methods the server will accept
curl -si --request OPTIONS "$1"

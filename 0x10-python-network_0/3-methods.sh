#!/bin/bash
#The script displays all http methods the server will accept
curl -sI "$1" | grep -i "Alow" | cut -d " " -f 2-

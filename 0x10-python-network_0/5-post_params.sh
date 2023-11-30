#!/bin/bash
#The script sends a post request and adds two variables wit their respective values
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
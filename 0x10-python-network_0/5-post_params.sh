#!/bin/bash
# Sends request to a URL using post and variables

# Store the URL argument
url="$1"

# data variable
email="test@gmail.com"
subject="I will always be here for PLD"

curl -sS -X POST -d "email=$email&subject=$subject" "$url"

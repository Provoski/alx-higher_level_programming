#!/bin/bash
# Sends a OPTIONS request a url

# Store the URL argument
url="$1"

# Display all the methods allowed of the http request
curl -sSI -X OPTIONS "$url" | awk '/^Allow/' | cut -d' ' -f2-

#!/bin/bash
# Sends request to a URL and print the size of the bod response

# Store the URL argument
url="$1"

# Send a request using curl and store the response body in a variable
response=$(curl -sSL -w "%{size_download}" -o /dev/null "$url")
echo $response

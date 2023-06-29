#!/bin/bash
# Sends a DELETE request

# Store the URL argument
url="$1"

# Send a request using curl and store the response body in a variable
curl -sSL -X DELETE "$url"

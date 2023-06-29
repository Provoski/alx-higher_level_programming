#!/bin/bash
# Sends request to a URL with a header variable

# Store the URL argument
url="$1"

header_value="98"
curl -sSL -H "X-School-User-Id: $header_value" "$url"

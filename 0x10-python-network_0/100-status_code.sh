#!/bin/bash
# Sends request to a URL and display only the status code
curl -sSL -w "%{http_code}" -o /dev/null "$1"

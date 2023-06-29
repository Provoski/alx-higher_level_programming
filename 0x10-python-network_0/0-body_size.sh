#!/bin/bash
# Sends request to a URL and print the size of the bod response
curl -sSL -w "%{size_download}\n" -o /dev/null "$1"

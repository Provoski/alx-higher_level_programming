#!/bin/bash
# Sends request to a URL with a header variable
curl -sSL -H "X-School-User-Id: 98" "$1"

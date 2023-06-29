#!/bin/bash
# Sends a OPTIONS request a url
curl -sSI -X OPTIONS "$1" | awk '/^Allow/' | cut -d' ' -f2-

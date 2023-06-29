#!/bin/bash
# senda a jason ppst requesst to a url
curl -sSL -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"

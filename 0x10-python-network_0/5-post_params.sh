#!/bin/bash
# Sends request to a URL using post and variables
curl -sS -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

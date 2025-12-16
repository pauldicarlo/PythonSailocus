#!/bin/bash
# @author: Paul DiCarlo
# @copyright: 2025 Paul DiCarlo
# @license: MIT
# @contact: https://github.com/pauldicarlo


export API_PATH=token


# TODO: Hide these better
PASSWORD=dingbat#17
USER_NAME=freddiano

# Execute curl using the substituted JSON file
curl -v -X POST "https://localhost:8000/${API_PATH}/" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=string&password=${PASSWORD}&scope=&client_id=string&client_secret=${PASSWORD}' \
  -H "Content-Type: application/json" \
  --cert certs/client.crt \
  --key certs/client.key \
  --cacert certs/ca.crt 



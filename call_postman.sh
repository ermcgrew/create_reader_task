#!/usr/bin/env bash

assign_to=$1
due_date=$2
include_tag=$3
protocol_id=$4

# echo In bash script to execute curl call to postman
# echo Assign task to "${assign_to}"
# echo Due date is "${due_date}"
# echo all files with tag "${include_tag}"
# echo protocol "${protocol_id}"

function get_data() {
  cat <<EOF
  {
    "assignees": ["${assign_to}"],
    "parent_type": "file",
    "project_id": "5c508d5fc2a4ad002d7628d8",
    "parent_tag_filter": {
      "include": ["${include_tag}"],
      "exclude": []
    },
    "viewer": "OHIF",
    "status": "Todo",
    "info": {},
    "config_overrides": {
    },
    "task_type": "R",
    "protocol_id": "${protocol_id}",
    "due_date": "${due_date}"
}
EOF
}


## load api key from log_in.py 
function get_api_key() {
  source ./log_in.py
  cat <<EOF 
Authorization: scitran-user upenn.flywheel.io:$api_key
EOF
}


curl --location 'https://upenn.flywheel.io/api/readertasks/batch' \
--header 'Content-Type: application/json' \
--header "$(get_api_key)" \
--data "$(get_data)"

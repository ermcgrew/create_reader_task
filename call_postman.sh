#!/usr/bin/env bash


assign_to=$1
due_date=$2
include_tag=$3
protocol_id=$4

# assign_to=emcgrew@upenn.edu
# due_date="2024-04-25T15:49:30.653Z"
# include_tag=ReadyforImageQC
# protocol_id="6478f22a6530585f6ee1284f"   ## T1 task

## protocol id's for T1, T2, Flair tasks
## ReadyforimageQC tag is only applied to T1 files right now

echo call_postman script running.
echo Assign task to "${assign_to}"
echo Due date is "${due_date}"
echo all files with tag "${include_tag}"
echo protocol "${protocol_id}"
echo

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

curl --location 'https://upenn.flywheel.io/api/readertasks/batch' \
--header 'Content-Type: application/json' \
--header 'Authorization: scitran-user upenn.flywheel.io:djE2DiqK-VNH1RtOrHDGHqguq_aco2KlwVDq_6qEugO5YXMWQB0s-R3oA' \
--data "$(get_data)"


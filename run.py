#!/usr/bin/env python
from datetime import datetime,timedelta
import flywheel
import json
import logging  
import subprocess
from log_in import api_key


## dictionary of {task_type:[postman protocol ID,tag to use for files that need this task]}
task_type_id_map = {"T1": ["6478f22a6530585f6ee1284f","PreferredT1"], 
                    "T2": ["6478f309f577c9ed0ad7816d","ReadyforImageQC"], 
                    "FLAIR": ["6478f1c6f577c9ed0ad7816c","ReadyforImageQC"]
                    }

def validate_user(assignee):
    fw = flywheel.Client(f"upenn.flywheel.io:{api_key}")
    try:
        project = fw.get_project('5c508d5fc2a4ad002d7628d8') #NACC-SC
    except flywheel.ApiException as e:
        print(f'Error: {e}')
    perm_list=project.permissions
    all_users=[user_dict["_id"] for user_dict in perm_list]
    if assignee not in all_users:
        return False
    else:
        return True
    

def main(context):
    config = context.config # from the gear context, get the config settings

    assign_to=config['assignee']
    if not validate_user(assign_to):
        log.warning(f"Assignee email invalid")
        raise ValueError("Assignee email not found in project")
    
    due_date=config['due_date']
    if not due_date:
        due_date_formatted = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        due_date_dt = datetime.strptime(due_date,"%Y-%m-%d") 
        due_date_formatted = due_date_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    task_type=config['task_type']
    protocol_id=task_type_id_map[task_type][0]
    include_tag=task_type_id_map[task_type][1]

    log.info(f"Calling postman to assign task with arguments: {assign_to}, {due_date_formatted}, {include_tag}, {protocol_id}")
    result=subprocess.run(["./call_postman.sh", assign_to,due_date_formatted,include_tag,protocol_id],\
                        capture_output=True,text=True)
    result_dict = json.loads(result.stdout)
    try:
        all_task_ids = [result_dict[i]['task_id'] for i in range(0,len(result_dict)) ]
        log.info(f"{len(result_dict)} tasks assigned, task ids: {all_task_ids}")
    except KeyError as e:
        log.warning(f'Error {e}: {json.loads(result.stderr)}')


if __name__ == "__main__": 
   # Initialize logging and set its level  
    logging.basicConfig()  
    log = logging.getLogger()  
    log.setLevel(logging.INFO)

    context = flywheel.GearContext() # Get the gear context  

    main(context)


#!/usr/bin/env python
from datetime import datetime,timedelta
import flywheel
import logging  
import subprocess
from log_in import api_key


## dictionary of {task_type:[postman protocol ID,tag to use for files that need this task]}
task_type_id_map = {"T1":["6478f22a6530585f6ee1284f","ReadyforImageQC"], 
                    "T2":["","ReadyforImageQC"], 
                    "FLAIR": ["","ReadyforImageQC"], 
                    "ASHS_T1":[], 
                    "ASHS_ICV":[]}
## TODO:protocols for T2, FLAIR, ASHS
## TODO:double-check T1 viewer config id in postman, not showing up

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

    log.info(f"Calling postman to assign task with arguments: {assign_to},{due_date_formatted},{include_tag},{protocol_id}")
    # result=subprocess.run(["./call_postman.sh", assign_to,due_date_formatted,include_tag,protocol_id],\
    #                     capture_output=True,text=True)
    # log.info(result)
    # log.info(result.stdout)
    ###TODO: How to parse result for useful logging
    # result_list = result.stdout.split("\n")
    # print(result_list)
    # print(result_list[-1])
    ## it's string that contains a list which is made up of dictionaries
    ## ideally want the "task_id" key from each dictionary 
    ## and a length of list for how many tasks created

if __name__ == "__main__": 
   # Initialize logging and set its level  
    logging.basicConfig()  
    log = logging.getLogger()  
    log.setLevel(logging.INFO)

    context = flywheel.GearContext() # Get the gear context  

    main(context)


#!/usr/bin/env python
from datetime import datetime
import flywheel
import logging  
import subprocess


## dictionary of {task_type:[postman protocol ID,tag to use for files that need this task]}
task_type_id_map = {"T1":["6478f22a6530585f6ee1284f","ReadyforImageQC"], 
                    "T2":["","ReadyforImageQC"], 
                    "FLAIR": ["","ReadyforImageQC"], 
                    "ASHS_T1":[], 
                    "ASHS_ICV":[]}
## TODO:protocols for T2, FLAIR, ASHS
## TODO:double-check T1 viewer config id in postman, not showing up


def main(context):
    config = context.config # from the gear context, get the config settings

    assign_to=config['assignee']
    ##TODO: in manifest? generate user list?
    
    due_date=config['due_date']
    if not due_date:
        current_date_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        due_date=current_date_time
    ##TODO: format to 2024-04-25T15:49:30.653Z
    ##TODO: if null, do current time + 1 week

    task_type=config['task_type']
    protocol_id=task_type_id_map[task_type][0]
    include_tag=task_type_id_map[task_type][1]


    # assign_to="emcgrew@upenn.edu"
    # due_date="2024-04-25T15:49:30.653Z"
    # protocol_id="6478f22a6530585f6ee1284f"
    # include_tag="ReadyforImageQC"

    log.info(f"Calling postman to assign task with arguments: {assign_to},{due_date},{include_tag},{protocol_id}")
    result=subprocess.run(["./call_postman.sh", assign_to,due_date,include_tag,protocol_id],\
                        capture_output=True,text=True)
    log.info(result)
    log.info(result.stdout)
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





#!/usr/bin/env python
import flywheel_gear_toolkit
import subprocess
import logging  
import flywheel

## dictionary of {task_type:[protocol ID,tag_to_base_on]}
task_type_id_map = {"T1":["6478f22a6530585f6ee1284f","ReadyforImageQC"], 
                    "T2":["","ReadyforImageQC"], 
                    "FLAIR": ["","ReadyforImageQC"], 
                    "ASHS_T1":[], 
                    "ASHS_ICV":[]}


# Initialize logging and set its level  
logging.basicConfig()  
log = logging.getLogger()  
log.setLevel(logging.INFO)

context = flywheel.GearContext() # Get the gear context  
config = context.config # from the gear context, get the config settings

print(context.config['task_type'])







# def main(gtk_context: flywheel_gear_toolkit.GearToolkitContext):
    # print(dir(gtk_context))
    # print(f"Using gtkcontext: {gtk_context.config.get('qc_type')}")

    # file_to_tag = gtk_context.get_input("file_to_qc")


    # assign_to="emcgrew@upenn.edu"

    # due_date="2024-04-25T15:49:30.653Z"

    # include_tag="ReadyforImageQC"
    # protocol_id="6478f22a6530585f6ee1284f" 

    # print('in main function')
    # result=subprocess.run(["./call_postman.sh", assign_to,due_date,include_tag,protocol_id],\
    #                     capture_output=True,text=True)

    # print(result.stdout)

    ###TODO: How to parse result for logging
    # result_list = result.stdout.split("\n")
    # print(result_list)
    # print(result_list[-1])
    # print(type(result_list[-1]))
    ## it's string that contains a list
    ## how to get it to be a list 
    # task_id key in dictionary in list
    # test='[{"_id":"662a833097099be7dec150d1","assignee":"emcgrew@upenn.edu","parent":{"id":"6617f4264aef0dfa0790d52b","type":"file","version":1},"parents":{"group":"dwolklab","project":"5c508d5fc2a4ad002d7628d8","subject":"6617f079d759966e00c0c53e","session":"6617f079d759966e00c0c53f","acquisition":"6617f4141de5b7b5be88a9d3","file":"6617f4264aef0dfa0790d52b","analysis":null},"status":"Todo","form_id":null,"viewer":"OHIF","viewer_config_id":null,"info":{},"config_overrides":{},"task_type":"R","batch_number":98,"batch_total_tasks":null,"item_number":1,"task_id":"R-98-1","protocol_id":"6478f22a6530585f6ee1284f","origin":{"type":"user","id":"emcgrew@upenn.edu"},"due_date":"2024-04-25T15:49:30.653000+00:00","created":"2024-04-25T16:22:08.597414+00:00","modified":"2024-04-25T16:22:08.597414+00:00","revision":1,"parent_tag_filter":{"include":["ReadyforImageQC"],"exclude":[]},"filters":null,"tags":[],"original_reader_task_id":null},{"_id":"662a833097099be7dec150d2","assignee":"emcgrew@upenn.edu","parent":{"id":"661d65e78eabdb1a6390d47b","type":"file","version":1},"parents":{"group":"dwolklab","project":"5c508d5fc2a4ad002d7628d8","subject":"5d02cc83a550c60048700a40","session":"661d62e658e7e6bfae88a938","acquisition":"661d65d99eebacff6ac0c570","file":"661d65e78eabdb1a6390d47b","analysis":null},"status":"Todo","form_id":null,"viewer":"OHIF","viewer_config_id":null,"info":{},"config_overrides":{},"task_type":"R","batch_number":98,"batch_total_tasks":null,"item_number":2,"task_id":"R-98-2","protocol_id":"6478f22a6530585f6ee1284f","origin":{"type":"user","id":"emcgrew@upenn.edu"},"due_date":"2024-04-25T15:49:30.653000+00:00","created":"2024-04-25T16:22:08.597414+00:00","modified":"2024-04-25T16:22:08.597414+00:00","revision":1,"parent_tag_filter":{"include":["ReadyforImageQC"],"exclude":[]},"filters":null,"tags":[],"original_reader_task_id":null}]'
    # tosearch="task_id"
    # first=test.index("task_id")
    # start=first + 10
    # end=start + 7
    # print(test[start:end])
    # log.info(f"{result.stdout}")

# if __name__ == "__main__": 
#     with flywheel_gear_toolkit.GearToolkitContext() as gtk_context:
#         # Setup basic logging
#         gtk_context.init_logging()
#         # Log the configuration for this job
#         gtk_context.log_config()

#         main(gtk_context)





from flask import Module,render_template,jsonify, redirect, request, session, g
import time
from marathon import MarathonClient
from marathon.models.base import MarathonResource
from marathon.models.app import MarathonTaskFailure
import cmconfig
# from configmanage.cmconfig import *
# print type(MARATHON)
marathon = Module(__name__)
# case.before_request(login_filter)
# print MARATHON
c = MarathonClient(cmconfig.MARATHON)
def marathoncollet():    
    appmetrics = c.get_metrics()
    appsIdList = c.list_apps()
    print appsIdList[1]
    appID = appsIdList[1].id
    cpus = appsIdList[1].cpus
    disk = appsIdList[1].disk
    mem = appsIdList[1].mem
    ports  = appsIdList[1].ports
    # last_task_failure = appsIdList[1].last_task_failure 
    # uris  = appsIdList[1].uris 
    tasks_staged  = appsIdList[1].tasks_staged 
 
    ###########container####################
    port_mappings = appsIdList[1].container.docker.port_mappings
    # Dtype = appsIdList[1].container.docker.type
    images = appsIdList[1].container.docker.image
    volumes  = appsIdList[1].container.volumes 
    
    task = c.list_tasks(appID)
    t = MarathonTaskFailure()
    for i in task:       
        t = MarathonTaskFailure()
        print appID,i.host,i.ports,i.staged_at,i.started_at
    #     t = str()
    #     print time.strftime(t,"%Y-%m-%d %H:%M:%S")
         
    print task 
    
    print appID,images
    print appID,cpus,disk,mem,ports,tasks_staged,volumes 
    # print port_mappings
    
    cmFile=open('cm.txt','w')
    cmFile.write(images)
    cmFile.close()
# print containerPort

# for i in appsIdList:
#  
#     print i
#     appid=i.rsplit('::/')[1]
#     print appid
#     taskList = c.list_tasks(appid)

# app=c.
# print leader,marathon_config
# print taskList
# print app2['"reconciliationInterval"']
# def create():
    
# marathoncollet()
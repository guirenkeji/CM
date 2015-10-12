from marathon import MarathonClient
from marathon.models.base import MarathonResource

c = MarathonClient('http://20.26.17.133:8080')
appmetrics=c.get_metrics()
appsIdList = c.list_apps()
print appsIdList[1]
cpus = appsIdList[1].cpus
disk = appsIdList[1].disk
mem = appsIdList[1].mem
ports  = appsIdList[1].ports 
# uris  = appsIdList[1].uris 
tasks_staged  = appsIdList[1].tasks_staged 
port_mappings = appsIdList[1].container.docker.port_mappings
# containerPort = port_mappings.containerPort
images = appsIdList[1].container.docker.image
volumes  = appsIdList[1].container.volumes 
print images
print cpus,disk,mem,ports,tasks_staged
print volumes 
print port_mappings
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

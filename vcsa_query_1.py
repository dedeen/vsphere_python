# dan@dsblue.net    Oct 2022
# Description: Connect to VCSA and list VMs, other info
# Reference:https://code.vmware.com/apis/191/vsphere-automation
#  Make sure you have "rest.py" file into your python directory.

import vcsa_rest_utils
import json
vcip="10.0.0.175" # vCenter server ip address/FQDN

#Get vCenter server session and can be used as needed. pass vcenter username & password
vcsession = vcsa_rest_utils.get_vc_session(vcip,"administrator@vsphere.local","Edeen#11")

#Get all the VMs from inventory using below method from "vcsa_rest_utils" module.
vms = vcsa_rest_utils.get_vms(vcip)

# Parsing the JSON response we got from above function call (it has all the Vms present in inventory
vm_response=json.loads(vms.text)
json_data=vm_response["value"]

print()
print ("VMs and MOIDs, Powered On")
print ("=========================")
for vm in json_data:
        if vm.get("power_state") == "POWERED_ON":
            pad = 25 - len(vm.get("name"))
            print (vm.get("name")+" "* pad +vm.get("vm")+"\t"+vm.get("power_state")+"\t"  
                    +str(vm.get("memory_size_MiB"))+" MiB"+"\t"
                    +str(vm.get("cpu_count"))+" cpus"+"\t"
            )
                
print()                
print ("VMs and MOIDs, Powered Off")
print ("==========================")
for vm in json_data:
        if vm.get("power_state") == "POWERED_OFF":
            pad = 25 - len(vm.get("name"))
            print (vm.get("name")+" "* pad +vm.get("vm")+"\t"+vm.get("power_state")+"\t"  
                    +str(vm.get("memory_size_MiB"))+" MiB"+"\t"
                    +str(vm.get("cpu_count"))+" cpus"+"\t"
            )
#############################################################            
#Get all the ESXi hosts from VCSA, using vcsa_rest_utils module.
hosts = vcsa_rest_utils.get_hosts(vcip)

# Parsing the JSON response we got from above function call (it has all hosts from vcsa
host_response=json.loads(hosts.text)
json_data=host_response["value"]

print()
print ("Hosts Returned from VCSA")
print ("========================")
for host in json_data:
      pad = 25 - len(host.get("host"))
      print (host.get("host")+" "* pad +host.get("name")+"\t"+host.get("connection_state"))
#############################################################            
#Get all the datastores from VCSA, using vcsa_rest_utils module.
datastores = vcsa_rest_utils.get_datastores(vcip)

# Parsing the JSON response we got from above function call (it has all hosts from vcsa
datastore_response=json.loads(datastores.text)
json_data=datastore_response["value"]

print()
print ("Datastores Returned from VCSA \t|    Capacity (GB)      Free (GB)        % Free")
print ("==============================================================================")

for ds in json_data:
      pad = 25 - len(ds.get("name"))
      cap_gbps = ds.get("capacity") // 1048576      #convert to GB
      free_gbps = ds.get("free_space") // 1048576
      temp=(free_gbps / cap_gbps)*100               #% free of capacity
      
      print (ds.get("name")+" "* pad +ds.get("type")+"\t"+"\t"
            +str(cap_gbps)+"    \t"+str(free_gbps)+"    \t"
            +str(int(temp))+" %"
            )


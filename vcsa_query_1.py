# dan@dsblue.net    Oct 2022
# Description: Connect to VCSA and list VMs, other info
# Reference:https://code.vmware.com/apis/191/vsphere-automation
#  Make sure you have "rest.py" file into your python directory.

import vcsa_rest_utils
import json
vcip="10.0.0.175" # vCenter server ip address/FQDN

#Get vCenter server session and can be used as needed. pass vcenter username & password
vcsession = vcsa_rest_utils.get_vc_session(vcip,"administrator@vsphere.local","Edeen#11")

#Get all the VMs from inventory using below method from "vcrest" module.
vms = vcsa_rest_utils.get_vms(vcip)

# Parsing the JSON response we got from above function call (it has all the Vms present in inventory
vm_response=json.loads(vms.text)
json_data=vm_response["value"]

print ("VM names and its unique MOID, ON")
print ("=================================")
for vm in json_data:
        if vm.get("power_state") == "POWERED_ON":
            pad = 25 - len(vm.get("name"))
            print (vm.get("name")+" "* pad +vm.get("vm")+"\t"+vm.get("power_state"))
                
print ("VM names and its unique MOID, OFF")
print ("=================================")
for vm in json_data:
        if vm.get("power_state") == "POWERED_OFF":
            pad = 25 - len(vm.get("name"))
            print (vm.get("name")+" "* pad +vm.get("vm")+"\t"+vm.get("power_state"))
            
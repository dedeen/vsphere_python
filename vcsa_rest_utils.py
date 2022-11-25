# dan@dsblue.net    Oct 2022
# Description: Connect to VCSA and list VMs, other info
# Reference:https://code.vmware.com/apis/191/vsphere-automation
#  Make sure you have "rest.py" file into your python directory.

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s=requests.Session()
s.verify=False

# Function to get the vCenter server session
def get_vc_session(vcip,username,password):
         s.post('https://'+vcip+'/rest/com/vmware/cis/session',auth=(username,password))
         return s

# Function to get all the VMs from vCenter inventory
def get_vms(vcip):
        vms=s.get('https://'+vcip+'/rest/vcenter/vm')
        return vms

#Function to power on particular VM
def poweron_vm(vmmoid,vcip):
        s.post('https://'+vcip+'/rest/vcenter/vm/'+vmmoid+'/power/start')

# Function to power off particular VM
def poweroff_vm(vmmoid,vcip):
        s.post('https://'+vcip+'/rest/vcenter/vm/'+vmmoid+'/power/stop')
#################################################################################
# Description:  Utilities for connecting to VCSA
#               Tested with ESXi and VCSA 6.7
#               https://code.vmware.com/apis/191/vsphere-automation
#               Dan Edeen, dan@dsblue.net    Oct 2022
#
import requests
import json

# Ignore non-cert condition for lab systems
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s=requests.Session()
s.verify=False
#
# Function to get the vCenter server session
def get_vc_session(vcip,username,password):
         s.post('https://'+vcip+'/rest/com/vmware/cis/session',auth=(username,password))
         return s
#
# Function to get all the VMs from vCenter inventory
def get_vms(vcip):
        vms=s.get('https://'+vcip+'/rest/vcenter/vm')
        return vms
#
#Function to power on particular VM
def poweron_vm(vmmoid,vcip):
        s.post('https://'+vcip+'/rest/vcenter/vm/'+vmmoid+'/power/start')
#
# Function to power off particular VM
def poweroff_vm(vmmoid,vcip):
        s.post('https://'+vcip+'/rest/vcenter/vm/'+vmmoid+'/power/stop')
#
# Function to get all the ESXi Hosts from VCSA
def get_hosts(vcip):
        hosts=s.get('https://'+vcip+'/rest/vcenter/host')
        return hosts
#
# Function to get all the datastores from VCSA
def get_datastores(vcip):
        datastores=s.get('https://'+vcip+'/rest/vcenter/datastore')
        return datastores
#
# Function to get network info from VCSA
def get_networks(vcip):
        networks=s.get('https://'+vcip+'/rest/vcenter/network')
        return networks
#################################################################################

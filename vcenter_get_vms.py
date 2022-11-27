"""
Description: Connect to VCSM and list VMs and many of the VM attributes
             VMware vSphere Python SDK, pyvmomi
             Tested with Vsphere 6.7.x
             Dan Edeen, dan@dsblue.net    Oct 2022
             Adapted from https://github.com/vmware/pyvmomi-community-samples
"""
from pyVim.connect import SmartConnect
import ssl

s=ssl.SSLContext(ssl.PROTOCOL_SSLv23) 
s.verify_mode=ssl.CERT_NONE
MAX_DEEP = 5

#list the vm info, and recurse folder to max depth
def list_vms(vm,depth=1):
    if hasattr(vm, 'childEntity'):
        if depth > MAX_DEEP:
            return
        vmlist = vm.childEntity
        for child in vmlist: 
            list_vms(child, depth+1)
        return
    
    summary = vm.summary
    print("[VM:"+summary.config.name+"]" )
    
    print("  InstUuid:   "+summary.config.instanceUuid +"\r\n"
        +"  uuid:       "+summary.config.uuid +"\r\n"
        +"  vmPathName: "+summary.config.vmPathName +"\r\n"
        +"  guestId:    "+summary.config.guestId +"\r\n"
        +"  guestFName: "+summary.config.guestFullName +"\r\n"
        +"  hostname:   "+summary.runtime.host.name +"\r\n"
        +"  last boot:   "+str(summary.runtime.bootTime) +"\r\n"
        +"  powerState:  "+summary.runtime.powerState +"\r\n"
        +"  IP Addr:     "+str(summary.guest.ipAddress) +"\r\n"
        +"  Parent Obj:  "+summary.runtime.host.parent.name +"\r\n"
        )
    
#list the vms from a vCenter
def main():
    si= SmartConnect(host="10.0.0.175", user="administrator@vsphere.local", pwd="Edeen#11", sslContext=s)
    content = si.RetrieveContent()
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            datacenter = child
            vmfolder = datacenter.vmFolder
            vmlist = vmfolder.childEntity
            for vm in vmlist: 
             list_vms(vm)

# Run it 
if __name__ == "__main__":
    main()

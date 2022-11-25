# Dan script to query 1 or more ESXi hosts and retrieve much useful information
# Hosts read from file here, later will pull from input parms file

from pyVim.connect import SmartConnect


si=SmartConnect(host="10.0.0.19",user="root",
pwd="Edeen#11",port=443)
aboutInfo=si.content.about

print("Product Name:",aboutInfo.fullName)

si.Disconnect(si)


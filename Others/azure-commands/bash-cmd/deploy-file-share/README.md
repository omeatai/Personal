-----------------------
DEPLOY AZURE FILE SHARE AND MAP TO WINDOWS SERVERS
-----------------------

-----------------------
#Create Resource Group
-----------------------
az group create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name RG-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus

-----------------------
#Create Virtual Network
-----------------------
az network vnet create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name vNET-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--address-prefix 10.0.0.0/16 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet-name mySubnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet-prefix 10.0.0.0/24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus

-----------------------
#Create VM-1
-----------------------
az vm create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--no-wait \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name VM-1 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vnet-name vNET-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet mySubnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--image win2016datacenter \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--size Standard_B2s \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-username azureadmin \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-password admin123123!

-----------------------
#Create VM-2
-----------------------
az vm create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--no-wait \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name VM-2 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vnet-name vNET-LAB24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet mySubnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--image win2016datacenter \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--size Standard_B2s \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-username azureadmin \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-password admin123123!

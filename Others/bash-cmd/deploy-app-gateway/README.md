-----------------------
DEPLOY APPLICATION GATEWAY PATH-BASED-ROUTING FOR AZURE VMS
-----------------------

-----------------------
#Create Resource Group
-----------------------
az group create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus 

-----------------------
#List Resource Groups
-----------------------
az group list -o table\
az group show --name RG-LAB22 -o table

-----------------------
#Create Virtual Network with 2 Subnets
-----------------------
az network vnet create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name vNET-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--address-prefixes 10.0.0.0/16 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--network-security-group "" \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet-name APPGW-Subnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet-prefixes 10.0.0.0/24 \\\

az network vnet subnet create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name BE-Subnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--address-prefixes 10.0.1.0/24 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vnet-name vNET-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--network-security-group "" 

-----------------------
#List Virtual Networks
-----------------------
az network vnet list -o table\
az network vnet show -g RG-LAB22 -n vNET-LAB22 -o table

-----------------------
#List Subnets
-----------------------
az network vnet subnet list --vnet-name vNET-LAB22 -g RG-LAB22 -o table

-----------------------
#Create a Network Security Group For VM1
-----------------------
az network nsg create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name NSG-VM1 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus 

-----------------------
#List Network Security Groups
-----------------------
az network nsg list -g RG-LAB22 -o table 

-----------------------
#Create Network Security Group Rule AllowHTTPInbound For NSG-VM1
-----------------------
az network nsg rule create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name AllowHTTPInbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg-name NSG-VM1 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--protocol Tcp \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--direction Inbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-address-prefixes '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-port-ranges '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-address-prefixes 'VirtualNetwork' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-port-ranges 80 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--access Allow \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--priority 200 

-----------------------
#Create Network Security Group Rule AllowSSHInbound For NSG-VM1
-----------------------
az network nsg rule create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name AllowSSHInbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg-name NSG-VM1 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--protocol Tcp \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--direction Inbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-address-prefixes '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-port-ranges '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-address-prefixes 'VirtualNetwork' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-port-ranges 22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--access Allow \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--priority 100 

-----------------------
#List custom Network Security Group Rules
-----------------------
az network nsg rule list --nsg-name NSG-VM1 -g RG-LAB22 -o table 

-----------------------
#Create Virtual Machine VM1
-----------------------
az vm create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name VM1 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-username azureadmin \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-password admin123123! \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--image UbuntuLTS \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vnet-name vNET-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet BE-Subnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg NSG-VM1 

-----------------------
#List Virtual Machines
-----------------------
az vm list -o table

-----------------------
#Install Apache Web Service in the Virtual Machine VM1 
-----------------------
az vm extension set \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--publisher Microsoft.Azure.Extensions \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--version 2.0 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name CustomScript \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vm-name VM1 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-profile-app.git /var/www/html/"}' 

-----------------------
#Create a Network Security Group For VM2
-----------------------
az network nsg create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name NSG-VM2 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus 

-----------------------
#Create Network Security Group Rule AllowHTTPInbound For NSG-VM2
-----------------------
az network nsg rule create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name AllowHTTPInbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg-name NSG-VM2 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--protocol Tcp \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--direction Inbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-address-prefixes '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-port-ranges '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-address-prefixes 'VirtualNetwork' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-port-ranges 80 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--access Allow \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--priority 200 

-----------------------
#Create Network Security Group Rule AllowSSHInbound For NSG-VM2
-----------------------
az network nsg rule create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name AllowSSHInbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg-name NSG-VM2 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--protocol Tcp \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--direction Inbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-address-prefixes '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-port-ranges '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-address-prefixes 'VirtualNetwork' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-port-ranges 22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--access Allow \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--priority 100 	

-----------------------
#Create Virtual Machine VM2
-----------------------
az vm create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name VM2 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-username azureadmin \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-password admin123123! \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--image UbuntuLTS \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vnet-name vNET-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet BE-Subnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg NSG-VM2 

-----------------------
#Install Apache Web Service in the Virtual Machine VM2 (Project Images WebServer)
-----------------------
az vm extension set \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--publisher Microsoft.Azure.Extensions \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--version 2.0 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name CustomScript \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vm-name VM2 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-project-images.git /var/www/html/images"}' 

-----------------------
#Create a Network Security Group For VM3
-----------------------
az network nsg create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name NSG-VM3 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--location eastus 

-----------------------
#Create Network Security Group Rule AllowHTTPInbound For NSG-VM3
-----------------------
az network nsg rule create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name AllowHTTPInbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg-name NSG-VM3 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--protocol Tcp \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--direction Inbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-address-prefixes '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-port-ranges '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-address-prefixes 'VirtualNetwork' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-port-ranges 80 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--access Allow \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--priority 200 

-----------------------
#Create Network Security Group Rule AllowSSHInbound For NSG-VM3
-----------------------
az network nsg rule create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name AllowSSHInbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg-name NSG-VM3 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--protocol Tcp \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--direction Inbound \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-address-prefixes '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--source-port-ranges '*' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-address-prefixes 'VirtualNetwork' \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--destination-port-ranges 22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--access Allow \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--priority 100 

-----------------------
#Create Virtual Machine VM3 (Project Videos WebServer)
-----------------------
az vm create \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name VM3 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-username azureadmin \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--admin-password admin123123! \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--image UbuntuLTS \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vnet-name vNET-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--subnet BE-Subnet \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--nsg NSG-VM3 

-----------------------
#Install Apache Web Service in the Virtual Machine VM3 (Project Videos WebServer)
-----------------------
az vm extension set \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--publisher Microsoft.Azure.Extensions \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--version 2.0 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--name CustomScript \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--vm-name VM3 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--resource-group RG-LAB22 \\\
  &nbsp;&nbsp;&nbsp;&nbsp;--settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-project-videos.git /var/www/html/videos"}' 













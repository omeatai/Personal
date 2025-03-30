#Create Resource Group
az group create \
  --name RG-LAB22 \
  --location eastus

#Create Virtual Network with 2 Subnets
az network vnet create \
  --name vNET-LAB22 \
  --address-prefixes 10.0.0.0/16 \
  --resource-group RG-LAB22 \
  --location eastus \
  --network-security-group "" \
  --subnet-name APPGW-Subnet \
  --subnet-prefixes 10.0.0.0/24

az network vnet subnet create \
  --name BE-Subnet \
  --address-prefixes 10.0.1.0/24 \
  --vnet-name vNET-LAB22 \
  --resource-group RG-LAB22 \
  --network-security-group ""
  
# Create a Network Security Group For VM1
az network nsg create \
  --name NSG-VM1 \
  --resource-group RG-LAB22 \
  --location eastus

# Create Network Security Group Rule AllowHTTPInbound For NSG-VM1
az network nsg rule create \
  --name AllowHTTPInbound \
  --nsg-name NSG-VM1 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 80 \
  --access Allow \
  --priority 200 

# Create Network Security Group Rule AllowSSHInbound For NSG-VM1
az network nsg rule create \
  --name AllowSSHInbound \
  --nsg-name NSG-VM1 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 22 \
  --access Allow \
  --priority 100

# Create Virtual Machine VM1
az vm create \
  --name VM1 \
  --resource-group RG-LAB22 \
  --admin-username azureadmin \
  --admin-password admin123123! \
  --image UbuntuLTS \
  --vnet-name vNET-LAB22 \
  --subnet BE-Subnet \
  --nsg NSG-VM1

# Install Apache Web Service in the Virtual Machine VM1 
az vm extension set \
  --publisher Microsoft.Azure.Extensions \
  --version 2.0 \
  --name CustomScript \
  --vm-name VM1 \
  --resource-group RG-LAB22 \
  --settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-profile-app.git /var/www/html/"}'

# Create a Network Security Group For VM2
az network nsg create \
  --name NSG-VM2 \
  --resource-group RG-LAB22 \
  --location eastus

# Create Network Security Group Rule AllowHTTPInbound For NSG-VM2
az network nsg rule create \
  --name AllowHTTPInbound \
  --nsg-name NSG-VM2 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 80 \
  --access Allow \
  --priority 200

# Create Network Security Group Rule AllowSSHInbound For NSG-VM2
az network nsg rule create \
  --name AllowSSHInbound \
  --nsg-name NSG-VM2 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 22 \
  --access Allow \
  --priority 100	

# Create Virtual Machine VM2
az vm create \
  --name VM2 \
  --resource-group RG-LAB22 \
  --admin-username azureadmin \
  --admin-password admin123123! \
  --image UbuntuLTS \
  --vnet-name vNET-LAB22 \
  --subnet BE-Subnet \
  --nsg NSG-VM2

# Install Apache Web Service in the Virtual Machine VM2 (Project Images WebServer)
az vm extension set \
  --publisher Microsoft.Azure.Extensions \
  --version 2.0 \
  --name CustomScript \
  --vm-name VM2 \
  --resource-group RG-LAB22 \
  --settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-project-images.git /var/www/html/images"}'

# Create a Network Security Group For VM3
az network nsg create \
  --name NSG-VM3 \
  --resource-group RG-LAB22 \
  --location eastus

# Create Network Security Group Rule AllowHTTPInbound For NSG-VM3
az network nsg rule create \
  --name AllowHTTPInbound \
  --nsg-name NSG-VM3 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 80 \
  --access Allow \
  --priority 200

# Create Network Security Group Rule AllowSSHInbound For NSG-VM3
az network nsg rule create \
  --name AllowSSHInbound \
  --nsg-name NSG-VM3 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 22 \
  --access Allow \
  --priority 100

# Create Virtual Machine VM3 (Project Videos WebServer)
az vm create \
  --name VM3 \
  --resource-group RG-LAB22 \
  --admin-username azureadmin \
  --admin-password admin123123! \
  --image UbuntuLTS \
  --vnet-name vNET-LAB22 \
  --subnet BE-Subnet \
  --nsg NSG-VM3

# Install Apache Web Service in the Virtual Machine VM3 (Project Videos WebServer)
az vm extension set \
  --publisher Microsoft.Azure.Extensions \
  --version 2.0 \
  --name CustomScript \
  --vm-name VM3 \
  --resource-group RG-LAB22 \
  --settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-project-videos.git /var/www/html/videos"}'










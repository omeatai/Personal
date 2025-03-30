#Create Resource Group Eastus
az group create \
  --name RG-LAB23 \
  --location eastus

#Create Virtual Network 1
az network vnet create \
    --resource-group RG-LAB23 \
    --name vNET-1 \
    --address-prefix 10.0.0.0/16 \
    --subnet-name Subnet-1 \
    --subnet-prefix 10.0.0.0/24 \
    --location eastus

#Create Virtual Network 2
az network vnet create \
    --resource-group RG-LAB23 \
    --name vNET-2 \
    --address-prefix 10.1.0.0/16 \
    --subnet-name Subnet-2 \
    --subnet-prefix 10.1.0.0/24 \
    --location eastus

#Create Virtual Network 3
az network vnet create \
    --resource-group RG-LAB23 \
    --name vNET-3 \
    --address-prefix 10.2.0.0/16 \
    --subnet-name Subnet-3 \
    --subnet-prefix 10.2.0.0/24 \
    --location westeurope

#Create VM-1
az vm create \
    --resource-group RG-LAB23 \
    --no-wait \
    --name VM-1 \
    --location eastus \
    --vnet-name vNET-1 \
    --subnet Subnet-1 \
    --image UbuntuLTS \
    --size Standard_B1s \
    --admin-username azureadmin \
    --admin-password admin123123!

#Create VM-2
az vm create \
    --resource-group RG-LAB23 \
    --no-wait \
    --name VM-2 \
    --location eastus \
    --vnet-name vNET-2 \
    --subnet Subnet-2 \
    --image UbuntuLTS \
    --size Standard_B1s \
    --admin-username azureadmin \
    --admin-password admin123123!

#Create VM-3
az vm create \
    --resource-group RG-LAB23  \
    --no-wait \
    --name VM-3 \
    --location westeurope \
    --vnet-name vNET-3 \
    --subnet Subnet-3\
    --image UbuntuLTS \
    --size Standard_B1s \
    --admin-username azureadmin \
    --admin-password admin123123!

#Connect Global Peer vNET-2 to vNET-3
az network vnet peering create \
    --name vNET-2-to-vNET-3 \
    --remote-vnet vNET-3 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-2 \
    --allow-vnet-access

#Connect Global Peer vNET-3 to vNET-2
az network vnet peering create \
    --name vNET-3-to-vNET-2 \
    --remote-vnet vNET-2 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-3 \
    --allow-vnet-access

#Connect Local Peer vNET-1 to vNET-2
az network vnet peering create \
    --name vNET-1-to-vNET-2 \
    --remote-vnet vNET-2 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-1 \
    --allow-vnet-access

#Connect Local Peer vNET-2 to vNET-1
az network vnet peering create \
    --name vNET-2-to-vNET-1 \
    --remote-vnet vNET-1 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-2 \
    --allow-vnet-access

#Connect Global Peer vNET-1 to vNET-3
az network vnet peering create \
    --name vNET-1-to-vNET-3 \
    --remote-vnet vNET-3 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-1 \
    --allow-vnet-access

#Connect Global Peer vNET-3 to vNET-1
az network vnet peering create \
    --name vNET-3-to-vNET-1 \
    --remote-vnet vNET-1 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-3 \
    --allow-vnet-access





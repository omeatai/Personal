#Create Resource Group
az group create \
  --name RG-LAB24 \
  --location eastus

#Create Virtual Network
az network vnet create \
    --resource-group RG-LAB24 \
    --name vNET-LAB24 \
    --address-prefix 10.0.0.0/16 \
    --subnet-name mySubnet \
    --subnet-prefix 10.0.0.0/24 \
    --location eastus

#Create VM-1
az vm create \
    --resource-group RG-LAB24 \
    --no-wait \
    --name VM-1 \
    --location eastus \
    --vnet-name vNET-LAB24 \
    --subnet mySubnet \
    --image win2016datacenter \
    --size Standard_B2s \
    --admin-username azureadmin \
    --admin-password admin123123!

#Create VM-2
az vm create \
    --resource-group RG-LAB24 \
    --no-wait \
    --name VM-2 \
    --location eastus \
    --vnet-name vNET-LAB24 \
    --subnet mySubnet \
    --image win2016datacenter \
    --size Standard_B2s \
    --admin-username azureadmin \
    --admin-password admin123123!









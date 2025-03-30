#Create Virtual Network 1
az network vnet create \
    --resource-group RG-LAB23 \
    --name vNET-1 \
    --address-prefix 10.0.0.0/16 \
    --subnet-name Subnet-1 \
    --subnet-prefix 10.0.0.0/24 \
    --location eastus
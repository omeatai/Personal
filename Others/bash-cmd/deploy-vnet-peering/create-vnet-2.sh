#Create Virtual Network 2
az network vnet create \
    --resource-group RG-LAB23 \
    --name vNET-2 \
    --address-prefix 10.1.0.0/16 \
    --subnet-name Subnet-2 \
    --subnet-prefix 10.1.0.0/24 \
    --location eastus
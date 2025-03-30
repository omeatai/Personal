#Create Virtual Network 3
az network vnet create \
    --resource-group RG-LAB23 \
    --name vNET-3 \
    --address-prefix 10.2.0.0/16 \
    --subnet-name Subnet-3 \
    --subnet-prefix 10.2.0.0/24 \
    --location westeurope
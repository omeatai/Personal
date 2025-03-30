#Create Virtual Network
az network vnet create \
    --resource-group RG-LAB24 \
    --name vNET-LAB24 \
    --address-prefix 10.0.0.0/16 \
    --subnet-name mySubnet \
    --subnet-prefix 10.0.0.0/24 \
    --location eastus
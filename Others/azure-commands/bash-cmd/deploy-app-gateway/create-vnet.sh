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

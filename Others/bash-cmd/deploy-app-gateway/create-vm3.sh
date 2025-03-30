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
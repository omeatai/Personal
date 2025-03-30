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
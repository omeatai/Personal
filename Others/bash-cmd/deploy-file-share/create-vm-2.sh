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

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
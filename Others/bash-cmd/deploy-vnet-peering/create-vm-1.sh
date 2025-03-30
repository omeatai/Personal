#Create VM-1
az vm create \
    --resource-group RG-LAB23 \
    --no-wait \
    --name VM-1 \
    --location eastus \
    --vnet-name vNET-1 \
    --subnet Subnet-1 \
    --image UbuntuLTS \
    --size Standard_B1s \
    --admin-username azureadmin \
    --admin-password admin123123!
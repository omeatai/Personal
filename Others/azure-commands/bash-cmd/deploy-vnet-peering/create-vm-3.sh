#Create VM-3
az vm create \
    --resource-group RG-LAB23  \
    --no-wait \
    --name VM-3 \
    --location westeurope \
    --vnet-name vNET-3 \
    --subnet Subnet-3\
    --image UbuntuLTS \
    --size Standard_B1s \
    --admin-username azureadmin \
    --admin-password admin123123!
#Connect Local Peer vNET-2 to vNET-1
az network vnet peering create \
    --name vNET-2-to-vNET-1 \
    --remote-vnet vNET-1 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-2 \
    --allow-vnet-access
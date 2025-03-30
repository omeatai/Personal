#Connect Global Peer vNET-3 to vNET-1
az network vnet peering create \
    --name vNET-3-to-vNET-1 \
    --remote-vnet vNET-1 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-3 \
    --allow-vnet-access
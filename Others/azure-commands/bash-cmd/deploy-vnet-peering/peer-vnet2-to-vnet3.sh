#Connect Global Peer vNET-2 to vNET-3
az network vnet peering create \
    --name vNET-2-to-vNET-3 \
    --remote-vnet vNET-3 \
    --resource-group RG-LAB23 \
    --vnet-name vNET-2 \
    --allow-vnet-access
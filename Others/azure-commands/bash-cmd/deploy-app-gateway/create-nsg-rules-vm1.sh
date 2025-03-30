# Create Network Security Group Rule AllowHTTPInbound For NSG-VM1
az network nsg rule create \
  --name AllowHTTPInbound \
  --nsg-name NSG-VM1 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 80 \
  --access Allow \
  --priority 200 

# Create Network Security Group Rule AllowSSHInbound For NSG-VM1
az network nsg rule create \
  --name AllowSSHInbound \
  --nsg-name NSG-VM1 \
  --resource-group RG-LAB22 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes 'VirtualNetwork' \
  --destination-port-ranges 22 \
  --access Allow \
  --priority 100
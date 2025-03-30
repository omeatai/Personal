# Install Apache Web Service in the Virtual Machine VM2 (Project Images WebServer)
az vm extension set \
  --publisher Microsoft.Azure.Extensions \
  --version 2.0 \
  --name CustomScript \
  --vm-name VM2 \
  --resource-group RG-LAB22 \
  --settings '{"commandToExecute":"apt-get -y update && apt-get -y install apache2 && rm -rf /var/www/html && git clone https://github.com/omeatai/my-project-images.git /var/www/html/images"}'

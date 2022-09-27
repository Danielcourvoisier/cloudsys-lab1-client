#!/bin/bash

# To install on start of server
#sudo apt -y install git
#cd /home/ubuntu/
#git clone https://github.com/Danielcourvoisier/cloudsys-lab1-client.git
#export CLOUDSYS_SERVER_IP=google.ch
export CLOUDSYS_SERVER_IP=194.182.190.225:8080 >>~/.bashrc
# Run Client
cd /home/ubuntu/cloudsys-lab1-client/
python3 main.py
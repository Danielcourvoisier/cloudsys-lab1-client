# Dependancies
import os
import time
import requests
import json

# Get env variable to get IP of server
server_addr = os.environ["CLOUDSYS_SERVER_IP"]

while True:
    response_API = requests.get(f"http://{server_addr}")
    print(response_API.status_code)
    data = response_API.text
    print(data)
    time.sleep(1)
    #json.loads(data)
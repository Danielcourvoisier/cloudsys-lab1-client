import time

import requests
import json


while True:
    response_API = requests.get('http://127.0.0.1:8000/')
    print(response_API.status_code)
    data = response_API.text
    print(data)
    time.sleep(1)
    #json.loads(data)

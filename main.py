import os
import requests
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Get env variable to get IP of server
server_addr = os.environ["SERVER_IP"]
server_port = os.environ["SERVER_PORT"]
server_url_data = f"http://{server_addr}:{server_port}/data"
app_port = os.environ["APP_PORT"]


app = FastAPI()


# root
@app.get("/", response_class=HTMLResponse)
async def root():
    # request data to server
    try:
        response = requests.get(server_url_data)
        print(response.status_code)
        data = response.text
    except:
        data = "Error retrieving data"

    return """
    <html>
        <head>
            <title>CloudSys Lab1</title>
        </head>
        <body>
            <h1>Hey, you are on my client!</h1>
            <p>
            My address: <a id="my_url" href=""> </a>
            <p>
            I get data from: 
            <a href="{server_url}">{server_url}</a>
            <p>
            Here the data:
            <p>
            {data}
            <p>
            <script>
                url = window.location.href;
                document.getElementById("my_url").innerHTML = url;
                document.getElementById("my_url").href = url
            </script>
        </body>
    </html>
    """.format(server_url=server_url_data, data=data)

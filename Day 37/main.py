import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "carlos1212"
TOKEN = "jskahdkjsahkaaansajsn"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_params, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
                }
headers = {
    "X-USER-TOKEN": TOKEN
}

#requests.post(url=pixela_endpoint, json=graph_endpoint, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date" : "20230206",
    "quantity": "9.74",
}

requests.post(url=pixel_creation_endpoint, json=graph_endpoint, headers=headers)
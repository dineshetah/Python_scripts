# HTTP REQUESTS 

# GET - requests.get()
# Post - requests.post()
# Put - requests.put()
# Delete -requests.delete()

# HTTP POST REQUESTS 
# https://pixe.la/  see first this website take it knowledge and go through to do project 

import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
USERNAME ="sudeep"
TOKEN = "kfg14578666@#$"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ADVANCED AUTHENTICATION USING AN HTTP HEADER 
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph", 
    "unit": "Km", 
    "type": "float", 
    "color":"ajisai", 
}
headers ={
    "X-USER-TOKEN": TOKEN
}
# resoponse = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resoponse)

# ADD A PIXEL TO THE HABIT TRACKER USING PSOT REQUEST 

# pixel_creation_endpoint = f"{pixela_endpoint/{USERNAME}/graphs/{GRAPH_ID}}"
pixel_creation_endpoint = "{}/users/{}/graphs/{}".format(pixela_endpoint, USERNAME, GRAPH_ID)

# Here, Autofilling today's date using strftime 
#today =datetime(year=2024,month=7, day=8)
today =datetime.now()
#today = datetime.now()
#datefortmtted=today.strftime("%Y%m%d")
print(today)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many kilometers did you cycle today?")

}
resoponse = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
# for put uses 
updated_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"5.57",
}

resoponse = requests.put(url=updated_endpoint,json=new_pixel_data, headers=headers)
#print(resoponse.text)

# for delete uses 
deleted_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}{today.strftime('%Y%m%d')}"
resoponse = requests.delete(url=deleted_endpoint, headers=headers)
print(resoponse.text)
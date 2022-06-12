
from constants import *
import requests
import json

todo = {"userId": 1, "title": "test", "completed": False}
response = requests.post(restapi_url, json=todo)
response.json()
#{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

print(response.status_code)



todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(restapi_url, data=json.dumps(todo), headers=headers)
response.json()
#{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

response.status_code
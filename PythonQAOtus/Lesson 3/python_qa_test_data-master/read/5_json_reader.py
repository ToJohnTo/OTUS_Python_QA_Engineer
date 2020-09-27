import json

with open("../files/example.json", "r") as f:
    users = json.loads(f.read())

users_list = users['users']

for user in users_list:
    print(user)

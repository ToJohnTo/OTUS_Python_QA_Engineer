import requests

headers = {
    "Accept" : None,
    "User-Agent" : None
}

response = requests.get("https://httpbin.org/get?a=b&c=10", headers=headers, params = {"d": "e", "f": 20})

if response.status_code == 200:
    print("OK!")

if response.ok:
    print("Ok!!!")

print(response.json())
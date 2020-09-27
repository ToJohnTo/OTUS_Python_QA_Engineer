import requests
from jsonschema import validate

url = "https://jsonplaceholder.typicode.com/posts/1"
proxy = {"https": "localhost:8080"}

def test_structure_of_schema():
    """ Проверка структуры ответа на запрос /posts/1 """
    response = requests.get(url, proxies=proxy, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
    }
    validate(instance=response.json(), schema=schema)

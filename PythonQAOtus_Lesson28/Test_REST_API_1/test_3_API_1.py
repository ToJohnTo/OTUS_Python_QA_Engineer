import requests
from jsonschema import validate

url = "https://dog.ceo/api/breeds/list/random"
proxy = {"https": "localhost:8080"}

def test_structure_of_schema():
    """ Проверка структуры ответа на запрос /breeds/list/random """
    response = requests.get(url, proxies=proxy, verify=False)
    schema = {
        "message": "object",
        "status": "success"
    }
    validate(instance=response.json(), schema=schema)

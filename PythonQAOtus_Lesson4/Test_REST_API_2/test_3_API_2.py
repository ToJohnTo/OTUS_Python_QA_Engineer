import requests
from jsonschema import validate#, Draft3Validator

url = "https://api.openbrewerydb.org/breweries"
proxy = {"https": "localhost:8080"}

def test_structure_of_schema():
    """ Проверка структуры ответа на запрос /breweries """
    response = requests.get(url, proxies=proxy, verify=False)

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {"type": "string"},
            "city": {"type": "string"},
            "state": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "updated_at": {"type": "string"},
            "tag_list": {"type": "array"},
        },
    }

    # v = Draft3Validator(schema)
    # for error in sorted(v.iter_errors(response.json()[0]), key=str):
    #     print("\n\n************ error ****************\n\n", error.message)

    validate(instance=response.json()[0], schema=schema)

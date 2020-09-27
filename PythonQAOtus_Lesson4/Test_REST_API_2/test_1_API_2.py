import pytest
import requests

url = "https://api.openbrewerydb.org/breweries?by_postal="
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("postal_code", [85382, 72114, 72202, 99654, 44107])
def test_postal_code(postal_code):
    """ Проверка фильтрации по почтовому коду. """
    response = requests.get(url + "{}".format(postal_code), proxies=proxy, verify=False)
    r = response.json()
    is_contain = 0
    for el in r:
        if str(postal_code) in el["postal_code"]:
            is_contain = 1                          # если встретилось хотя бы одно, считаем успешным
    assert is_contain == 1

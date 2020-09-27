import pytest
import requests

url = "https://api.openbrewerydb.org/breweries?by_city="
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("city", ["Birmingham", "Williams", "Tucson"])
def test_filter_by_city(city):
    """ Проверка фильтрации по городу. """
    response = requests.get(url + "{}".format(str(city)), proxies=proxy, verify=False)
    rj = response.json()

    is_contain = 0
    is_not_contain = 0
    for el in rj:
        if city in el["city"]:
            is_contain = 1
        else:
            is_not_contain = 1
    if is_not_contain:
        is_contain = 0
    assert is_contain == 1
import pytest
import requests

url = "https://dog.ceo/api/"
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("breeds", [1, 30, 94])
def test_count_list(breeds):
    """ Проверка получения списка рандомных пород. """
    response = requests.get(url + "breeds/list/random/{}".format(breeds), proxies=proxy, verify=False)
    assert len(response.json()["message"]) == breeds
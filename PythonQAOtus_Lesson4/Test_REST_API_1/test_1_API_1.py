import pytest
import requests

url = "https://dog.ceo/api/"
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("number", [2, 3, 4, 5])
def test_count_image(number):
    """ Проверка получения фотографий рандомных пород. """
    response = requests.get(url + "breeds/image/random/{}".format(number), proxies=proxy, verify=False)
    assert len(response.json()["message"]) == number

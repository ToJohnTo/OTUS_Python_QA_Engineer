import pytest
import requests

url = "https://dog.ceo/api/breeds/list/all/random"
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("count_of_try", [1, 2, 3, 4, 5])
def test_of_availability_server(count_of_try):
    """
    Проверка доступности сервера при различных рандомных списках
    пород собак, получаемых в респонсе.
    """
    response = requests.get(url, proxies=proxy, verify=False)
    assert response.status_code == 200


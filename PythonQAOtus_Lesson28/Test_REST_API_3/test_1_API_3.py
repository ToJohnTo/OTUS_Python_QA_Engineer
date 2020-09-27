import pytest
import requests

url = "https://jsonplaceholder.typicode.com/posts/"
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("post", [1, 2, 3, 4])
def test_get_post(post):
    """ Проверка получения определённых постов. """
    response = requests.get(url + "{}".format(post), proxies=proxy, verify=False)
    assert response.json()["id"] == post

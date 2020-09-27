import pytest
import requests

url = "https://jsonplaceholder.typicode.com/posts/"
proxy = {"https": "localhost:8080"}

@pytest.mark.parametrize("comments", [1, 3, 10])
def test_post_comments(comments):
    """ Проверка получения 5 комментариев к постам. """
    response = requests.get(url + "{}/comments".format(comments), proxies=proxy, verify=False)
    assert len(response.json()) == 5
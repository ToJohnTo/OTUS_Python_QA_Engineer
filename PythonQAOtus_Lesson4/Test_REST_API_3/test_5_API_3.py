import requests

url = "https://jsonplaceholder.typicode.com/posts?userId=1"
proxy = {"https": "localhost:8080"}

def test_userid_status():
    """ Проверка успешности выполнения запроса при выборке по userId. """
    response = requests.get(url, proxies=proxy, verify=False)
    rj = response.json()

    is_filter = 0
    is_not_filter = 0

    for el in rj:
        if el["userId"] == 1:
            is_filter = 1
        else:
            is_not_filter = 0
    if is_not_filter:
        is_filter = 0
    assert is_filter == 1


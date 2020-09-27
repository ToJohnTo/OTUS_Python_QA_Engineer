import requests

url = "https://dog.ceo/api/breeds/list"
proxy = {"https": "localhost:8080"}

def test_all_list_status():
    """ Проверка успешности выполнения запроса при выдаче списка со всеми породами собак. """
    response = requests.get(url, proxies=proxy, verify=False)
    assert response.json()["status"] == "success"


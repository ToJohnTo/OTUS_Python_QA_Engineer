import requests

url = "https://api.openbrewerydb.org/breweries/autocomplete?query=dog"
proxy = {"https": "localhost:8080"}

def test_all_list_status():
    """ Проверка того, что в поиске по слову dog, в каждом значении будет содержаться слово dog """
    response = requests.get(url, proxies=proxy, verify=False)

    is_contain = 0
    is_not_contain = 0
    
    for el in response.json():
        # содержится ли dog во всех значениях словаря
        if "dog" in el["name"].lower():
            is_contain = 1          # содержится
        else:
            is_not_contain = 1      # не содержится
            
    if is_not_contain:              # если не содержится хотя бы в одном значении, то значит нам не подходит
        is_contain = 0
    assert is_contain == 1

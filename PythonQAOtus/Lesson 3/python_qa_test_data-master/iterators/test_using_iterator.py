import pytest
import requests

from csv import DictReader


f = open('test_data.csv')
reader = DictReader(f)

@pytest.mark.parametrize("param", reader)
def test_iterator(param):
    r = requests.get(param['url'])
    assert r.status_code == int(param['status'])

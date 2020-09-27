import pytest
from logging import log


@pytest.fixture()
def open_file():
    f = open("test")
    try:
        yield f

    finally:
        f.close()


def test_open_file(open_file):
    for each in open_file:
        assert each == 'test2'

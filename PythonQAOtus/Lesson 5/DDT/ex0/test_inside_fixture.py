import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 8, 9])
def fixture3(request):
    return request.param


@pytest.fixture(params=[2, 3, 4, 5, 6, 7, 8, 9])
def fixture4(request, fixture3):
    return request.param, fixture3


def test_params_infixture(fixture4):
    assert fixture4[1] + fixture4[0] > 0
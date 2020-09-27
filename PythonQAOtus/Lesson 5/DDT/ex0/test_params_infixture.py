import pytest


# @pytest.fixture(params=["one", "uno"])
# def fixture1(request):
#     return request.param
#
#
# @pytest.fixture(params=["two", "duo", "tres"])
# def fixture2(request):
#     return request.param
#
#
# def test_params_infixture(fixture1, fixture2):
#     assert type(fixture1) == type(fixture2)


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 8, 9])
def fixture3(request):
    return request.param


@pytest.fixture(params=[2, 3, 4, 5, 6, 7, 8, 9])
def fixture4(request):
    return request.param


def test_params_infixture(fixture3, fixture4):
    assert fixture3 + fixture4 > 0
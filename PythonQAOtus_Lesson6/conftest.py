import pytest


@pytest.fixture(params=["Triangle", "Rectangle", "Square", "Circle"])
def fixture_names(request):
    return request.param


@pytest.fixture(params=["0", "3", "4"])
def fixture_angles(request):
    return request.param


@pytest.fixture(params=["0", "14", "30", "60", "256"])
def fixture_perimeter(request):
    return request.param


@pytest.fixture(params=["0", "11", "26", "55", "199"])
def fixture_area(request):
    return request.param

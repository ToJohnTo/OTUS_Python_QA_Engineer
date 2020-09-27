import pytest
import random
import math

class TestClass:

    def __init__(self, mod1, mod2):
        self.mod1 = mod1
        self.mod2 = mod2

    def Hello(self, name):
        return f"Hello, {name}"

# --fixtures
@pytest.fixture(scope="session")
def first_fixture():
    print("\n====> Print from 'first_fixture' in conftest.py")

@pytest.fixture(scope="function")
def fixture_return_rnd_int():
    return random.randint(1, 100)

@pytest.fixture
def fixture_return_class():
    return TestClass(mod1=random, mod2=math)

@pytest.fixture(params=[11, 12, 13, 14])
def fixture_with_params(request):
    return request.param


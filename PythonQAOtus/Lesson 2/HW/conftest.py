import pytest

class TestClass:
    def __init__(self, mod1, mod2, mod3, mod4):
        mod1 = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
        self.mod1 = mod1
        mod2 = set('abracadabra')
        self.mod2 = mod2
        mod3 = {'jack': 4098, 'sape': 4139, 'guido': 4127}
        self.mod3 = mod3
        mod4 = 'spameggs_add_something_words'
        self.mod4 = mod4

@pytest.fixture(scope="session")
def fixture_return_class():
    return TestClass(mod1=list, mod2=set, mod3=dict, mod4=str())

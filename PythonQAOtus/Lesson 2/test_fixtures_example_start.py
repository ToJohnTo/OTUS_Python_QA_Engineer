import pytest

# --fixtures

# @pytest.fixture
# def first_fixture():
#     print("\n====> Print from 'first_fixture'")

@pytest.fixture
def second_fixture():
    print("====> Print from 'second_fixture'")
    return None



# --test cases

def test_fixture_one_example(first_fixture):
    """
    Someting
    """
    pass

def test_fixture_two_example(first_fixture, second_fixture):
    """
    Someting
    """
    pass

def test_fixture_one_example(fixture_return_rnd_int):
    assert fixture_return_rnd_int == 20

def test_the_class(fixture_return_class):
    assert fixture_return_class.mod2.pow(2, 3) == 8
    assert fixture_return_class.mod1.choice(['a', 'b', 'c']) == 'a'
    # assert fixture_return_class.Hello('John') == "Hello, John"

def test_with_params(fixture_with_params):
    return fixture_with_params

@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_with_params_two(test_input):
    print(test_input)



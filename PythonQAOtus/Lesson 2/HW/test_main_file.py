import pytest

# Task-case for perform a skill of use fixture
def test_the_class(fixture_return_class):
    # test for list 1
    assert fixture_return_class.mod1.count('apple') == 2
    # test for list 1.2
    assert fixture_return_class.mod1.count('kiwi') == 1
    # test for list 2
    fixture_return_class.mod1.reverse()
    assert fixture_return_class.mod1 == ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
    # test for list 3
    fixture_return_class.mod1.append('grape')
    assert fixture_return_class.mod1 == ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
    # test for list 4
    fixture_return_class.mod1.sort()
    assert fixture_return_class.mod1 == ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
    # test for list 5
    assert fixture_return_class.mod1.pop() == 'pear'
    # ---------------------------------------------------------------
    # test for set 1
    assert fixture_return_class.mod2 == {'a', 'r', 'b', 'c', 'd'}
    # test for set 2
    b = set('alacazam')
    assert (fixture_return_class.mod2 - b) == {'r', 'd', 'b'}
    # test for set 3
    assert (fixture_return_class.mod2 | b) == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    # test for set 4
    assert (fixture_return_class.mod2 & b) == {'a', 'c'}
    # test for set 5
    assert (fixture_return_class.mod2 ^ b) == {'r', 'd', 'b', 'm', 'z', 'l'}
    # ---------------------------------------------------------------
    # test for dict 1
    assert fixture_return_class.mod3['jack'] == 4098
    # test for dict 2.1
    del fixture_return_class.mod3['sape']
    assert fixture_return_class.mod3 == {'guido': 4127, 'jack': 4098}
    # test for dict 2.2
    fixture_return_class.mod3['irv'] = 4127
    assert fixture_return_class.mod3 == {'guido': 4127, 'irv': 4127, 'jack': 4098}
    # test for dict 3
    assert list(fixture_return_class.mod3.keys()) == ['jack', 'guido', 'irv']
    # test for dict 4
    assert sorted(fixture_return_class.mod3.keys()) == ['guido', 'irv', 'jack']
    # test for dict 5
    b = 'guido' in fixture_return_class.mod3
    assert b is True
    # ---------------------------------------------------------------
    # test for string 1
    assert fixture_return_class.mod4[3:5] == 'me'
    # test for string 2
    assert fixture_return_class.mod4[2::2] == 'aeg_d_oehn_od'
    # test for string 3
    len_of_string = len(fixture_return_class.mod4)
    assert len_of_string == 28
    # test for string 4
    assert fixture_return_class.mod4.upper() == 'SPAMEGGS_ADD_SOMETHING_WORDS'
    # test for string 5
    assert fixture_return_class.mod4.istitle() is False


# Task-case for perform a skill of use parametrize
@pytest.mark.parametrize("test_input", ['abcdefghi', 'jklmnopqr', 'stuvwxyza'])
def test_with_params(test_input):
    a = set(test_input)
    assert len(a) == 9

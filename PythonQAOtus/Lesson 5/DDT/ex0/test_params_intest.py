import pytest


@pytest.mark.parametrize("test_input", "expected_result", [(1, 2), (2, 4), (3, 6)])
def test_multiplication(test_input, expected_result):
    assert test_input * 2 == expected_result

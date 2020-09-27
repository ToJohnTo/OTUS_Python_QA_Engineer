import pytest
import time


def test_example(choice_browser, default_url):
    """
    """
    choice_browser.get(default_url)
    time.sleep(5)
    assert choice_browser.title == 'Your Store'

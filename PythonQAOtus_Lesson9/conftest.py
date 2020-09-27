import pytest
import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def driver_factory(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    # parser.addoption("--url", action="store", default="http://localhost//", help="Enter start page for testing")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    # url = request.config.getoption("--url")
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    # driver.get(url)
    return driver

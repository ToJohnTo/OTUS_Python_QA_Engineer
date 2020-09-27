import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions, FirefoxProfile


def driver_factory(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.headless = True
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        profile = FirefoxProfile()
        profile.accept_untrusted_certs = True
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options, firefox_profile=profile)
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver

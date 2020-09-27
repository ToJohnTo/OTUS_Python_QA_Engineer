import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        type=str,
        help="Browser which will work",
        choices=['chrome', 'firefox'],
        required=True
    )

    parser.addoption(
        '--default_url',
        action='store',
        type=str,
        help="Default url of Opencart",
        default="http://localhost/index.php?route=common/home"
    )


@pytest.fixture
def choice_browser(request):
    cli_input = request.config.getoption("--browser")

    if cli_input == "chrome":
        options = ChromeOptions()
        options.headless = True
        wd = webdriver.Chrome(options=options)
        request.addfinalizer(wd.quit)
        return wd
    elif cli_input == "firefox":
        options = FirefoxOptions()
        options.headless = True
        wd = webdriver.Firefox(options=options)
        wd.wait = WebDriverWait(wd, 8)
        request.addfinalizer(wd.quit)
        return wd


@pytest.fixture
def default_url(request):
    return request.config.getoption("--default_url")

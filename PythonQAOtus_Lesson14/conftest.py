import pytest
import logging
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions, FirefoxProfile
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.base import BasePage
from pages.catalog import CatalogPage
from pages.product_card import ProductCardPage
from pages.login import LoginPage
from pages.login_admin import LoginAdminPage
from pages.products_table import ProductsTablePage
from pages.upload_file_mozilla_page import UploadFileMozillaPage


logging.basicConfig(format='%(levelname)s::%(filename)s::%(funcName)s::%(message)s', filename="logs/selenium.log")
LOG_LEVEL = 10  # DEBUG


def driver_factory(browser):
    if browser == "chrome":
        logger = logging.getLogger('chrome_fixture')
        logger.setLevel(LOG_LEVEL)
        options = ChromeOptions()
        options.headless = True
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        logger.info("Подготовка среды для запуска тестов...")
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        options.add_experimental_option('w3c', False)
        driver = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=caps, options=options), MyListener())
        logger.debug("Браузер Chrome запущен со следующими desired_capabilities:{}".format(driver.desired_capabilities))
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


@pytest.fixture(scope="session")
def browser(request):
    logger = logging.getLogger('browser_fixture')
    logger.setLevel(LOG_LEVEL)
    driver = driver_factory(request.config.getoption("--browser"))
    driver.maximize_window()

    def fin():
        driver.close()
        logger.debug("Браузер закрыт")

    request.addfinalizer(fin)
    return driver


@pytest.fixture()
def base_page(browser):
    page = BasePage(browser)
    page.go_to(url="http://localhost//")
    return page


@pytest.fixture()
def catalog_page(browser):
    page = CatalogPage(browser)
    page.go_to(url="http://localhost/index.php?route=product/category&path=20")
    return page


@pytest.fixture()
def product_card_page(browser):
    page = ProductCardPage(browser)
    page.go_to(url="http://localhost/index.php?route=product/product&path=57&product_id=49")
    return page


@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser)
    page.go_to(url="http://localhost/index.php?route=account/login")
    return page


@pytest.fixture()
def login_admin_page(browser):
    page = LoginAdminPage(browser)
    page.go_to(url="http://localhost//admin/")
    return page


@pytest.fixture()
def products_table_page(browser):
    page = ProductsTablePage(browser)
    page.go_to(url="http://localhost//admin/")
    page.login('user', 'bitnami1')
    page.open_products_table()
    return page


@pytest.fixture()
def upload_file_mozilla_page(browser):
    page = UploadFileMozillaPage(browser)
    page.go_to(url="https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file")
    return page


class MyListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        logging.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'{exception}.png')

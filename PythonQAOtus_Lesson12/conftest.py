import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions, FirefoxProfile
from pages.base import BasePage
from pages.catalog import CatalogPage
from pages.product_card import ProductCardPage
from pages.login import LoginPage
from pages.login_admin import LoginAdminPage
from pages.products_table import ProductsTablePage


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


@pytest.fixture(scope="session")
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    driver.maximize_window()
    request.addfinalizer(driver.close)
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

import pytest
import logging
import allure
import requests
import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, FirefoxProfile
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from pages.base import BasePage
from pages.catalog import CatalogPage
from pages.product_card import ProductCardPage
from pages.login import LoginPage
from pages.login_admin import LoginAdminPage
from pages.products_table import ProductsTablePage
from pages.upload_file_mozilla_page import UploadFileMozillaPage

logging.basicConfig(format='%(levelname)s::%(filename)s::%(funcName)s::%(message)s',
                    filename="logs/selenium.log")
LOG_LEVEL = 10  # DEBUG


def url_data_exists(url):
    # Ждем доступности url
    wait = 10
    while wait > 0:
        r = requests.get(url)
        if r.ok:
            return True
        else:
            time.sleep(1)
            wait -= 1
    return False


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# Это какая-то магия отсюда https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def driver_factory(browser, executor_url, test_name):
    if browser == "chrome":
        logger = logging.getLogger('chrome_fixture')
        logger.setLevel(LOG_LEVEL)
        caps = {"browserName": browser,
                "version": "83.0",
                "enableVnc": True,
                "enableVideo": True,
                "enableLog": True,
                "screenResolution": "1280x720",
                "name": test_name}
        driver = EventFiringWebDriver(webdriver.Remote(command_executor=executor_url + "/wd/hub",
                                                       desired_capabilities=caps),
                                      MyListener())
        logger.info(f"Start session {driver.session_id}")
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
    parser.addoption("--selenoid", action="store", default="localhost")


@pytest.fixture
def browser(request):
    logger = logging.getLogger('browser_fixture')
    logger.setLevel(LOG_LEVEL)
    selenoid = request.config.getoption("--selenoid")
    executor_url = f"http://{selenoid}:4444"
    driver = driver_factory(request.config.getoption("--browser"),
                            executor_url,
                            request.node.name)

    driver.maximize_window()

    def fin():
        log_url = executor_url + f"/logs/{driver.session_id}.log"
        video_url = executor_url + f"/video/{driver.session_id}.mp4"

        driver.quit()

        # Проверяем статус
        if request.node.status == 'failed':
            if url_data_exists(video_url):
                allure.attach(body=requests.get(video_url).content,
                              attachment_type=allure.attachment_type.MP4)

            if url_data_exists(log_url):
                r = requests.get(log_url)
                allure.attach(name="selenoid_log", body=r.text,
                              attachment_type=allure.attachment_type.TEXT)

        # Удаляем данные теста
        if url_data_exists(video_url): requests.delete(url=video_url)
        if url_data_exists(log_url): requests.delete(url=log_url)

    allure.attach(name=driver.session_id,
                  body=str(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)

    request.addfinalizer(fin)
    return driver


@pytest.fixture()
def base_page(browser):
    page = BasePage(browser)
    page.go_to(url="http://demo.opencart.com/")
    # page.go_to(url="http://localhost//")
    return page


@pytest.fixture()
def catalog_page(browser):
    page = CatalogPage(browser)
    page.go_to(url="http://demo.opencart.com/index.php?route=product/category&path=20")
    return page


@pytest.fixture()
def product_card_page(browser):
    page = ProductCardPage(browser)
    page.go_to(url="http://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    return page


@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser)
    page.go_to(url="http://demo.opencart.com/index.php?route=account/login")
    return page


@pytest.fixture()
def login_admin_page(browser):
    page = LoginAdminPage(browser)
    page.go_to(url="http://demo.opencart.com/admin/")
    return page


@pytest.fixture()
def products_table_page(browser):
    page = ProductsTablePage(browser)
    page.go_to(url="http://demo.opencart.com/admin/")
    page.login('demo', 'demo')  # page.login('user', 'bitnami1')
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
        driver.save_screenshot(driver.session_id + 'error.png')

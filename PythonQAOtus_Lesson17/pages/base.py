import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


LOG_LEVEL = 10  # DEBUG


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(LOG_LEVEL)

    def go_to(self, url):
        with allure.step("Открытие url: {}".format(url)):
            self.logger.debug("Открытие url: {}".format(url))
        return self.driver.get(url)

    def title(self, title, timeout=5):
        with allure.step("Проверка обнаружения title: {}".format(title)):
            try:
                self.logger.debug("Проверка обнаружения title: {}".format(title))
                WebDriverWait(self.driver, timeout).until(EC.title_is(title))
            except TimeoutException:
                raise AssertionError("Ждал что title будет: '{}' но он был '{}'".format(title, self.driver.title))

    def element(self, locator, timeout=5):
        with allure.step("Проверка видимости элемента с локатором: {}".format(locator)):
            try:
                self.logger.debug("Проверка видимости элемента с локатором: {}".format(locator))
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Не дождался видимости элемента: {}".format(locator))

    def elements(self, locator, timeout=5):
        with allure.step("Проверка видимости элементов с локатором: {}".format(locator)):
            try:
                self.logger.debug("Проверка видимости элементов с локатором: {}".format(locator))
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
            except TimeoutException:
                raise AssertionError("Не дождался видимости элемента: {}".format(locator))

    def text_in_element(self, locator, text, timeout=3):
        with allure.step("Проверка видимости элемента с локатором: {}".format(locator)):
            try:
                self.logger.debug("Проверка видимости элемента с локатором: {}".format(locator))
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            except TimeoutException:
                raise AssertionError("Не дождался видимости элемента: {}".format(locator))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        return self.driver.get(url)

    def title(self, title, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise TimeoutException("Ждал что title будет: '{}' но он был '{}'".format(title, self.driver.title))

    def element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(locator))

    def elements(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(locator))

    def link(self, locator, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(locator))

    def text_in_element(self, locator, text, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(locator))

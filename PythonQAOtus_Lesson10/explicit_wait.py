from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MyWaits(object):

    def __init__(self, driver):
        self.driver = driver

    def title(self, title, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise TimeoutException("Ждал что title будет: '{}' но он был '{}'".format(title, self.driver.title))

    def element(self, selector, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(selector))

    def elements(self, selector, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(selector))

    def link(self, selector, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, selector)))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(selector))

    def text_in_element(self, selector, text, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, selector), text))
        except TimeoutException:
            raise TimeoutException("Не дождался видимости элемента: {}".format(selector))

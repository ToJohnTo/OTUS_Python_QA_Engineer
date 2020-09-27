from selenium.webdriver.common.by import By
from .base import BasePage


class ProductCardPage(BasePage):
    something_selector = (By.ID, 'something_id')

    def something_func(self):
        pass

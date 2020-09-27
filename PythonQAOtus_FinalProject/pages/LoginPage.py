from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):

    locator_username = (By.CSS_SELECTOR, 'input[type=text]')
    locator_password = (By.CSS_SELECTOR, 'input[type=password]')
    locator_submit_button = (By.CSS_SELECTOR, 'button[type=submit]')

    def _set_username_(self, name):
        self.logger.debug("Очистка поля username")
        self.element(locator=self.locator_username).clear()
        self.logger.debug("Ввод значения '{}' в поле username".format(name))
        self.element(locator=self.locator_username).send_keys(name)

    def _set_password_(self, password):
        self.logger.debug("Очистка поля password")
        self.element(locator=self.locator_password).clear()
        self.logger.debug("Ввод значения '{}' в поле password".format(password))
        self.element(locator=self.locator_password).send_keys(password)

    def login(self, username, password):
        self.logger.info("Ввод имени пользователя и пароля")
        self._set_username_(username)
        self._set_password_(password)
        self.logger.info("Авторизация")
        self.element(locator=self.locator_submit_button).click()

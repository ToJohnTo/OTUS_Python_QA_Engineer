from selenium.webdriver.common.by import By
from .base import BasePage


class LoginAdminPage(BasePage):

    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, '.btn.btn-primary')
    logout_button = (By.XPATH, "/html/body/div[1]/header/div/ul/li[2]/a/i")

    def _set_username_(self, name):
        self.logger.debug("Очистка поля username")
        self.element(locator=self.username).clear()
        self.logger.debug("Ввод значения '{}' в поле username".format(name))
        self.element(locator=self.username).send_keys(name)

    def _set_password_(self, password):
        self.logger.debug("Очистка поля password")
        self.element(locator=self.password).clear()
        self.logger.debug("Ввод значения '{}' в поле password".format(password))
        self.element(locator=self.password).send_keys(password)

    def login(self, username, password):
        self.logger.info("Ввод имени пользователя и пароля")
        self._set_username_(username)
        self._set_password_(password)
        self.logger.info("Авторизация")
        self.element(locator=self.submit_button).click()

    def logout(self):
        self.logger.info("Выход из профиля")
        self.element(locator=self.logout_button).click()

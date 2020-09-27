from selenium.webdriver.common.by import By
from .BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class AdminPage(BasePage):
    locator_menu_button = (By.CSS_SELECTOR, 'div[data-navi-item-name="applicantProfile"]')
    locator_searching_field = (By.CSS_SELECTOR, 'input[type="text"]')
    js_my_resume_tab = 'document.getElementsByClassName("supernova-link HH-Supernova-NaviLevel2-Link")[0].click();'
    # js_create_resume_button = 'document.getElementsByClassName("bloko-button bloko-button_stretched")[1].click();'
    locator_phone_field = (By.CSS_SELECTOR, 'input[data-qa="resume-phone-cell_phone"]')
    js_select_checkbox_experience = 'document.getElementsByClassName("bloko-radio__text")[3].click()'
    locator_save_and_publish_button = (By.CSS_SELECTOR, '.bloko-button.bloko-button_primary.bloko-button_large')
    locator_success_publish = (By.XPATH, '//h2[@class="suitablevacancies__published-head" and text()="Резюме успешно опубликовано"]')

    def logout(self):
        self.logger.info("Выход из профиля")
        self.logger.debug("Нажатие на кнопку меню")
        self.element(locator=self.locator_menu_button).click()
        self.logger.debug("Нажатие на кнопку Выход")
        js = 'document.getElementsByClassName("supernova-dropdown-option HH-Supernova-Menu-Option")[7].click();'
        self.driver.execute_script(js)

    def search(self, search_request):
        self.logger.info("Поиск вакансий")
        self.logger.debug("Очистка поля поисковой строки")
        self.element(locator=self.locator_searching_field).clear()
        self.logger.debug("Вставка запроса '{}' в поле поисковой строки".format(search_request))
        self.element(locator=self.locator_searching_field).send_keys(search_request)
        self.logger.debug("Нажатие на кнопку поиска")
        self.element(locator=self.locator_searching_field).send_keys(Keys.ENTER)

    def create_resume(self):
        self.logger.info("Создание резюме")
        self.logger.debug("Нажатие на вкладку Мои резюме")
        self.driver.execute_script(self.js_my_resume_tab)
        # self.logger.debug("Нажатие на кнопку Создать резюме")
        # self.driver.execute_script(self.js_create_resume_button)
        self.logger.debug("Ввод номера телефона для резюме")
        # self.driver.execute_script(self.js_enter_number_of_phone)
        self.element(locator=self.locator_phone_field).send_keys("9810000001")
        self.logger.debug("Выбор опыта работы в чекбоксе")
        self.driver.execute_script(self.js_select_checkbox_experience)
        self.logger.debug("Нажатие на кнопку Сохранить и опубликовать")
        self.element(locator=self.locator_save_and_publish_button).click()
        self.logger.debug("Нажатие на кнопку Сохранить и опубликовать")
        self.element(locator=self.locator_save_and_publish_button).click()

    def check_success_publish(self):
        self.logger.debug("Проверка успешного опубликования")
        self.element(locator=self.locator_success_publish)

from selenium.webdriver.common.by import By


# url = "http://localhost//"


def test_element_by_id(base_page):
    base_page.logger.info('====== Started ======')
    base_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    base_page.element(locator=(By.CSS_SELECTOR, "#search"))
    base_page.logger.info('====== Finished ======')


def test_elements_by_css_selector(base_page):
    base_page.logger.info('====== Started ======')
    base_page.element(locator=(By.CSS_SELECTOR, ".btn-group.btn-block"))
    base_page.logger.info('====== Finished ======')


def test_element_by_class_name_selector(base_page):
    base_page.logger.info('====== Started ======')
    base_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    base_page.logger.info('====== Finished ======')
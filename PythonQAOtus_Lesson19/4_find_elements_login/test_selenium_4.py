from selenium.webdriver.common.by import By


# url = "http://localhost/index.php?route=account/login"


def test_element_by_id(login_page):
    login_page.logger.info('====== Started ======')
    login_page.element(locator=(By.CSS_SELECTOR, "#content"))
    login_page.element(locator=(By.CSS_SELECTOR, "#column-right"))
    login_page.logger.info('====== Finished ======')


def test_elements_by_css_selector(login_page):
    login_page.logger.info('====== Started ======')
    login_page.elements(locator=(By.CSS_SELECTOR, ".form-control"))
    login_page.logger.info('====== Finished ======')


def test_element_by_class_name_selector(login_page):
    login_page.logger.info('====== Started ======')
    login_page.elements(locator=(By.CSS_SELECTOR, ".control-label"))
    login_page.logger.info('====== Finished ======')

from selenium.webdriver.common.by import By


# url = "http://localhost/index.php?route=product/category&path=20"


def test_element_by_id(catalog_page):
    catalog_page.logger.info('====== Started ======')
    catalog_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    catalog_page.element(locator=(By.CSS_SELECTOR, "#search"))
    catalog_page.logger.info('====== Finished ======')


def test_elements_by_css_selector(catalog_page):
    catalog_page.logger.info('====== Started ======')
    catalog_page.element(locator=(By.CSS_SELECTOR, ".btn-group.btn-block"))
    catalog_page.logger.info('====== Finished ======')


def test_element_by_class_name_selector(catalog_page):
    catalog_page.logger.info('====== Started ======')
    catalog_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    catalog_page.logger.info('====== Finished ======')

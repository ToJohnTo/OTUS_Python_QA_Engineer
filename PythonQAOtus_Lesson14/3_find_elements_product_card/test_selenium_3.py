from selenium.webdriver.common.by import By


# url = "http://localhost/index.php?route=product/product&path=57&product_id=49"


def test_element_by_id(product_card_page):
    product_card_page.logger.info('====== Started ======')
    product_card_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    product_card_page.element(locator=(By.CSS_SELECTOR, "#search"))
    product_card_page.logger.info('====== Finished ======')


def test_elements_by_css_selector(product_card_page):
    product_card_page.logger.info('====== Started ======')
    product_card_page.elements(locator=(By.CSS_SELECTOR, ".thumbnail"))
    product_card_page.logger.info('====== Finished ======')


def test_element_by_class_name_selector(product_card_page):
    product_card_page.logger.info('====== Started ======')
    product_card_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    product_card_page.logger.info('====== Finished ======')

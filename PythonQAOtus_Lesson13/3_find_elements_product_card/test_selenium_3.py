from selenium.webdriver.common.by import By


# url = "http://localhost/index.php?route=product/product&path=57&product_id=49"


def test_element_by_id(product_card_page):
    product_card_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    # browser.find_element(By.ID, "logo")
    product_card_page.element(locator=(By.CSS_SELECTOR, "#search"))
    # browser.find_element_by_id("search")


def test_elements_by_css_selector(product_card_page):
    product_card_page.elements(locator=(By.CSS_SELECTOR, ".thumbnail"))
    # browser.find_elements(By.CSS_SELECTOR, ".thumbnail")


def test_element_by_class_name_selector(product_card_page):
    product_card_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    # browser.find_elements_by_class_name("input-group-btn")

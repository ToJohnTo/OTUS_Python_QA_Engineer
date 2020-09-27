from selenium.webdriver.common.by import By


# url = "http://localhost/index.php?route=product/category&path=20"


def test_element_by_id(catalog_page):
    catalog_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    # browser.find_element(By.ID, "logo")
    catalog_page.element(locator=(By.CSS_SELECTOR, "#search"))
    # browser.find_element_by_id("search")


def test_elements_by_css_selector(catalog_page):
    catalog_page.element(locator=(By.CSS_SELECTOR, ".btn-group.btn-block"))
    # browser.find_elements(By.CSS_SELECTOR, ".btn-group.btn-block")


def test_element_by_class_name_selector(catalog_page):
    catalog_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    # browser.find_elements_by_class_name("input-group-btn")

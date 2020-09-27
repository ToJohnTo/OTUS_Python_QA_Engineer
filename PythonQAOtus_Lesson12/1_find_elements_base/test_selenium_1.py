from selenium.webdriver.common.by import By


# url = "http://localhost//"


def test_element_by_id(base_page):
    base_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    # browser.find_element(By.ID, "logo")
    base_page.element(locator=(By.CSS_SELECTOR, "#search"))
    # browser.find_element_by_id("search")


def test_elements_by_css_selector(base_page):
    base_page.element(locator=(By.CSS_SELECTOR, ".btn-group.btn-block"))
    # browser.find_elements(By.CSS_SELECTOR, ".btn-group.btn-block")


def test_element_by_class_name_selector(base_page):
    base_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    # browser.find_elements_by_class_name("input-group-btn")

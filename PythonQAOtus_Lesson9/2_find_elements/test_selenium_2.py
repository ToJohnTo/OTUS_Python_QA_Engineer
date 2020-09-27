from selenium.webdriver.common.by import By


url = "http://localhost/index.php?route=product/category&path=20"


def test_element_by_id(browser):
    browser.get(url)
    browser.find_element(By.ID, "logo")
    browser.find_element_by_id("search")


def test_element_by_link_text(browser):
    browser.get(url)
    browser.find_element_by_partial_link_text("Laptops")


def test_elements_by_css_selector(browser):
    browser.get(url)
    browser.find_elements(By.CSS_SELECTOR, ".btn-group.btn-block")


def test_element_by_class_name_selector(browser):
    browser.get(url)
    browser.find_elements_by_class_name("input-group-btn")

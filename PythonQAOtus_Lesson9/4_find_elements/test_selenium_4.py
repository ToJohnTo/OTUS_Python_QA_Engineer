from selenium.webdriver.common.by import By


url = "http://localhost/index.php?route=account/login"


def test_element_by_id(browser):
    browser.get(url)
    browser.find_element(By.ID, "content")
    browser.find_element_by_id("column-right")


def test_element_by_link_text(browser):
    browser.get(url)
    browser.find_elements_by_partial_link_text("Address")


def test_elements_by_css_selector(browser):
    browser.get(url)
    browser.find_elements(By.CSS_SELECTOR, ".form-control")


def test_element_by_class_name_selector(browser):
    browser.get(url)
    browser.find_elements_by_class_name("control-label")

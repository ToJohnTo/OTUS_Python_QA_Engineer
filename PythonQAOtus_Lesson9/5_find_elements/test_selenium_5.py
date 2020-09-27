from selenium.webdriver.common.by import By


url = "http://localhost//admin/"


def test_element_by_id(browser):
    browser.get(url)
    browser.find_element(By.ID, "footer")
    browser.find_element_by_id("header").find_element_by_id("header-logo")


def test_element_by_name(browser):
    browser.get(url)
    browser.find_element_by_name("username")


def test_elements_by_css_selector(browser):
    browser.get(url)
    browser.find_elements(By.CSS_SELECTOR, ".input-group-addon")


def test_element_by_class_name_selector(browser):
    browser.get(url)
    browser.find_elements_by_class_name("fa fa-user")

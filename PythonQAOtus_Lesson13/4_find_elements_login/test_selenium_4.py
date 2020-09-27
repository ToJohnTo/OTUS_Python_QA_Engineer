from selenium.webdriver.common.by import By


# url = "http://localhost/index.php?route=account/login"


def test_element_by_id(login_page):
    login_page.element(locator=(By.CSS_SELECTOR, "#content"))
    # browser.find_element(By.ID, "content")
    login_page.element(locator=(By.CSS_SELECTOR, "#column-right"))
    # browser.find_element_by_id("column-right")


def test_elements_by_css_selector(login_page):
    login_page.elements(locator=(By.CSS_SELECTOR, ".form-control"))
    # browser.find_elements(By.CSS_SELECTOR, ".form-control")


def test_element_by_class_name_selector(login_page):
    login_page.elements(locator=(By.CSS_SELECTOR, ".control-label"))
    # browser.find_elements_by_class_name("control-label")

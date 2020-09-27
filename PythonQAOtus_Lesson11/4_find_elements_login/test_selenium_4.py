from explicit_wait import MyWaits


url = "http://localhost/index.php?route=account/login"


def test_element_by_id(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.element("#content")
    # browser.find_element(By.ID, "content")
    my_waits.element("#column-right")
    # browser.find_element_by_id("column-right")


def test_elements_by_css_selector(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.elements(".form-control")
    # browser.find_elements(By.CSS_SELECTOR, ".form-control")


def test_element_by_class_name_selector(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.elements(".control-label")
    # browser.find_elements_by_class_name("control-label")

from explicit_wait import MyWaits


url = "http://localhost//admin/"


def test_login(browser):
    """ Check login """
    my_waits = MyWaits(browser)
    browser.get(url)
    # login
    my_waits.element("#input-username").send_keys("user")
    # password
    my_waits.element("#input-password").send_keys("bitnami1")
    # button of login
    btn_login = my_waits.element(".btn.btn-primary")
    btn_login.click()
    # Find user account on page
    my_waits.element("#user-profile", timeout=15)    # big timeout special for firefox


def test_unlogin(browser):
    """ Check unlogin """
    my_waits = MyWaits(browser)
    # Login
    test_login(browser)
    # Logout
    my_waits.element(".fa.fa-sign-out").click()
    # Find login on page
    my_waits.element("#input-username")


def test_products_table(browser):
    """ Check transfer to Catalog/Products and check table """
    my_waits = MyWaits(browser)
    # Login
    test_login(browser)
    # Press Catalog
    my_waits.element(".fa.fa-tags.fw").click()
    # Press Products
    catalog = browser.find_element_by_id("collapse1")
    catalog_table = catalog.find_elements_by_tag_name("li")
    # catalog = my_waits.element("#collapse1")        # так сделать не удаётся, т.к. возращается WebElement
    # catalog_table = MyWaits(catalog).elements("li") # после чего повторно использовать метод elemen(s) нельзя
    for el in catalog_table:
        if el.text == "Products":
            btn_products = el
    btn_products.click()
    # Check table is
    my_waits.element("#form-product")


def test_element_by_id(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.element("#footer")
    # browser.find_element(By.ID, "footer")
    my_waits.element("#footer")
    my_waits.element("#header-logo")
    # browser.find_element_by_id("header").find_element_by_id("header-logo")


def test_element_by_name(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.element("[name=username]")
    # browser.find_element_by_name("username")


def test_elements_by_css_selector(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.elements(".input-group-addon")
    # browser.find_elements(By.CSS_SELECTOR, ".input-group-addon")


def test_element_by_class_name_selector(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.elements(".fa.fa-user")
    # browser.find_elements_by_class_name("fa fa-user")

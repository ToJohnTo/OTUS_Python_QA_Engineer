from explicit_wait import MyWaits
from selenium.webdriver.common.alert import Alert
import time


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
    for el in catalog_table:
        if el.text == "Products":
            btn_products = el
            btn_products.click()
            break
    # Check table is
    my_waits.element("#form-product")


def test_products_add_product(browser):
    """ Check add product to products table """
    my_waits = MyWaits(browser)
    # Go to page products table (General page)
    test_products_table(browser)
    # Press Add Product Button
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    # Enter Product Name
    my_waits.element("#input-name1").send_keys("ex_name_1")
    # Enter Product Tag Name
    browser.find_element_by_css_selector("#input-meta-title1").send_keys("ex_tag_1")
    # Go to Data page
    table_title = browser.find_element_by_css_selector("#form-product")
    table_title_list = table_title.find_elements_by_tag_name("li")
    for el in table_title_list:
        if el.text == "Data":
            btn_data = el
            btn_data.click()
            break
    # Enter Product Name
    my_waits.element("#input-model").send_keys("ex_model_1")
    # Press Save Button
    browser.find_elements_by_css_selector(".pull-right")[3].find_element_by_tag_name("button").click()
    # Check success after add product
    my_waits.element(".alert.alert-success.alert-dismissible")
    assert \
        browser.find_element_by_css_selector(".alert.alert-success.alert-dismissible").get_property("innerText")\
        == \
        " Success: You have modified products!\n×"


def test_products_modify_product(browser):
    """ Check modify product in products table """
    my_waits = MyWaits(browser)
    test_products_add_product(browser)
    # Find line with product
    lines = browser.find_element_by_css_selector(".table.table-bordered.table-hover").find_elements_by_tag_name("tr")
    flag_out_of_loop = False
    for line in lines:
        elements = line.get_property("cells")
        for el in elements:
            if el.get_property("innerText") == "ex_name_1":
                # Press Edit Button
                line.find_element_by_css_selector(".fa.fa-pencil").click()
                flag_out_of_loop = True
                break
        if flag_out_of_loop:
            break
    # Clear Product Name
    my_waits.element("#input-name1").clear()
    # Enter new Product Name
    my_waits.element("#input-name1").send_keys("1_new_ex_name_1")
    # Press Save Button
    browser.find_elements_by_css_selector(".pull-right")[3].find_element_by_tag_name("button").click()
    # Check success after add product
    my_waits.element(".alert.alert-success.alert-dismissible")
    assert \
        browser.find_element_by_css_selector(".alert.alert-success.alert-dismissible").get_property("innerText") \
        == \
        " Success: You have modified products!\n×"


def test_products_remove_product(browser):
    """ Check remove product from products table """
    my_waits = MyWaits(browser)
    test_products_add_product(browser)
    # Find line with product
    lines = browser.find_element_by_css_selector(".table.table-bordered.table-hover").find_elements_by_tag_name("tr")
    for line in lines:
        if "ex_name_1" in line.get_property("innerText"):
            # Select product for remove
            line.find_elements_by_tag_name("td")[0].click()
            flag_out_of_loop = True
            break
    # Press Trash Button
    browser.find_element_by_css_selector(".fa.fa-trash-o").click()
    # Confirm alert message
    Alert(browser).accept()
    # Check success after remove product
    my_waits.element(".alert.alert-success.alert-dismissible")
    assert \
        browser.find_element_by_css_selector(".alert.alert-success.alert-dismissible").get_property("innerText") \
        == \
        " Success: You have modified products!\n×"


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

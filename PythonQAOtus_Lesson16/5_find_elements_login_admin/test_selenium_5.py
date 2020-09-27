
def test_login(login_admin_page):
    """ Check login """
    login_admin_page.logger.info('====== Started ======')
    login_admin_page.login('demo', 'demo')      # login_admin_page.login('user', 'bitnami1')
    assert login_admin_page.driver.title == 'Dashboard'
    login_admin_page.logger.info('====== Finished ======')


def test_unlogin(login_admin_page):
    """ Check unlogin """
    login_admin_page.logger.info('====== Started ======')
    # Login
    test_login(login_admin_page)
    # Logout
    login_admin_page.logout()
    assert login_admin_page.driver.title == 'Administration'
    login_admin_page.logger.info('====== Finished ======')


def test_products_table(products_table_page):
    """ Check transfer to Catalog/Products and check table """
    products_table_page.logger.info('====== Started ======')
    assert products_table_page.driver.title == 'Products'
    products_table_page.logger.info('====== Finished ======')


def test_products_add_product(products_table_page):
    """ Check add product to products table """
    products_table_page.logger.info('====== Started ======')
    # Go to page products table (General page)
    test_products_table(products_table_page)
    # Add new product
    products_table_page.add_new_product(name="ex_name_1", tag="ex_tag_1", model="ex_model_1")
    assert \
        products_table_page.driver.find_element_by_css_selector(".alert.alert-success.alert-dismissible").get_property("innerText")\
        == \
        " Success: You have modified products!\n×"
    products_table_page.logger.info('====== Finished ======')


def test_products_modify_product(products_table_page):
    """ Check modify product in products table """
    products_table_page.logger.info('====== Started ======')
    # Prepare for test - add product
    test_products_add_product(products_table_page)
    # Modify product
    products_table_page.modify_product_name(new_name="1_new_ex_name_1")
    assert \
        products_table_page.driver.find_element_by_css_selector(".alert.alert-success.alert-dismissible").get_property("innerText") \
        == \
        " Success: You have modified products!\n×"
    products_table_page.logger.info('====== Finished ======')


def test_products_remove_product(products_table_page):
    """ Check remove product from products table """
    products_table_page.logger.info('====== Started ======')
    # Prepare for test - add product
    test_products_add_product(products_table_page)
    # Remove product
    products_table_page.remove_product_with(name="ex_name_1")
    assert \
        products_table_page.driver.find_element_by_css_selector(".alert.alert-success.alert-dismissible").get_property("innerText") \
        == \
        " Success: You have modified products!\n×"
    products_table_page.logger.info('====== Finished ======')


def test_negative_login_bad_username(login_admin_page):
    login_admin_page.logger.info('====== Started ======')
    login_admin_page.login('', 'bitnami1')
    assert login_admin_page.driver.title != 'Dashboard'
    login_admin_page.logger.info('====== Finished ======')


def test_negative_login_bad_password(login_admin_page):
    login_admin_page.logger.info('====== Started ======')
    login_admin_page.login('user', '')
    assert login_admin_page.driver.title != 'Dashboard'
    login_admin_page.logger.info('====== Finished ======')


def test_negative_login_bad_all(login_admin_page):
    login_admin_page.logger.info('====== Started ======')
    login_admin_page.login('', '')
    assert login_admin_page.driver.title != 'Dashboard'
    login_admin_page.logger.info('====== Finished ======')


def test_add_product_logout(products_table_page):
    products_table_page.logger.info('====== Started ======')
    products_table_page.add_new_product(name="test_name1", tag="test_tag1", model="test_model1")
    products_table_page.logout()
    assert products_table_page.driver.title == 'Administration'
    products_table_page.logger.info('====== Finished ======')


def test_add_product_remove_logout(products_table_page):
    products_table_page.logger.info('====== Started ======')
    products_table_page.add_new_product(name="test_name2", tag="test_tag2", model="test_model2")
    products_table_page.remove_product_with(name="test_name2")
    products_table_page.logout()
    assert products_table_page.driver.title == 'Administration'
    products_table_page.logger.info('====== Finished ======')

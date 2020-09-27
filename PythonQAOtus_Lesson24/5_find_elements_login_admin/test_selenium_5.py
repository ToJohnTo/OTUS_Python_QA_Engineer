
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


def test_login(login_admin_page):
    """ Check login """
    login_admin_page.logger.info('====== Started ======')
    login_admin_page.login('user', 'bitnami1')
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


def test_products_add_product(products_table_page, db_connect):
    """ Check add product to products table """
    products_table_page.logger.info('====== Started ======')
    # Go to page products table (General page)
    test_products_table(products_table_page)
    # Add new product
    name = "ex_name_1"
    tag = "ex_tag_1"
    model = "ex_model_1"
    products_table_page.add_new_product(name=name, tag=tag, model=model)
    # Check that new product added
    query = f"""
        SELECT oc_product_description.name, oc_product_description.meta_title, oc_product.model
        FROM oc_product_description, oc_product
        WHERE oc_product_description.name=\"{name}\"
            AND oc_product_description.meta_title=\"{tag}\"
            AND oc_product.model=\"{model}\"
    """
    db_connect.execute(query)
    result = db_connect.fetchall()
    products_table_page.logger.info(result)
    ids = [i[0] for i in result]
    products_table_page.logger.info(ids)
    assert len(ids) != 0, 'Добавление произведено успешно'
    products_table_page.logger.info('====== Finished ======')


def test_products_remove_product(products_table_page, db_connect):
    """ Check remove product from products table """
    products_table_page.logger.info('====== Started ======')
    data1 = (666, 1, 'ex_name_1', 'ex_tag_1')
    data2 = (666, 'ex_model_1')
    ins1 = f"INSERT INTO oc_product_description (product_id, language_id, name, meta_title) VALUES {data1}"
    ins2 = f"INSERT INTO oc_product (product_id, model) VALUES {data2}"
    db_connect.execute(ins1)
    db_connect.execute(ins2)
    # Remove product
    name = "new_name_1"
    products_table_page.remove_product_with(name=name)
    # Check that product removed
    query = f"""
        SELECT *
        FROM oc_product_description
        WHERE name=\"{name}\"
    """
    db_connect.execute(query)
    result = db_connect.fetchall()
    products_table_page.logger.info(result)
    ids = [i[0] for i in result]
    products_table_page.logger.info(ids)
    assert len(ids) == 0, 'Удаление произведено успешно'
    products_table_page.logger.info('====== Finished ======')


def test_products_modify_product(products_table_page, db_connect):
    """ Check modify product in products table """
    products_table_page.logger.info('====== Started ======')
    # Prepare for test - add product
    data1 = (777, 1, 'ins_name_1', 'ins_tag_1')
    data2 = (777, 'ins_model_1')
    ins1 = f"INSERT INTO oc_product_description (product_id, language_id, name, meta_title) VALUES {data1}"
    ins2 = f"INSERT INTO oc_product (product_id, model) VALUES {data2}"
    db_connect.execute(ins1)
    db_connect.execute(ins2)
    # Modify product
    new_name = "1_new_ex_name_1"
    products_table_page.modify_product_name(new_name=new_name)
    # Check that product modified
    query = f"""
        SELECT *
        FROM oc_product_description
        WHERE name=\"{new_name}\"
    """
    db_connect.execute(query)
    result = db_connect.fetchall()
    products_table_page.logger.info(result)
    ids = [i[0] for i in result]
    products_table_page.logger.info(ids)
    assert len(ids) != 0, 'Модификация произведена успешно'
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

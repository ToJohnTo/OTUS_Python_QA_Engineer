from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from .login_admin import LoginAdminPage


class ProductsTablePage(LoginAdminPage):

    catalog_button = (By.CSS_SELECTOR, ".fa.fa-tags.fw")
    add_product_button = (By.CSS_SELECTOR, ".btn.btn-primary")
    product_name_field = (By.CSS_SELECTOR, "#input-name1")
    product_tag_field = (By.CSS_SELECTOR, "#input-meta-title1")
    product_model_field = (By.CSS_SELECTOR, "#input-model")
    trash_button = (By.CSS_SELECTOR, ".fa.fa-trash-o")
    modify_success_alert = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def open_products_table(self):
        # Press Catalog
        self.element(locator=self.catalog_button).click()
        # Press Products
        catalog = self.driver.find_element_by_id("collapse1")
        catalog_table = catalog.find_elements_by_tag_name("li")
        for el in catalog_table:
            if el.text == "Products":
                btn_products = el
                btn_products.click()
                break

    def add_new_product(self, name, tag, model):
        # Press Add Product Button
        self.element(locator=self.add_product_button).click()
        # Enter Product Name
        self.element(locator=self.product_name_field).send_keys(name)
        # Enter Product Tag Name
        self.element(locator=self.product_tag_field).send_keys(tag)
        # Go to Data page
        table_title = self.driver.find_element_by_css_selector("#form-product")
        table_title_list = table_title.find_elements_by_tag_name("li")
        for el in table_title_list:
            if el.text == "Data":
                btn_data = el
                btn_data.click()
                break
        # Enter Product Model
        self.element(locator=self.product_model_field).send_keys(model)
        # Press Save Button
        self.driver.find_elements_by_css_selector(".pull-right")[3].find_element_by_tag_name("button").click()
        # Check success after add product
        self.element(locator=self.modify_success_alert)

    def modify_product_name(self, new_name):
        # Find line with product
        lines = self.driver.find_element_by_css_selector(
            ".table.table-bordered.table-hover").find_elements_by_tag_name("tr")
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
        self.element(locator=self.product_name_field).clear()
        # Enter new Product Name
        self.element(locator=self.product_name_field).send_keys(new_name)
        # Press Save Button
        self.driver.find_elements_by_css_selector(".pull-right")[3].find_element_by_tag_name(
            "button").click()
        # Check success after add product
        self.element(locator=self.modify_success_alert)

    def remove_product_with(self, name):
        # Find line with product
        lines = self.driver.find_element_by_css_selector(".table.table-bordered.table-hover"). \
            find_elements_by_tag_name("tr")
        for line in lines:
            if name in line.get_property("innerText"):
                # Select product for remove
                line.find_elements_by_tag_name("td")[0].click()
                flag_out_of_loop = True
                break
        # Press Trash Button
        self.element(locator=self.trash_button).click()
        # Confirm alert message
        Alert(self.driver).accept()
        # Check success after remove product
        # self.element(locator=self.modify_success_alert)

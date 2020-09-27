from selenium.webdriver.common.by import By


# url = "http://localhost//"


def test_element_by_id(base_page):
    base_page.logger.info('====== Started ======')
    base_page.element(locator=(By.CSS_SELECTOR, "#logo"))
    base_page.element(locator=(By.CSS_SELECTOR, "#search"))
    base_page.logger.info('====== Finished ======')


def test_elements_by_css_selector(base_page):
    base_page.logger.info('====== Started ======')
    base_page.element(locator=(By.CSS_SELECTOR, ".btn-group.btn-block"))
    base_page.logger.info('====== Finished ======')


def test_element_by_class_name_selector(base_page):
    base_page.logger.info('====== Started ======')
    base_page.elements(locator=(By.CSS_SELECTOR, ".input-group-btn"))
    base_page.logger.info('====== Finished ======')


def test_logging_browser(base_page):
    base_page.driver.execute_script("console.warn('Here is the WARNING message!')")
    base_page.driver.execute_script("console.error('Here is the ERROR message!')")
    base_page.driver.execute_script("console.log('Here is the LOG message!')")

    # Логиирование производительности страницы
    base_page.logger.info("Логиирование производительности страницы")
    performance_log = base_page.driver.get_log("performance")
    base_page.logger.info("Не вывожу - очень длинная портянка. Если потребуется, раскомментить код ниже.")
    # for log in performance_log:
    #     base_page.logger.info(log)

    # Логи консоли браузера - собирает WARNINGS, ERRORS
    base_page.logger.info("Логиирование консоли браузера")
    browser_log = base_page.driver.get_log("browser")
    for log in browser_log:
        base_page.logger.info(log)

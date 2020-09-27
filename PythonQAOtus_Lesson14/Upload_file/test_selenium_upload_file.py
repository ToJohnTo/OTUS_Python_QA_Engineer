import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file"


def test_upload_file(upload_file_mozilla_page):
    """ Check upload """
    dirname = os.path.dirname("/home/john/Study/OTUS/PythonQAOtus_Lesson13/Upload_file/")
    filename = os.path.join(dirname, "1.jpeg")
    iframe = upload_file_mozilla_page.elements(locator=(By.CSS_SELECTOR, "iframe"))
    upload_file_mozilla_page.driver.switch_to.frame(iframe[3])
    upload_file_mozilla_page.driver.execute_script('document.getElementById("image_uploads").style.opacity = "1"')
    input_manager = upload_file_mozilla_page.element(locator=(By.CSS_SELECTOR, "#image_uploads"))
    input_manager.send_keys(filename)
    button_sumbit = upload_file_mozilla_page.element(locator=(By.CSS_SELECTOR, "button"))
    button_sumbit.send_keys(Keys.ENTER)

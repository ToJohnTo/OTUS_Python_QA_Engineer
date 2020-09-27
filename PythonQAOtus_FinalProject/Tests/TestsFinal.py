import allure
import time


@allure.feature('Bad Authentication')
@allure.story('test1')
@allure.title("Test check bad try(empty username field) for login on hh.ru")
def test_negative_login_bad_username(login_page):
    """ Check login with bad username """
    login_page.logger.info('====== Started ======')
    login_page.login('', 'bitnami1')
    assert login_page.driver.current_url == 'https://spb.hh.ru/account/login'
    login_page.logger.info('====== Finished ======')


@allure.feature('Bad Authentication')
@allure.story('test2')
@allure.title("Test check bad try(empty password field) for login on hh.ru")
def test_negative_login_bad_password(login_page):
    """ Check login with bad password """
    login_page.logger.info('====== Started ======')
    login_page.login('user', '')
    assert login_page.driver.current_url == 'https://spb.hh.ru/account/login'
    login_page.logger.info('====== Finished ======')


@allure.feature('Bad Authentication')
@allure.story('test3')
@allure.title("Test check bad try(empty username and password fields) for login on hh.ru")
def test_negative_login_bad_all(login_page):
    """ Check login with bad username and password """
    login_page.logger.info('====== Started ======')
    login_page.login('', '')
    assert login_page.driver.current_url == 'https://spb.hh.ru/account/login'
    login_page.logger.info('====== Finished ======')


@allure.feature('Create resume')
@allure.story('test1')
@allure.title("Test check create resume on hh.ru")
def test_create_resume(admin_page):
    """ Check create resume """
    admin_page.logger.info('====== Started ======')
    admin_page.create_resume()
    admin_page.check_success_publish()
    admin_page.logger.info('====== Finished ======')


@allure.feature('Good Authentication')
@allure.story('test1')
@allure.title("Test check login on hh.ru")
def test_login(login_page):
    """ Check login """
    login_page.logger.info('====== Started ======')
    login_page.login(
        username='otus_final_project@mail.ru',
        password='Otus25082020'
    )
    assert login_page.driver.current_url != 'https://spb.hh.ru/account/login'
    login_page.logger.info('====== Finished ======')


@allure.feature('Good Authentication')
@allure.story('test2')
@allure.title("Test check unlogin from hh.ru")
def test_unlogin(admin_page):
    """ Check unlogin """
    admin_page.logger.info('====== Started ======')
    # Logout
    admin_page.logout()
    time.sleep(3)
    assert admin_page.driver.current_url == 'https://spb.hh.ru/'
    admin_page.logger.info('====== Finished ======')


@allure.feature('Search')
@allure.story('test1')
@allure.title("Test check search vacancy on hh.ru")
def test_search(admin_page):
    """ Check search """
    admin_page.logger.info('====== Started ======')
    admin_page.search("тестировщик")
    time.sleep(3)
    assert admin_page.driver.current_url == 'https://spb.hh.ru/vacancies/testirovshik'
    admin_page.logger.info('====== Finished ======')

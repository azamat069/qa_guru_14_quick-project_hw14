from pages.main_page import main_page
import allure
from allure_commons.types import Severity


class TestAuth:

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.feature('Авторизация')
    @allure.story('Тест открытия модального окна авторизации')
    def test_auth_modal(self):
        main_page.open_main_page()
        main_page.click_auth_button()
        main_page.check_auth_modal_is_opened()

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.feature('Авторизация')
    @allure.story('Тест добавления тест кейса в allure testops')
    def test_add_case_to_testops(self):
        main_page.open_main_page()

from allure_commons.types import Severity
from pages.main_page import main_page
import allure


class TestHeaders:

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Хедеры')
    @allure.story('Тест открытия странцы "Это как"')
    def test_open_how_to_page(self):
        main_page.open_main_page()
        main_page.open_how_to_page()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Хедеры')
    @allure.story('Тест открытия странцы "Это баг"')
    def test_open_debug_page(self):
        main_page.open_main_page()
        main_page.open_debug_page()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Хедеры')
    @allure.story('Тест открытия странцы "Как решить"')
    def test_open_zadacha_page(self):
        main_page.open_main_page()
        main_page.open_zadacha_page()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Хедеры')
    @allure.story('Тест перехода на главную станицу по клику на лого сайта"')
    def test_click_main_page_logo(self):
        main_page.open_main_page()
        main_page.open_debug_page()
        main_page.click_to_main_page_label()

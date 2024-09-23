from allure_commons.types import Severity
from pages.main_page import search, main_page
import allure


class TestSearchField:

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Поиск')
    @allure.story('Тест открытия поискового поля')
    def test_open_search_field(self):
        main_page.open_main_page()
        search.click_search_button()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Поиск')
    @allure.story('Тест ввода текста в поле поиска')
    def test_type_search_field(self):
        main_page.open_main_page()
        search.click_search_button()
        search.type_in_search_field('python')
        search.assert_search_results()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Поиск')
    @allure.story('Тест ввод некорректного текста в поле поиска')
    def test_type_incorrect_text_in_search_field(self):
        main_page.open_main_page()
        search.click_search_button()
        search.type_in_search_field('fsdjkfsdg')
        search.assert_search_results()

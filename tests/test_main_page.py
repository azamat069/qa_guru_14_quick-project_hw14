from allure_commons.types import Severity
from pages.main_page import main_page
import allure


class TestMainPage:

    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.feature('Главная страница')
    @allure.story('Тест открытия главной страницы')
    def test_open_main_page(self):
        main_page.open_main_page()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест переключание на вкладку "Задачи"')
    def test_switch_on_popular_tab(self):
        main_page.open_main_page()
        main_page.click_on_popular_tab()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест переключание на вкладку "Полезное"')
    def test_switch_on_news_tab(self):
        main_page.open_main_page()
        main_page.click_on_popular_tab()
        main_page.click_on_news_tab()

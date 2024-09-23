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
    @allure.story('Тест отображения виджета на главной сранице')
    def test_main_widget_is_enabled(self):
        main_page.open_main_page()
        main_page.widget_is_visible_on_main_page()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест переключание на вкладку "Задачи"')
    def test_switch_to_popular_tab(self):
        main_page.open_main_page()
        main_page.click_on_popular_tab()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест колличества статей во вкладке "Задачи"')
    def test_popular_tab_have_three_articles(self):
        main_page.open_main_page()
        main_page.click_on_popular_tab()
        main_page.is_three_articles_in_popular_tab()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест переключание на вкладку "Полезное"')
    def test_switch_to_news_tab(self):
        main_page.open_main_page()
        main_page.click_on_popular_tab()
        main_page.click_on_news_tab()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест колличества статей во вкладке "Поясняем"')
    def test_news_tab_have_three_articles(self):
        main_page.open_main_page()
        main_page.is_three_articles_in_new_tab()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест открытия статьи "Python для новичнов" в новой вкладке')
    def test_click_python_for_inners_widget(self):
        main_page.open_main_page()
        main_page.widget_python_for_inners_is_visible()
        main_page.close_block_widget()
        main_page.click_widget_python_for_inners()
        main_page.switch_browser_tab()
        main_page.assert_widget_python_for_inners_title()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест отправки формы подписки на рассылку')
    def test_click_check_box_personal_data_agree(self):
        main_page.open_main_page()
        main_page.subscribe_widget_is_visible()
        main_page.close_block_widget()
        main_page.type_email_field_in_subscribe_widget('villiam_jones@icloud.com')
        main_page.click_check_box_personal_data_agree()
        main_page.shoud_be_check_box_personal_data_agree_is_active()

    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.feature('Главная страница')
    @allure.story('Тест кнопки "Что там дальше?"')
    def test_click_load_more_button(self):
        main_page.open_main_page()
        main_page.scroll_to_load_more_button()
        main_page.close_block_widget()
        main_page.click_load_more_button()
        main_page.check_load_more_articles()

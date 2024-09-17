from selene import browser, have, be, query
import allure


class MainPage:

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        browser.open('/')
        assert browser.get(query.url) == 'https://thecode.media/'

    @allure.step('Переходим на страницу "Это как"')
    def open_how_to_page(self):
        browser.element('.menu-item-3592').click()
        browser.element('[class="search__title"]').should(have.text('Это как'))

    @allure.step('Переходим на страницу "Это баг"')
    def open_debug_page(self):
        browser.element('.menu-item-3593').click()
        browser.element('[class ="search__title"]').should(have.text('Это баг'))

    @allure.step('Переходим на страницу "Как решить"')
    def open_zadacha_page(self):
        browser.element('.menu-item-3594').click()
        browser.element('[class="search__title"]').should(have.text('Как решить'))

    @allure.step('Клик по лого сайта')
    def click_to_main_page_label(self):
        browser.element('[class="heading-logo__thecode"]').click()
        assert browser.get(query.url) == 'https://thecode.media/'

    @allure.step('Клик по иконке поиска')
    def click_search_button(self):
        browser.element('[class="heading-search__open"]').click()
        browser.element('[class="heading-search__input"]').should(be.visible)

    @allure.step('Ввод текста в поле поиска {search_text_value}')
    def type_in_search_field(self, search_text_value):
        search_field = browser.element('[class="heading-search__input"]')
        search_field.clear()
        search_field.should(be.blank)
        search_field.type(search_text_value).press_enter()
        browser.element('[class="search__title"]').should(have.text(search_text_value))

    @allure.step('Ввод некорректного текста в поле поиска {incorrect_text_value}')
    def type_incorrect_text_in_search_field(self, incorrect_text_value):
        search_field = browser.element('[class="heading-search__input"]')
        search_field.clear()
        search_field.should(be.blank)
        search_field.type(incorrect_text_value).press_enter()
        browser.element('[class="search__title"]').should(have.text(incorrect_text_value))
        browser.element('[class="search__title search__titleNotFound"]').should(
            have.text('По вашему запросу ничего не найдено'))

    @allure.step('Клик по кнопке авторизации')
    def click_auth_button(self):
        browser.element('[class="heading-user"]').click()
        browser.element('[class="login-popup-inner"]').should(be.visible)
        browser.element('[class="login-popup__title"]').should(have.text('Войдите, чтобы следить за любимыми темами'))
        browser.element('[class="wp-social-login-provider wp-social-login-provider-yandex"]').should(have.text('Войти'))
        browser.element('[class="login-popup__close"]').click()
        browser.element('[class="login-popup-inner"]').should(be.not_.visible)

    @allure.step('Клик по вкладке "Задачи" на виджете')
    def click_on_popular_tab(self):
        browser.element('[class="main-widget-tab tab-popular tab-questions"]').click()
        browser.element('[class="main-widget main-widget-popular--active"]').should(be.enabled)

    @allure.step('Клик по вкладке "Полезное" на виджете')
    def click_on_news_tab(self):
        browser.element('[class="main-widget-tab tab-news"]').click()
        browser.element('[class="main-widget main-widget-news--active"]').should(be.enabled)


main_page = MainPage()

from selene import browser, have, be, query, command
import allure


class MainPage:

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        browser.open('/')
        assert browser.get(query.url) == 'https://thecode.media/'

    @allure.step('Клик по кнопке авторизации')
    def click_auth_button(self):
        browser.element('[class="heading-user"]').click()

    @allure.step('Проверка успешного открытия модального окна авторизации')
    def check_auth_modal_is_opened(self):
        browser.element('[class="login-popup-inner"]').should(be.visible)
        browser.element('[class="login-popup__title"]').should(have.text('Войдите, чтобы следить за любимыми темами'))
        browser.element('[class="wp-social-login-provider wp-social-login-provider-yandex"]').should(have.text('Войти'))
        browser.element('[class="login-popup__close"]').click()
        browser.element('[class="login-popup-inner"]').should(be.not_.visible)

    @allure.step('Проверка отображения виджета на главной странице')
    def widget_is_visible_on_main_page(self):
        browser.element('[class="main-widget-inner main-widget-news"]').should(be.visible)

    @allure.step('В виджете главной страницы во вкладке "Задачи" отображается три статьи')
    def is_three_articles_in_popular_tab(self):
        browser.element('[class="main-widget-inner main-widget-popular main-widget-questions"]').perform(
            command.js.scroll_into_view)
        browser.all('.main-widget-inner.main-widget-popular.main-widget-questions .main-widget-post').should(
            have.size(3))

    @allure.step('В виджете главной страницы во вкладке "Поясняем" отображается три статьи')
    def is_three_articles_in_new_tab(self):
        browser.element('[class="main-widget-inner main-widget-popular main-widget-questions"]').perform(
            command.js.scroll_into_view)
        browser.all('.main-widget-inner.main-widget-news .main-widget-post').should(
            have.size(3))

    @allure.step('Клик по вкладке "Задачи" на виджете')
    def click_on_popular_tab(self):
        browser.element('[class="main-widget-tab tab-popular tab-questions"]').click()
        browser.element('[class="main-widget main-widget-popular--active"]').should(be.enabled)

    @allure.step('Клик по вкладке "Полезное" на виджете')
    def click_on_news_tab(self):
        browser.element('[class="main-widget-tab tab-news"]').click()
        browser.element('[class="main-widget main-widget-news--active"]').should(be.enabled)

    @allure.step('Клик по кнопке закрытия блокирующего виджета')
    def close_block_widget(self):
        if browser.element('[class="adfox-bottom adfox-bottom-link__desk"]').wait_until(be.visible):
            browser.element('[class="adfox-bottom-close"]').click()

    @allure.step('Виджет "Python для новичков" отображается на странице')
    def widget_python_for_inners_is_visible(self):
        browser.element('[class="b-python-inner"]').perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element('[class="b-python-title"]').should(have.text('Python с нуля'))

    @allure.step('Клик по виджету "Python для новичков"')
    def click_widget_python_for_inners(self):
        browser.element('[class="b-python-btn"]').perform(
            command.js.scroll_into_view).should(be.visible).click()

    @allure.step('Переход на новую вкладку')
    def switch_browser_tab(self):
        tabs = browser.driver.window_handles
        browser.driver.switch_to.window(tabs[1])

    @allure.step('Открылась новая вкладка, проверка заголовка статьи')
    def assert_widget_python_for_inners_title(self):
        browser.element('[class="mastrids-title"]').should(have.text('Язык программирования Python'))

    @allure.step('Скролл страницы к виджету подписки на рассылку')
    def subscribe_widget_is_visible(self):
        browser.element('[class="main-subscribe"]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element('[class="main-subscribe__title"]').should(
            have.text('Один мальчик подписался на рассылку Кода и постепенно стал программистом'))

    @allure.step('Ввод электронной почты в поле email')
    def type_email_field_in_subscribe_widget(self, email):
        browser.element('[class="main-subscribe__input"]').should(be.blank).type(email)

    @allure.step('Клик по чек боксу согласия на обработку персональных данных')
    def click_check_box_personal_data_agree(self):
        browser.element('[class="main-subscribe-checkbox"]').click()

    @allure.step('Проверка активности кнопки "Отправить"')
    def shoud_be_check_box_personal_data_agree_is_active(self):
        browser.element('[class="main-subscribe-checkbox main-subscribe-checkbox--active"]').perform(
            command.js.scroll_into_view).should(be.enabled)

    @allure.step('Скролл страницы к кнопке "Что там дальше?"')
    def scroll_to_load_more_button(self):
        browser.element('[class="alm-load-more-btn more "]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element('[class="alm-load-more-btn more "]').should(have.text('Что там дальше?'))

    @allure.step('Клик по кнопке "Что там дальше?"')
    def click_load_more_button(self):
        browser.element('[class="alm-load-more-btn more "]').click()

    @allure.step('Проверка отображения дополнительных статей(12шт.)')
    def check_load_more_articles(self):
        browser.all('.alm-reveal .post').should(have.size(12))


main_page = MainPage()


class SearchField:

    def __init__(self):
        self.search_text_value = None

    @allure.step('Клик по иконке поиска')
    def click_search_button(self):
        browser.element('[class="heading-search__open"]').click()
        browser.element('[class="heading-search__input"]').should(be.visible)

    @allure.step('Ввод текста в поле поиска {search_text_value}')
    def type_in_search_field(self, search_text_value):
        self.search_text_value = search_text_value
        search_field = browser.element('[class="heading-search__input"]')
        search_field.clear()
        search_field.should(be.blank)
        search_field.type(search_text_value).press_enter()

    @allure.step('Проверка результатов поиска')
    def assert_search_results(self):
        if browser.element('[class="search__amount"]').wait_until(be.visible):
            browser.element('[class="search__title"]').should(have.text(self.search_text_value))
            result = browser.element('[class="post-text"]').locate().text
            assert self.search_text_value in result.lower(), f'{self.search_text_value} не отображается в результате'
        elif browser.element('[class="search__amount"]').wait_until(be.not_.visible):
            browser.element('[class="search__title search__titleNotFound"]').should(
                have.text('По вашему запросу ничего не найдено'))
        else:
            raise AssertionError("Ошибка отображения страницы результатов поиска")


search = SearchField()

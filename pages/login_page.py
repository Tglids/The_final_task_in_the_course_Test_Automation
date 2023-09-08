from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'Подстроки "login" нет в текущем url'

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except:
            assert False, 'Форма аутентификации не найдена'
        assert True

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except:
            assert False, 'Форма регистрации не найдена'
        assert True
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BookPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    #
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    #
    # def add_to_cart(self):
    #     try:
    #         self.browser.find_element(*BookPageLocators.CART_BUTTON).click()
    #     except:
    #         assert False, 'Кнопка корзины не найдена'
    #     assert True
    #
    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"
    #
    # def should_be_success_message(self):
    #     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         'Success message is presented'







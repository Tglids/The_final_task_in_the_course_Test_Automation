from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import BookPageLocators
from .locators import MainPageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def add_to_cart(self):
        try:
            self.browser.find_element(*BookPageLocators.CART_BUTTON).click()
        except:
            assert False, 'Кнопка корзины не найдена'
        assert True

    def comparison(self, browser):
        name = CartPage.should_name_in_cart(browser) == ProductPage.should_be_name_book(
            browser)
        price = CartPage.should_price_in_cart(browser) == ProductPage.should_be_price_book(
            browser)
        url = browser.current_url
        assert name and price, url

    def get_url(self):
        return self.browser.current_url

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return self.browser, self.browser.current_url


    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), 'Basket link is not presented'

    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def solve_quiz_and_get_code(self):
       alert = self.browser.switch_to.alert
       x = int(alert.text.split(" ")[2])
       try:
           res = str(math.log(abs((12 * math.sin(float(x))))))
           print(f"Your code: {res}")
           alert.send_keys(res)
           alert.accept()
       except NoAlertPresentException:
           print("No second alert presented")
           return False
       return True


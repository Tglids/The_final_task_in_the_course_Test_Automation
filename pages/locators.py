from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_EMAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_BTN_AUTORIZE = (By.CSS_SELECTOR, 'btn btn-lg btn-primary')
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REGISTER_BTN = (By.NAME, 'registration_submit')



class CartPageLocators():
    NAME_IN_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_IN_BASKET_TOP = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs(2)')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')


class BookPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRICE_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main p')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#basket-items')



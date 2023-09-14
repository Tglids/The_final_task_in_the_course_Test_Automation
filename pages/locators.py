from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class CartPageLocators():
    NAME_IN_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_IN_BASKET_TOP = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs(2)')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')


class BookPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRICE_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main p')

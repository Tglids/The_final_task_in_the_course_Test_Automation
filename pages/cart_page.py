from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):

    def should_name_in_cart(self):
        try:
            name = self.find_element(*CartPageLocators.NAME_IN_BASKET).text
            print(f'Имя в корзине {name}')
            return name
        except:
            assert False, 'Имя в корзине не найдено'

    def should_price_in_cart_top(self):
        try:
            price = self.find_element(*CartPageLocators.PRICE_IN_BASKET_TOP).text

            print(f'Цена в шапке корзины {price}')
            return price
        except:
            assert False, 'Цена в корзине не найдена'

    def should_price_in_cart(self):
        try:
            price = self.find_element(*CartPageLocators.PRICE_IN_BASKET).text
            print(f'Цена в синем окне корзины {price}')
            return price
        except:
            assert False, 'Цена в корзине не найдена'



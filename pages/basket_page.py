from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Item in the basket '

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), 'Корзина не пуста или нет текста'
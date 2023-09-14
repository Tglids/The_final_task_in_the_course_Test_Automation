from .locators import BookPageLocators
from .base_page import BasePage
from .main_page import MainPage

class ProductPage(BasePage):

    def should_be_name_book(self):
        try:
            name = self.find_element(*BookPageLocators.NAME_BOOK).text
            print(f'Имя на карточке {name}')
            return name
        except:
            assert False, 'Имя на карточке продукта не найдено'

    def should_be_price_book(self):
        try:
            price = self.find_element(*BookPageLocators.PRICE_BOOK).text
            print(f'Цена на карточке {price}')
            return price
        except:
            assert False, 'Цена на карточке продукта не найдена'
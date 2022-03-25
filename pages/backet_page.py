from locators import CartPageLocators
from base_page import BasePage


class CartPage(BasePage):
    def cart_should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.ADDED_ITEMS), 'Cart is not empty'

    def should_be_cart_page(self):
        assert 'basket' in self.browser.current_url

    def cart_empty_message_present(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_NOTIFICATION)

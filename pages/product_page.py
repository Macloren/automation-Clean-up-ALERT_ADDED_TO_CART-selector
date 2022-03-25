from basket_page import BasePage
from locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def should_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

    def should_solve_quiz(self):
        self.solve_quiz_and_get_code()

    def alert_should_popup(self):
        product_title = (self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)).text
        confirmation_title = (self.browser.find_element(*ProductPageLocators.CONFIRMATION_TITLE)).text
        assert product_title == confirmation_title, 'Added title does not match requested title'

    def prices_should_match(self):
        product_price = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)).text
        cart_price = (self.browser.find_element(*ProductPageLocators.CART_PRICE)).text
        assert product_price == cart_price, 'Prices do not match'

    def should_not_be_present(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is present, but shouldnt be'

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear"

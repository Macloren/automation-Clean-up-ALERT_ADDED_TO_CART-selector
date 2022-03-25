from pages.basket_page import CartPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   
    page.open()                      
    page.go_to_login_page()          

@pytest.mark.login_guest
class TestLoginMainPage():
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.cart_should_be_empty()
    cart_page.cart_empty_message_present()

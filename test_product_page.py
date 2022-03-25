from pages.login_page import LoginPage
from pages.basket_page import CartPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
import pytest
import time
import faker

base_url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
link1 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
offer1_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer7'

@pytest.mark.need_review
@pytest.mark.parametrize('promo', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_cart(browser, promo):
    link = f'{base_url}?promo=offer{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.should_solve_quiz()
    page.alert_should_popup()
    page.prices_should_match()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_add_to_cart()
    page.should_not_be_present()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_not_be_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_add_to_cart()
    time.sleep(1)
    page.should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link1)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.cart_should_be_empty()
    cart_page.cart_empty_message_present()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        f = faker.Faker()
        email = f.email()
        page.register_new_user(email, 'SuperSecret567')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_not_be_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_add_to_cart()
        #page.should_solve_quiz()
        page.alert_should_popup()
        page.prices_should_match()

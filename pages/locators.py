from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_CART_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email.form-control')
    PASS_FIELD = (By.CSS_SELECTOR, '#id_registration-password1.form-control')
    CONFIRM_PASS_FIELD = (By.CSS_SELECTOR, '#id_registration-password2.form-control')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value=\'Register\']')

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, '.alertinner :first-child')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon.alert-success.fade.in:first-child')

class CartPageLocators():
    ADDED_ITEMS = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_CART_NOTIFICATION = (By.CSS_SELECTOR, '#content_inner > p')

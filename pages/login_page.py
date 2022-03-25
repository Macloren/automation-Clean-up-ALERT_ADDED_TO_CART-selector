from base_page import BasePage
from locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.browser(*LoginPageLocators.LOGIN_FORM), "Login forn was not located"

    def should_be_register_form(self):
        assert self.browser(*LoginPageLocators.REGISTER_FORM), 'Registration form was not located'

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_address.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        pass_field.send_keys(password)
        confirm_pass = self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_FIELD)
        confirm_pass.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

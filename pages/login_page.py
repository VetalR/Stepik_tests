from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + 'password'
        self.browser.find_element(By.XPATH, "//*[@name='registration-email']").send_keys(email)
        self.browser.find_element(By.XPATH, "//*[@name='registration-password1']").send_keys(password)
        self.browser.find_element(By.XPATH, "//*[@name='registration-password2']").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, 'button[name="registration_submit"]').click()






    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_LINK), 'No register link'
        

    def should_be_login_form(self):
        self.browser.find_element(By.ID, "login_link").click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form'
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'No register form'
        
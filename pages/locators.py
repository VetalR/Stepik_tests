from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    REGISTER_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success.fade.in')
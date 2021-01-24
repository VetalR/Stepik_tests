from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
class LoginPageLocators():
    REGISTER_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.XPATH, "//*[@name='registration-email']")
    PASSWORD = (By.XPATH, "//*[@name='registration-password1']")
    REPEAT_PASSWORD = (By.XPATH, "//*[@name='registration-password2']")
class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success.fade.in')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    INTO_BASKET = (By.CSS_SELECTOR, 'div h1')
    BASKET_EMPTY = (By.CSS_SELECTOR, 'h2.col-sm-6')
    BASKET_EMPTY_TEXT = (By.XPATH, "//p/text()[1]")
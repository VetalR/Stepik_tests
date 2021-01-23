from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_LINK), 'No BASKET link'
        self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")   


    def should_be_name_equal(self):
        name_page = self.browser.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main :nth-child(1)').text
        name_basket = self.browser.find_element(By.CSS_SELECTOR, 'div.alertinner strong').text
        assert name_page == name_basket, 'not equal name'

    def should_be_price_equal(self):
        price_page = self.browser.find_element(By.CSS_SELECTOR, 'p.price_color').text
        price_basket = self.browser.find_element(By.CSS_SELECTOR, 'div.alertinner p strong').text
        assert price_page == price_basket, 'not equal price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
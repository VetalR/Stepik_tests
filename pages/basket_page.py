
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):           
    def go_to_basket_page(self):    # Переход к корзине
        self.browser.find_element(By.CSS_SELECTOR, '.btn-group a.btn.btn-default').click()

    def should_be_no_product(self):     # Проверка на отсутствие товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), 'Not empty basket'

    def add_some_to_basket(self):       # Добавление товара
        self.browser.find_element(By.CSS_SELECTOR, 'form  button.btn.btn-primary.btn-block').click()

    def should_be_text_empty_basket(self):      # Присутствие текста Корзина пуста
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), 'No Text empty basket'
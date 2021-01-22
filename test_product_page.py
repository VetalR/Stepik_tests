from .pages.product_page import ProductPage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()          # добавление книги
    page.solve_quiz_and_get_code()      # Работа с assert
    page.should_be_name_equal()     #сравнение наименований
    page.should_be_price_equal()        #сравнение цен
    page.should_not_be_success_message()


def test_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()          # добавление книги
    page.solve_quiz_and_get_code()      # Работа с assert
    page.should_be_name_equal()     #сравнение наименований
    page.should_be_price_equal()        #сравнение цен

@pytest.mark.parametrize('linked', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4","?promo=offer5",  
                                    "?promo=offer6",pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
def test_add_special(browser, linked):
   link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{linked}'
   page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
   page.open()                      # открываем страницу
   page.add_to_basket()          # добавление книги
   page.solve_quiz_and_get_code()      # Работа с assert
   page.should_be_name_equal()     #сравнение наименований
   page.should_be_price_equal()        #сравнение цен
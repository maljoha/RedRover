from selenium.webdriver.common.by import By

from Locators.order_locators import OrderLocators
from Pages.login_page import LoginPage


class TestCart():
    def test_add_to_cart(self, driver):
        login = LoginPage(driver, self.url)
        login.open()
        login.authorization(driver, "standard_user", "secret_sauce")
        item = driver.find_element(OrderLocators.INVENTORY_NAME).text
        driver.find_element(OrderLocators.ORDER_BTN).click()
        driver.find_element(OrderLocators.SHOPING_CART).click()
        assert driver.current_url == "https://www.saucedemo.com/v1/cart.html"
        cart_item = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        assert item == cart_item, "В корзину не добавлен выбранный товар"
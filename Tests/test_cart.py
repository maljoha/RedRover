from selenium.webdriver.common.by import By


class TestCart():
    def test_add_to_cart(self, driver):
        self.authorization(driver, "standard_user", "secret_sauce")
        item = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        driver.find_element(By.CSS_SELECTOR, "div.shopping_cart_container").click()
        assert driver.current_url == "https://www.saucedemo.com/v1/cart.html"
        cart_item = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        assert item == cart_item

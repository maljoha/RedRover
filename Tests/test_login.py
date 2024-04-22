from Locators.login_locators import LoginLocators


class TestLogin():

    def authorization(self, driver, login, password):
        driver.get('https://saucedemo.com/v1/')
        driver.find_element(*LoginLocators.USER_NAME).send_keys(login)
        driver.find_element(*LoginLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BTN).click()

    def test_authorization(self, driver):
        self.authorization(driver, "standard_user", "secret_sauce")
        assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'URL не соответствует ожидаемому'

    def test_wrong_authorization(self, driver):
        self.authorization(driver, "user", "user1")
        assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'URL не соответствует ожидаемому'


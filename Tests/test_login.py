from Locators.main_locators import MainLocators
from Pages.login_page import LoginPage
from src.units import Urls
from src.user_data import UserData


class TestLogin():
    url = Urls().base_url
    locators = MainLocators()

    def test_authorization(self, driver):
        login = LoginPage(driver, self.url)
        login.open()
        login.authorization(driver, UserData.login, UserData.password)
        actual_text = login.get_text(self.locators.TITLE)
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'URL не соответствует ожидаемому'
        assert actual_text == "Products", "Название раздела не 'Products'"

    def test_wrong_authorization(self, driver):
        login = LoginPage(driver, self.url)
        login.open()
        login.authorization(driver, "user", "user1")
        assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'URL не соответствует ожидаемому'

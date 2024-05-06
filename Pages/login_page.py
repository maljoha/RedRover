from Locators.login_locators import LoginLocators
from Pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginLocators()

    def authorization(self, driver, login, password):
        driver.find_element(*LoginLocators.USER_NAME).send_keys(login)
        driver.find_element(*LoginLocators.PASSWORD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BTN).click()

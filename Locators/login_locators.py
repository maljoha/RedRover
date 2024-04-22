from selenium.webdriver.common.by import By
class LoginLocators:
    USER_NAME = (By.XPATH, "//*[@id='user-name']")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login-button')

from selenium.webdriver.common.by import By


class MainLocators:
    TITLE = (By.CSS_SELECTOR, "span[data-test='title']")
    CARDS = (By.CSS_SELECTOR, "span[data-test='inventory-item']")

from selenium.webdriver.common.by import By


class OrderLocators():
    INVENTORY_NAME = (By.CSS_SELECTOR, "div.inventory_item_name")
    ORDER_BTN = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    SHOPING_CART = (By.CSS_SELECTOR, "div.shopping_cart_container")
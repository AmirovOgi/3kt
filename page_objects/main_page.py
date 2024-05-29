from page_objects.base_page import base_page
from selenium.webdriver.common.by import By

class main_page(base_page):
    search = (By.CSS_SELECTOR, "#search")
    macbook = (By.LINK_TEXT, "MacBook")

    droptablet = (By.LINK_TEXT, "Планшеты")
    droptelephone = (By.LINK_TEXT, "Телефоны")

    iphone = (By.LINK_TEXT, "iPhone")
    samsung = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
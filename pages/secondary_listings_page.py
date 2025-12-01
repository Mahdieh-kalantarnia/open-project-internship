from pages.base_page import Page
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class SecondaryListingPage:
    FILTERS_BTN = (By.XPATH, "//div[@class='filter-text']")
    WANT_BUY_BTN = (By.XPATH, "//div[text()='Want to buy']")
    APPLY_FILTER_BTN = (By.XPATH, "//a[text()='Apply filter']")
    LIST_ITEMS = (By.XPATH, "//div[text()='Want to buy']")

    def __init__(self, driver):
        self.driver = driver

        self.expected_url = "https://soft.reelly.io/secondary-listings"

    def is_page_opened(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.expected_url in d.current_url
            )
            return True
        except:
            return False


    def filters_icon(self):
        self.driver.find_element(*self.FILTERS_BTN).click()


    def want_to_buy_btn(self):
        self.driver.find_element(*self.WANT_BUY_BTN).click()

    def apply_filter_btn(self):
        self.driver.find_element(*self.APPLY_FILTER_BTN).click()

    def verify_all_tag(self):
        cards = self.driver.find_elements(*self.LIST_ITEMS)
        count = len(cards)
        print(f"Number of cards: {count}")
        return count

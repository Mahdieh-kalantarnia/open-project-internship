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
    FIRST_PRICE = (By.XPATH, "(//input[@id='field-5'])[1]")
    SECOND_PRICE = (By.XPATH, "(//input[@id='field-5'])[2]")
    PRICE_TEXT=(By.CSS_SELECTOR, ".number-price-text")




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

    def enter_first_price(self):
        self.driver.find_element(*self.FIRST_PRICE).send_keys("1200000")


    def enter_second_price(self):
        self.driver.find_element(*self.SECOND_PRICE).send_keys("2000000")


    def verify_all_price(self):
        min_price = 1200000
        max_price = 2000000

        prices = self.driver.find_elements(*self.PRICE_TEXT)

        for price in prices:
            price_text = price.get_attribute("innerText")

            clean_price = price_text.replace("AED", "").replace(",", "").replace("\xa0", "").strip()
            price_number = int(clean_price)

            assert min_price <= price_number <= max_price, \
                f"Price {price_number} is OUT of range!"

        print(f"All prices are within the range {min_price} - {max_price}(Test Passed).")

from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Enter the first price')
def enter_first_price(context):
    #context.driver.find_element(By.XPATH, "(//input[@id='field-5'])[1]").send_keys("1200000")
    context.app.secondary_listing_page.enter_first_price()


@then('Enter the second price')
def enter_second_price(context):
    #context.driver.find_element(By.XPATH, "(//input[@id='field-5'])[2]").send_keys("2000000")
    context.app.secondary_listing_page.enter_second_price()

@then('Verify the price')
def verify_price(context):
    # min_price = 1200000
    # max_price = 2000000
    #
    # prices = context.driver.find_elements(By.CSS_SELECTOR, ".number-price-text")
    #
    # for price in prices:
    #     price_text = price.get_attribute("innerText")
    #
    #
    #     clean_price = price_text.replace("AED", "").replace(",", "").replace("\xa0", "").strip()
    #     price_number = int(clean_price)
    #
    #
    #     assert min_price <= price_number <= max_price, \
    #         f"Price {price_number} is OUT of range!"
    #
    # print(f"All prices are within the range {min_price} - {max_price}(Test Passed).")
    context.app.secondary_listing_page.verify_all_price()
#from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('Open the main page')
def open_page(context):
    #   context.driver.get('https://soft.reelly.io')
    context.app.main_page.open_page()
    sleep(5)


@when('Enter username & password')
def enter_user_pass(context):
    #  context.driver.find_element(By.XPATH, "//input[@id='email-2']").send_keys("atefeh210@yahoo.com")
    #  context.driver.find_element(By.XPATH, "//input[@id='field']").send_keys("Atefeh.210!")
    context.app.signin_page.username_password()


@then('Click on Continue')
def click_continue(context):
    #    context.driver.find_element(By.XPATH, "//a[text()='Continue']").click()
    context.app.signin_page.continue_btn()
    sleep(5)

@then('Click on “Secondary” option')
def click_secondary(context):
    context.app.main_page.secondary_option()

@then('Verify the right page opens')
def verify_secondary(context):
    context.app.secondary_listing_page.is_page_opened()


@then('Click on Filters')
def click_filters(context):
    context.app.secondary_listing_page.filters_icon()
    sleep(2)

@then('Click want to buy btn')
def click_want_to_buy(context):
    context.app.secondary_listing_page.want_to_buy_btn()
    sleep(2)

@then('Click on apply filter btn')
def click_apply_filter(context):
    context.app.secondary_listing_page.apply_filter_btn()
    sleep(2)


@then('Verify all cards have tag')
def verify_all_tag(context):
    context.app.secondary_listing_page.verify_all_tag()
    sleep(2)
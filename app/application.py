from pages.base_page import Page
from pages.main_page import MainPage
from pages.signin_page import SignIn
from pages.secondary_listings_page import SecondaryListingPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self)
        self.signin_page = SignIn(driver)
        self.main_page = MainPage(driver)
        self.secondary_listing_page = SecondaryListingPage(driver)

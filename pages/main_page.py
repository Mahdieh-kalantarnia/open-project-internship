from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

      SECONDARY_BTN = (By.XPATH, "//div[text()='Secondary']")

      def open_page(self):
        self.open_url('https://soft.reelly.io')


      def secondary_option(self):
          self.driver.find_element(*self.SECONDARY_BTN).click()

          sleep(10)
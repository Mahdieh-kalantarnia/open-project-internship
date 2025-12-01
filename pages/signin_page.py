from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page




class SignIn(Page):

    USERNAME = (By.XPATH, '//input[@id="email-2"]')
    PASSWORD = (By.XPATH, '//input[@id="field"]')
    CONTINUE = (By.XPATH, '//a[text()="Continue"]')


    def username_password(self):

     self.driver.find_element(*self.USERNAME).send_keys("atefeh210@yahoo.com")
     self.driver.find_element(*self.PASSWORD).send_keys("Atefeh.210!")


    def continue_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE)
        )


        self.driver.execute_script("arguments[0].click();", element)




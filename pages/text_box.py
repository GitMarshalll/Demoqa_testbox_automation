from selenium.webdriver.common.by import By
from base.base_page import BasePage

class Text_Box_Page(BasePage):
    username_input = (By.XPATH, '//input[@id="userName"]')

    def enter_username(self, username):
        self.input_text(self.username_input, username)

    email_input = (By.XPATH, '//input[@id="userEmail"]')

    def enter_email(self, email):
        self.input_text(self.email_input, email)

    currentadd_input = (By.XPATH, '//textarea[@id="currentAddress"]')

    def enter_currentadd(self, currentadd):
        self.input_text(self.currentadd_input, currentadd)

    permanentadd_input = (By.XPATH, '//textarea[@id="permanentAddress"]')

    def enter_permanentadd(self, permanentadd):
        self.input_text(self.permanentadd_input, permanentadd)

    submit_button = (By.XPATH, '//button[@id="submit"]')

    def click_submit_button(self):
        self.click(self.submit_button)










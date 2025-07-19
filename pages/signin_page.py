from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):


    EMAIL_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a[wized="loginButton"]')

    def open_signin_page(self):
        self.driver.get('https://soft.reelly.io')
        sleep(3)

    def enter_email(self, text, *locator):
        self.input_text("***", *self.EMAIL_FIELD)

    def enter_password(self, text, *locator):
        self.input_text("***", *self.PASSWORD_FIELD)

    def click_continue(self):
        self.wait_for_element_click(*self.CONTINUE_BTN)

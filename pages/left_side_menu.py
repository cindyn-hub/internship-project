from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class LeftSideMenu(Page):

    OFF_PLAN_BTN =(By.CSS_SELECTOR, 'a[wized="newOffPlanLink"]')

    def click_off_plan_button(self):
        self.wait_for_element_click(*self.OFF_PLAN_BTN)

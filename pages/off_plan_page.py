from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class OffPlanPage(Page):


    SALE_STATUS_BTN = (By.XPATH, '//button[text()="Sale Status"]')
    OUT_OF_STOCK_BTN = (By.XPATH, '//div[text()="Out of Stock"]')
    OUT_OF_STOCK_TAG = (By.XPATH, '//button[text()="Out of stock"]')



    def verify_off_plan_opened(self):
        self.wait_for_url_contains("?pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1")

    def click_sale_status(self):
        self.wait_for_element_click(*self.SALE_STATUS_BTN)

    def click_out_of_stock(self):
        self.wait_for_element_click(*self.OUT_OF_STOCK_BTN)

    def verify_out_of_stock(self):
        out_of_stock_tags = self.driver.find_elements(*self.OUT_OF_STOCK_TAG)
        print(out_of_stock_tags)



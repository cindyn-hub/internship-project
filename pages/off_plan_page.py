from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class OffPlanPage(Page):
    SALE_STATUS_BTN = (By.XPATH, '//button[text()="Sale Status"]')
    OUT_OF_STOCK_BTN = (By.XPATH, '//div[text()="Out of Stock"]')
    PRODUCT_CARDS = (By.XPATH, '//div[@class="absolute top-4 left-4 flex gap-1"]')

    def verify_off_plan_opened(self):
        self.wait_for_url_contains("?pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1")

    def click_sale_status(self):
        self.wait_for_element_click(*self.SALE_STATUS_BTN)

    def click_out_of_stock(self):
        self.wait_for_element_click(*self.OUT_OF_STOCK_BTN)

    def verify_all_out_of_stock(self):
        expected_text = "Out of stock"
        all_valid = True

        product_cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        print(f" Found {len(product_cards)} product cards.")


        for i, card in enumerate(product_cards, start=1):
            spans = card.find_elements(By.XPATH, './/span[contains(@class, "bg-white")]')
            tags_text = [span.text.strip() for span in spans]

            found = any(expected_text.lower() in tag.lower() for tag in tags_text)

            if found:
                print(f"Product {i} contains 'Out of stock'")
            else:
                print(f"Product {i} does NOT contain 'Out of stock'")
                all_valid = False

        assert all_valid, "One or more of the products are missing the 'Out of stock' tag."
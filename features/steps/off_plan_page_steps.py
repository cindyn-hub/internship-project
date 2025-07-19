from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify off plan page opens')
def verify_off_plan_page_opened(context):
    context.app.off_plan_page.verify_off_plan_opened()

@when('Filter by Out of Stocks')
def filter_out_of_stocks(context):
    context.app.off_plan_page.click_sale_status()
    context.app.off_plan_page.click_out_of_stock()
    context.app.off_plan_page.click_sale_status()

@then('Verify products have Out of Stock tag')
def verify_out_of_stock(context):
    context.app.off_plan_page.verify_out_of_stock()

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click off plan')
def click_off_plan(context):
    context.app.left_side_menu.click_off_plan_button()

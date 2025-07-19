from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_main_page(context):
    context.app.signin_page.open_signin_page()

@when('Log in to page')
def enter_creds_and_continue(context):
    context.app.signin_page.enter_email(context)
    context.app.signin_page.enter_password(context)
    context.app.signin_page.click_continue()
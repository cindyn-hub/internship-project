from pages.base_page import Page
from pages.signin_page import SignInPage
from pages.left_side_menu import LeftSideMenu
from pages.off_plan_page import OffPlanPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.signin_page = SignInPage(driver)
        self.left_side_menu = LeftSideMenu(driver)
        self.off_plan_page = OffPlanPage(driver)
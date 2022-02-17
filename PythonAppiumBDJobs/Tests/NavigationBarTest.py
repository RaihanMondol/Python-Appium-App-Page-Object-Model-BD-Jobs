import time

import self as self

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.NavigationBarPage import Main_navBar


class SearchTest(BasePage):
    def test_navbar(self):
        login = LoginPage(self.driver)
        login.click_first_next_button()
        time.sleep(3)
        login.click_allow_button()
        time.sleep(3)
        login.click_signIn_icon()
        time.sleep(3)
        login.enter_username("rm.qups@gmail.com")
        time.sleep(3)
        login.click_arrow_next_button()
        time.sleep(3)
        login.enter_password("rm123456789")
        time.sleep(3)
        login.click_arrow_next_button()
        time.sleep(10)

        navbar = Main_navBar(self.driver)
        navbar.click_hotjobs()
        time.sleep(10)
        navbar.click_shortlisted()
        time.sleep(10)
        navbar.click_mybdjobs()
        time.sleep(10)
        navbar.click_more()

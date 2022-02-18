import time

import self as self

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.SearchJobPage import SearchPage


class SearchTest(BasePage):

    def test_searchJob(self):
        login = LoginPage(self.driver)
        login.click_first_next_button()
        time.sleep(3)
        login.click_allow_button()
        time.sleep(5)
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

        search = SearchPage(self.driver)
        time.sleep(3)
        search.click_search_icon()
        time.sleep(3)
        search.enter_keyword("QA Engineer")
        time.sleep(3)
        search.enter_general_category("IT/Telecommunication")
        time.sleep(3)
        search.select_experience()
        time.sleep(3)
        search.click_final_search_icon()
        time.sleep(10)

        self.driver.swipe(400, 1500, 400, 800, 1000)

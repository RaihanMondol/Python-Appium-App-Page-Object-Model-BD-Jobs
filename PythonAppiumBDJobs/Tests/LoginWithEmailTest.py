import time

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class LoginTest(BasePage):

    def test_LoginPage(self):
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

from Pages.HomePage import HomePage
from Locators.Locators import LoginLocators

class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator =  LoginLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_first_next_button(self):
        self.find_element(*self.locator.first_next_buton_id).click()

    def click_allow_button(self):
        self.find_element(*self.locator.allow_button_id).click()

    def click_signIn_icon(self):
        self.find_element(*self.locator.signin_icon_id).click()

    def enter_username(self, username):
        self.find_element(*self.locator.enter_username_textbox_id).send_keys(username)

    def click_arrow_next_button(self):
        self.find_element(*self.locator.arrow_button_id).click()

    def enter_password(self, password):
        self.find_element(*self.locator.enter_password_textbox_id).send_keys(password)
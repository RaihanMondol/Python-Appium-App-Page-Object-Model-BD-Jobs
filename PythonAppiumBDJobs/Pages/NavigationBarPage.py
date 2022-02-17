from Locators.Locators import NavigationBarLocators
from Pages.HomePage import HomePage


class Main_navBar(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = NavigationBarLocators
        self.driver = driver
        super(Main_navBar, self).__init__(driver)

    def click_hotjobs(self):
        self.find_element(*self.locator.hotjobs_button_id).click()

    def click_shortlisted(self):
        self.find_element(*self.locator.shortlisted_button_id).click()

    def click_mybdjobs(self):
        self.find_element(*self.locator.myBdjobs_button_id).click()

    def click_more(self):
        self.find_element(*self.locator.more_button_id).click()

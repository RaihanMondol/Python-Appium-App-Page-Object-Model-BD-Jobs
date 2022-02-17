from Locators.Locators import SearchJobLocators
from Pages.HomePage import HomePage


class SearchPage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = SearchJobLocators
        self.driver = driver
        super(SearchPage, self).__init__(driver)

    def click_search_icon(self):
        self.find_element(*self.locator.search_button_id).click()

    def enter_keyword(self, text):
        self.find_element(*self.locator.keyword_textbox_id).send_keys(text)

    def enter_general_category(self, text):
        self.find_element(*self.locator.general_category_id).send_keys(text)

    def select_experience(self):
        self.find_element(*self.locator.experience_button_id).click()

    def click_final_search_icon(self):
        self.find_element(*self.locator.final_search_icon_id).click()

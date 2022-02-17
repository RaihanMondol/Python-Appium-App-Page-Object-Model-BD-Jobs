import unittest
from appium import webdriver


class BasePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  'automationName': 'UiAutomator2',
                                  'platformVersion': '10',
                                  'udid': 'emulator-5554',
                                  'app': 'D:/pythonProject/PythonAppiumBDJobs/APK/com.bdjobs.app-v2.8.0.3.apk'

                                  }
        )
        print("Test Started.......")

    def tearDown(self):
        # self.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()

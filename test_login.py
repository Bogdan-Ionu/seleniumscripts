import sys
sys.path.append("C:/Users/Bogdan/logintest/test")
print(sys.path)

from selenium import webdriver
import unittest
import time


from pages.logintest import LoginPage as LP

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200")
        self.driver.maximize_window()

    def test_login(self):
        loginPage = LP(self.driver)

        loginPage.goToLogin()
        time.sleep(2)
        loginPage.clickLoginNav()
        time.sleep(2)
        loginPage.setUsername("b@a.com")
        time.sleep(2)
        loginPage.setPassowrd("b")
        time.sleep(2)
        loginPage.clickLogin()
        time.sleep(2)
        loginPage.logoutButton()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
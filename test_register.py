import sys
sys.path.append("C:/Users/Bogdan/logintest/test")
print(sys.path)

from selenium import webdriver
import unittest
import time


from pages.registertest import RegisterPage as RP

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200")
        self.driver.maximize_window()

    def test_register(self):
        registerPage = RP(self.driver)

        registerPage.goToRegister()
        time.sleep(2)
        registerPage.clickRegisterNav()
        time.sleep(2)
        registerPage.setUsername("m@m.com")
        time.sleep(2)
        registerPage.setPassowrd("m")
        time.sleep(2)
        registerPage.clickRegister()
        time.sleep(2)
        registerPage.logoutButton()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
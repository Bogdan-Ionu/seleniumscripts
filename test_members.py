import sys
sys.path.append("C:/Users/Bogdan/logintest/test")
print(sys.path)

from selenium import webdriver
import unittest
import time


from pages.memberstest import MembersPage as MP

class MembersTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200")
        self.driver.maximize_window()

    def test_login(self):
        membersPage = MP(self.driver)

        membersPage.goToMembers()
        time.sleep(2)
        membersPage.clickMembersNav()
        time.sleep(2)
        membersPage.setUsername("b@b.com")
        time.sleep(2)
        membersPage.setPassowrd("b")
        time.sleep(2)
        membersPage.clickLogin()
        time.sleep(2)
        membersPage.logoutButton()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
from selenium.webdriver.common.by import By
from locators.locators import MembersLocators

class MembersPage:
    def __init__(self, driver):
        self.driver = driver
    
    def goToMembers(self):
        self.driver.get("http://localhost:4200")

    def clickMembersNav(self):
        nav_members = self.driver.find_element(*MembersLocators.nav_members)
        nav_members.click()

    def setUsername(self, userVal): 
        username = self.driver.find_element(*MembersLocators.username)
        username.clear()
        username.send_keys(userVal)

    def setPassowrd(self, passVal):
        password = self.driver.find_element(*MembersLocators.password)
        password.clear()
        password.send_keys(passVal) 

    def clickLogin(self):
        loginButton = self.driver.find_element(*MembersLocators.loginButton)
        loginButton.click()

    def logoutButton(self):
        logoutButton = self.driver.find_element(*MembersLocators.logoutButton)
        logoutButton.click()
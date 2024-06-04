from selenium.webdriver.common.by import By
from locators.locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def goToLogin(self):
        self.driver.get("http://localhost:4200")

    def clickLoginNav(self):
        nav_login = self.driver.find_element(*LoginLocators.nav_login)
        nav_login.click()

    def setUsername(self, userVal): 
        username = self.driver.find_element(*LoginLocators.username)
        username.clear()
        username.send_keys(userVal)

    def setPassowrd(self, passVal):
        password = self.driver.find_element(*LoginLocators.password)
        password.clear()
        password.send_keys(passVal) 

    def clickLogin(self):
        loginButton = self.driver.find_element(*LoginLocators.loginButton)
        loginButton.click()

    def logoutButton(self):
        logoutButton = self.driver.find_element(*LoginLocators.logoutButton)
        logoutButton.click()


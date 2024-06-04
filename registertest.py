from selenium.webdriver.common.by import By
from locators.locators import LoginLocators
from locators.locators import RegisterLocators

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
    
    def goToRegister(self):
        self.driver.get("http://localhost:4200")

    def clickRegisterNav(self):
        nav_register = self.driver.find_element(*RegisterLocators.nav_register)
        nav_register.click()

    def setUsername(self, userVal): 
        username = self.driver.find_element(*RegisterLocators.username)
        username.clear()
        username.send_keys(userVal)

    def setPassowrd(self, passVal):
        password = self.driver.find_element(*RegisterLocators.password)
        password.clear()
        password.send_keys(passVal) 

    def clickRegister(self):
        registerButton = self.driver.find_element(*RegisterLocators.registerButton)
        registerButton.click()

    def logoutButton(self):
        logoutButton = self.driver.find_element(*RegisterLocators.logoutButton)
        logoutButton.click()

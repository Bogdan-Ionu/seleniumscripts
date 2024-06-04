from selenium.webdriver.common.by import By

class LoginLocators:
    nav_login = (By.XPATH, "(//a[normalize-space()='Login'])[1]")
    username = (By.XPATH, "(//input[@name='email'])[1]")
    password = (By.XPATH, "(//input[@name='password'])[1]")
    loginButton = (By.XPATH, "(//button[normalize-space()='Login'])[1]")
    logoutButton = (By.XPATH, "(//a[normalize-space()='Logout'])[1]")

class RegisterLocators:
    nav_register = (By.XPATH, "//a[normalize-space()='Register']")
    username = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@name='password']")
    registerButton = (By.XPATH, "//button[normalize-space()='Register']")
    logoutButton = (By.XPATH, "(//a[normalize-space()='Logout'])[1]")

class MembersLocators:
    nav_members = (By.XPATH, "//a[normalize-space()='Membrii']")
    username = (By.XPATH, "(//input[@name='email'])[1]")
    password = (By.XPATH, "(//input[@name='password'])[1]")
    loginButton = (By.XPATH, "(//button[normalize-space()='Login'])[1]")
    logoutButton = (By.XPATH, "(//a[normalize-space()='Logout'])[1]")
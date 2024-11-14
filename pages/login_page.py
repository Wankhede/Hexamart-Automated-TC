from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        driver.set_page_load_timeout(30)  # Wait for 30 seconds for page load

        self.username_field ="//*[@name='username']"
        self.password_field = "//*[@name='password']"
        self.login_button = "//*[@type='submit']"
        self.stay_logged_in_button = "//*[@name='checked']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.password_field).send_keys(password)

    def click_stay_logged_in(self):
        self.driver.find_element(By.XPATH,self.stay_logged_in_button).click()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

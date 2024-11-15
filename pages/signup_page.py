from selenium.webdriver.common.by import By


class SignupPage:
    def __init__(self, driver_signup):
        self.driver = driver_signup
        self.driver.set_page_load_timeout(30)

        self.account_exist = "//*[@href='/register']"
        self.salon_name_field = "//*[@placeholder='Enter your name']"
        self.email_field = "//*[@placeholder=\"Enter owner's email address\"]"
        self.contact_field = "//*[@placeholder='Enter contact number']"
        self.password_field = "//*[@placeholder='Enter password']"
        self.confirm_password_field = "//*[@placeholder='Confirm password']"
        self.owner_name_field = "//*[@placeholder=\"Enter owner's name\"]"
        self.submit_button = "//*[@type='submit']"
        self.name_error = "//*[@id='standard-weight-helper-text-name-login']"

    def enter_salon_name(self, salon_name):
        self.driver.find_element(By.XPATH, self.salon_name_field).send_keys(salon_name)

    def enter_owner_name(self, owner_name):
        self.driver.find_element(By.XPATH, self.owner_name_field).send_keys(owner_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    def enter_contact(self, contact):
        self.driver.find_element(By.XPATH, self.contact_field).send_keys(contact)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_field).send_keys(confirm_password)

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()

    def name_error_message(self):
        return self.driver.find_element(By.XPATH, self.name_error).text

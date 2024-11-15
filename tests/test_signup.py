from time import sleep

import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from tests.conftest import driver_signup
from utils.config import OWNER_NAME, BLANK_OWNER_NAME, SALON_NAME, EMAIL, CONTACT_NUM, PASSWORD, CONFIRM_PASSWORD

class TestSignup:

    @pytest.fixture(autouse=True)
    def setup(self, driver_signup):
        """Fixture to set up the page object and driver."""
        self.driver = driver_signup
        self.driver.implicitly_wait(10)
        self.signupPage = SignupPage(self.driver)

    # # def test_missing_owner_signup(self):
    #     self.signupPage.enter_salon_name(SALON_NAME)
    #     self.signupPage.enter_owner_name(BLANK_OWNER_NAME)
    #     self.signupPage.enter_email(EMAIL)
    #     self.signupPage.enter_contact(CONTACT_NUM)
    #     self.signupPage.enter_password(PASSWORD)
    #     self.signupPage.enter_confirm_password(CONFIRM_PASSWORD)
    #     self.signupPage.click_signup()
    #     sleep(5)
    #
    #
    # # def test_missing_all_fields_signup(self):
    #     submit_button_1 = self.driver.find_element(By.XPATH, "//*[@type='submit']")
    #     err_pop_username_1 = self.driver.find_element(By.XPATH,"//*[@class='MuiAlert-message css-12v1nhx-MuiAlert-message']")
    #
    #     assert not submit_button_1.is_displayed(), "Submit button is visible when it shouldn't be!Submit button is visible when it shouldn't be!"
    #     self.signupPage.click_signup()
    #     assert not err_pop_username_1.is_displayed(), "Submit button is not visible "
    #
    # # def test_valid_signup(self):
    #     self.signupPage.enter_owner_name(OWNER_NAME)
    #     self.signupPage.enter_salon_name(SALON_NAME)
    #     self.signupPage.enter_email(EMAIL)
    #     self.signupPage.enter_contact(CONTACT_NUM)
    #     self.signupPage.enter_password(PASSWORD)
    #     assert self.signupPage.click_signup().is_visible() == False
    #     self.signupPage.enter_confirm_password(CONFIRM_PASSWORD)
    #     assert self.signupPage.click_signup().is_visible() == True
    #     self.signupPage.click_signup()

    def test_already_exists_signup(self):
        self.signupPage.enter_owner_name(OWNER_NAME)
        self.signupPage.enter_salon_name(SALON_NAME)
        self.signupPage.enter_email(EMAIL)
        self.signupPage.enter_contact(CONTACT_NUM)
        self.signupPage.enter_password(PASSWORD)
        submit_button_1 = self.driver.find_element(By.XPATH, "//*[@type='submit']")
        assert not submit_button_1.is_enabled(), "Submit button is visible when it shouldn't be!Submit button is visible when it shouldn't be!"
        self.signupPage.enter_confirm_password(CONFIRM_PASSWORD)
        assert submit_button_1.is_enabled(), "Submit button is visible "
        assert "Username Already Exists" in self.driver.page_source
        if "Username Already Exists" in self.driver.page_source:
            # Navigate to login page
            self.driver.find_element(By.XPATH, "//*[@href='/login']").click()

            # Wait for login page to load
            sleep(3)  # Adjust this based on actual load time or replace with WebDriverWait if needed
            self.loginPage = LoginPage(self.driver)  # Initialize the login page instance

            # Login with the same credentials
            self.login_page.enter_username(EMAIL)
            self.login_page.enter_password(PASSWORD)
            self.login_page.click_stay_logged_in()
            self.login_page.click_login()

            sleep(10)  # Wait for login to complete (can be adjusted)

            # Capture screenshot after login attempt
            self.driver.save_screenshot(f"screenshot-{int(time.time())}.png")
            assert "Pricing" in self.driver.title  # Verify login success by checking page title
        else:
            # If no error message, assert successful signup (depending on what indicates signup success)
            assert "Signup Success Message" in self.driver.page_source



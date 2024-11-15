from time import sleep
import pytest
from selenium.webdriver.common.by import By


from pages.login_page import LoginPage
from tests.conftest import driver_login
from utils.config import USERNAME, PASSWORD, WRONG_USERNAME, PASSWORD_WRONG

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver_login):
        """Fixture to set up the page object and driver."""
        self.driver = driver_login
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)

    def test_valid_login_creds(self):
        """Test for valid login credentials."""
        self.login_page.enter_username(USERNAME)
        self.login_page.enter_password(PASSWORD)
        self.login_page.click_stay_logged_in()
        self.login_page.click_login()

        sleep(10)
        self.driver.save_screenshot("screenshot-%(time).png")
        assert "Pricing" in self.driver.title  # Adjust as needed to match the actual title after login

    def test_invalid_login_creds(self):
        """Test for invalid login credentials."""
        self.login_page.enter_username(WRONG_USERNAME)
        self.login_page.enter_password(PASSWORD_WRONG)
        self.login_page.click_stay_logged_in()
        self.login_page.click_login()
        sleep(3)
        err = self.driver.find_element(By.XPATH, "//*[@class='MuiFormHelperText-root Mui-error css-1z0uwg0-MuiFormHelperText-root']")
        self.driver.save_screenshot("screenshot-%(time).png")
        assert "Verify Your Username & Password" in err.text

    def test_invalid_login_only_username(self):
        """Test for invalid login username credentials."""
        self.login_page.enter_username(WRONG_USERNAME)
        self.login_page.enter_password(PASSWORD)
        self.login_page.click_stay_logged_in()
        self.login_page.click_login()
        sleep(3)
        err = self.driver.find_element(By.XPATH, "//*[@class='MuiFormHelperText-root Mui-error css-1z0uwg0-MuiFormHelperText-root']")
        self.driver.save_screenshot("screenshot-%(time).png")
        assert "Verify Your Username & Password" in err.text

    def test_invalid_login_only_password(self):
        """Test for invalid login username credentials."""
        self.login_page.enter_username(USERNAME)
        self.login_page.enter_password(PASSWORD_WRONG)
        self.login_page.click_stay_logged_in()
        self.login_page.click_login()
        sleep(3)
        err = self.driver.find_element(By.XPATH, "//*[@class='MuiFormHelperText-root Mui-error css-1z0uwg0-MuiFormHelperText-root']")
        self.driver.save_screenshot("screenshot-%(time).png")
        assert "Verify Your Username & Password" in err.text